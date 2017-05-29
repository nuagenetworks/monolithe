# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from future import standard_library
from urlparse import urlparse
standard_library.install_aliases()

import os, uuid
from configparser import RawConfigParser
from shutil import copyfile, rmtree, copytree
from os import remove, makedirs

from monolithe.lib import SDKUtils, TaskManager
from monolithe.generators.lib import TemplateFileWriter
from monolithe.specifications import SpecificationAPI

class APIVersionWriter(TemplateFileWriter):
    """ Provide useful method to write Java files.

    """
    def __init__(self, monolithe_config, api_info):
        """ Initializes a _JavaSDKAPIVersionFileWriter

        """
        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.vro")

        self.api_version = api_info["version"]
        self._api_version_string = SDKUtils.get_string_version(self.api_version)
        self.api_root = api_info["root"]
        self.api_prefix = api_info["prefix"]

        self.monolithe_config = monolithe_config
        self._output = self.monolithe_config.get_option("output", "transformer")
        self._name = self.monolithe_config.get_option("name", "transformer")
        self._class_prefix = ""
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._product_name = self.monolithe_config.get_option("product_name")
        self._url = self.monolithe_config.get_option("url", "transformer")

        self._package_prefix = self._get_package_prefix(self._url)
        self._package_name = self._package_prefix + ".vro." + self._name
        self._package_subdir = self._package_name.replace('.', '/')

        self.output_directory = "%s/vro" % (self._output)
        self.override_folder = os.path.normpath("%s/__overrides" % self.output_directory)
        self.fetchers_path = "/fetchers/"
        self.enums_path = "/enums/"

        self.attrs_defaults = RawConfigParser()
        path = "%s/vro/__attributes_defaults/attrs_defaults.ini" % self._output
        self.attrs_defaults.optionxform = str
        self.attrs_defaults.read(path)

        self.inventory_entities = RawConfigParser()
        path = "%s/vro/__attributes_defaults/inventory_entities.ini" % self._output
        self.inventory_entities.optionxform = str
        self.inventory_entities.read(path)

        self.workflow_attrs = RawConfigParser()
        path = "%s/vro/__attributes_defaults/workflow_attrs.ini" % self._output
        self.workflow_attrs.optionxform = str
        self.workflow_attrs.read(path)

        self.attrs_types = RawConfigParser()
        path = "%s/vro/__attributes_defaults/attrs_types.ini" % self._output
        self.attrs_types.optionxform = str
        self.attrs_types.read(path)

        self.plugin_version = self.monolithe_config.get_option("version", "transformer")

        self.workflow_version = self.monolithe_config.get_option("version", "transformer")

        with open("%s/vro/__code_header" % self._output, "r") as f:
            self.header_content = f.read()

    def perform(self, specifications):
        """
        """
        self._resolve_parent_apis(specifications) # Temporary fix, see method's comment for more info
        self._set_local_and_workflow_type(specifications) # Temporary until get_type_name is enhanced to include specificiation subtype and local_name

        self._write_file(self.output_directory, "pom.xml.tpl", "pom.xml")
        self._write_o11plugin(specifications)
        self._write_o11plugin_core(specifications)
        self._write_o11plugin_package(specifications)

    def _write_o11plugin(self, specifications):
        """
        """
        output_directory = "%s/o11nplugin-%s" % (self.output_directory, self._name.lower())
        self._write_file(output_directory, "o11nplugin/pom.xml.tpl", "pom.xml")
        license_output_directory = "%s/src/main/vmoapp/VSO-INF" % (output_directory)
        os.makedirs(license_output_directory)
        copyfile("%s/LICENSE" % (self.output_directory), "%s/vsoapp.txt" % (license_output_directory));

        icons_output_directory = "%s/src/main/dar/resources/images" % (output_directory)
        os.makedirs(icons_output_directory)
        icons_source_directory = "%s/__icons" % (self.output_directory)
        self._copyfile("icon-plugin.png", icons_source_directory, icons_output_directory)
        self._copyfile("icon-session.png", icons_source_directory, icons_output_directory)
        self._copyfile("icon-folder.png", icons_source_directory, icons_output_directory)
        for rest_name, specification in specifications.items():
            self._copyfile("icon-%s.png" % (specification.entity_name.lower()), icons_source_directory, icons_output_directory)
        rmtree("%s" % (icons_source_directory))

    def _write_o11plugin_core(self, specifications):
        """
        """
        output_directory = "%s/o11nplugin-%s-core" % (self.output_directory, self._name.lower())
        self._write_file(output_directory, "o11nplugin-core/pom.xml.tpl", "pom.xml")
        
        source_output_directory = "%s/src/main/java/%s" % (output_directory, self._package_subdir)
        self._write_modulebuilder(source_output_directory, package_name=self._package_name)
        self._write_pluginadaptor(source_output_directory, package_name=self._package_name)
        self._write_pluginfactory(specifications, source_output_directory, package_name=self._package_name)

        model_package_name = self._package_name + ".model"
        model_source_output_directory = "%s/model" % (source_output_directory)
        self._write_constants(specifications, model_source_output_directory, package_name=model_package_name)
        self._write_sessionmanager(model_source_output_directory, package_name=model_package_name)
        self._write_session(specifications, model_source_output_directory, package_name=model_package_name)
        self._write_modelhelper(specifications, model_source_output_directory, package_name=model_package_name)

        task_manager = TaskManager()
        for rest_name, specification in specifications.items():
            task_manager.start_task(method=self._write_model, specification=specification, specification_set=specifications, output_directory=model_source_output_directory, package_name=model_package_name)
            task_manager.start_task(method=self._write_fetcher, specification=specification, specification_set=specifications, output_directory=model_source_output_directory, package_name=model_package_name)
            for attribute in specification.attributes:
                if attribute.type == "enum" or attribute.subtype == "enum":
                    task_manager.start_task(method=self._write_enum, specification=specification, attribute=attribute, output_directory=model_source_output_directory, package_name=model_package_name)

        task_manager.wait_until_exit()

    def _write_o11plugin_package(self, specifications):
        """
        """
        output_directory = "%s/o11nplugin-%s-package" % (self.output_directory, self._name.lower())
        self._write_file(output_directory, "o11nplugin-package/pom.xml.tpl", "pom.xml")
        self._write_file("%s/src/main/resources/META-INF" % (output_directory), "o11nplugin-package/dunes-meta-inf.xml.tpl", "dunes-meta-inf.xml")
        copyfile("%s/archetype.keystore" % (self.output_directory), "%s/archetype.keystore" % (output_directory));
        remove("%s/archetype.keystore" % (self.output_directory))

        resources_output_directory = "%s/src/main/resources" % (output_directory)
        workflows_output_directory = "%s/Workflow" % (resources_output_directory)        
        actions_output_directory = "%s/ScriptModule" % (resources_output_directory)

        workflow_package = "Session"
        workflow_directory = "%s/Library/VSPK/Basic/%s" % (workflows_output_directory, workflow_package)
        self._write_workflow_file(specification=None, specification_set=None, workflow_directory=workflow_directory, template_file="o11nplugin-package/Add Session.element_info.xml.tpl", filename="Add Session.element_info.xml", workflow_type="add", workflow_id=None, attrs_includes=None, attrs_excludes=None, workflow_name="Add Session", workflow_package=workflow_package, parent_spec=None)
        self._write_workflow_file(specification=None, specification_set=None, workflow_directory=workflow_directory, template_file="o11nplugin-package/Add Session.xml.tpl", filename="Add Session.xml", workflow_type="add", workflow_id=None, attrs_includes=None, attrs_excludes=None, workflow_name = "Add Session", workflow_package=workflow_package, parent_spec=None)
        self._write_workflow_file(specification=None, specification_set=None, workflow_directory=workflow_directory, template_file="o11nplugin-package/Remove Session.element_info.xml.tpl", filename="Remove Session.element_info.xml", workflow_type="remove", workflow_id=None, attrs_includes=None, attrs_excludes=None, workflow_name = "Remove Session", workflow_package=workflow_package, parent_spec=None)
        self._write_workflow_file(specification=None, specification_set=None, workflow_directory=workflow_directory, template_file="o11nplugin-package/Remove Session.xml.tpl", filename="Remove Session.xml", workflow_type="remove", workflow_id=None, attrs_includes=None, attrs_excludes=None, workflow_name = "Remove Session", workflow_package=workflow_package, parent_spec=None)

        for rest_name, specification in specifications.items():
            for attribute in specification.attributes:
                attrs_includes = self._get_entity_list_filter(self.workflow_attrs, specification.entity_name, "includes")
                attrs_excludes = self._get_entity_list_filter(self.workflow_attrs, specification.entity_name, "excludes")
                if (attribute.required or attribute.local_name in attrs_includes) and (not attribute.local_name in attrs_excludes):
                    if attribute.type == "enum" or attribute.type == "list":
                        self._write_action_files(specification=specification, attribute=attribute, package_name=self._package_name, output_directory=actions_output_directory)

        for rest_name, specification in specifications.items():
            if not specification.is_root:
                attrs_includes = self._get_entity_list_filter(self.workflow_attrs, specification.entity_name, "includes")
                attrs_excludes = self._get_entity_list_filter(self.workflow_attrs, specification.entity_name, "excludes")

                for parent_api in specification.parent_apis:
                   workflow_package = "Other" if specification.package is None else specification.package.capitalize()
                   if parent_api.rest_name in specifications:
                      parent_spec = specifications[parent_api.rest_name]
                      if parent_spec:
                         entity_excludes = self._get_entity_list_filter(self.inventory_entities, parent_spec.entity_name, "excludes")
                         if specification.entity_name not in entity_excludes:
                            if parent_api.allows_create:
                               self._write_workflow_files(specification=specification, specification_set=specifications, output_directory=workflows_output_directory, workflow_type="add", attrs_includes=attrs_includes, attrs_excludes=attrs_excludes, workflow_name="Add %s to %s" % (specification.entity_name, parent_spec.entity_name), workflow_package=workflow_package, parent_spec=parent_spec)
                            if parent_api.allows_create or parent_spec.is_root:
                               self._write_workflow_files(specification=specification, specification_set=specifications, output_directory=workflows_output_directory, workflow_type="find", attrs_includes=attrs_includes, attrs_excludes=attrs_excludes, workflow_name="Find %s in %s" % (specification.entity_name, parent_spec.entity_name), workflow_package=workflow_package, parent_spec=parent_spec)

                   self._write_workflow_files(specification=specification, specification_set=specifications, output_directory=workflows_output_directory, workflow_type="edit", attrs_includes=attrs_includes, attrs_excludes=attrs_excludes, workflow_name="Edit %s" % (specification.entity_name), workflow_package=workflow_package)
                   self._write_workflow_files(specification=specification, specification_set=specifications, output_directory=workflows_output_directory, workflow_type="remove", attrs_includes=attrs_includes, attrs_excludes=attrs_excludes, workflow_name="Remove %s" % (specification.entity_name), workflow_package=workflow_package)

    def _write_session(self, specifications, output_directory, package_name):
        """
        """
        template_file = "o11nplugin-core/session.java.tpl"
        base_name = "Session"
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=output_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   name=self._name,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=package_name,
                   specifications=list(specifications.values()),
                   root_entity=specifications[self.api_root])

    def _write_model(self, specification, specification_set, output_directory, package_name):
        """ Write autogenerate specification file

        """
        template_file = "o11nplugin-core/model.java.tpl"
        filename = "%s%s.java" % (self._class_prefix, specification.entity_name)

        override_content = self._extract_override_content(specification.entity_name)
        superclass_name = "BaseRootObject" if specification.rest_name == self.api_root else "BaseObject"

        defaults = {}
        section = specification.entity_name
        if self.attrs_defaults.has_section(section):
            for attribute in self.attrs_defaults.options(section):
                defaults[attribute] = self.attrs_defaults.get(section, attribute)

        entity_includes = self._get_entity_list_filter(self.inventory_entities, section, "includes")
        entity_excludes = self._get_entity_list_filter(self.inventory_entities, section, "excludes")
        entity_name_attr = "id"
        if self.inventory_entities.has_section(section):
            if self.inventory_entities.has_option(section, "name"):
                entity_name_attr = self.inventory_entities.get(section, "name")

        self.write(destination=output_directory,
                   filename=filename, 
                   template_name=template_file,
                   specification=specification,
                   specification_set=specification_set,
                   version=self.api_version,
                   name=self._name,
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   override_content=override_content,
                   superclass_name=superclass_name,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=package_name,
                   attribute_defaults=defaults,
                   entity_name_attr=entity_name_attr,
                   root_api=self.api_root,
                   entity_includes=entity_includes,
                   entity_excludes=entity_excludes)

        return (filename, specification.entity_name)

    def _write_fetcher(self, specification, specification_set, output_directory, package_name):
        """ Write fetcher

        """
        template_file = "o11nplugin-core/fetcher.java.tpl"
        destination = "%s%s" % (output_directory, self.fetchers_path)
        base_name = "%sFetcher" % specification.entity_name_plural
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=destination,
                   filename=filename,
                   template_name=template_file,
                   specification=specification,
                   specification_set=specification_set,
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   override_content=override_content,
                   header=self.header_content,
                   name=self._name,
                   version_string=self._api_version_string,
                   package_name=package_name)

        return (filename, specification.entity_name_plural)

    def _write_modulebuilder(self, output_directory, package_name):
        """
        """
        template_file = "o11nplugin-core/modulebuilder.java.tpl"
        base_name = "ModuleBuilder"
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=output_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   name=self._name,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=package_name)

    def _write_pluginadaptor(self, output_directory, package_name):
        """
        """
        template_file = "o11nplugin-core/pluginadaptor.java.tpl"
        base_name = "PluginAdaptor"
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=output_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   name=self._name,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=package_name)

    def _write_pluginfactory(self, specifications, output_directory, package_name):
        """
        """
        template_file = "o11nplugin-core/pluginfactory.java.tpl"
        base_name = "PluginFactory"
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=output_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   name=self._name,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=package_name,
                   specification_set=specifications,
                   specifications=list(specifications.values()))

    def _write_constants(self, specifications, output_directory, package_name):
        """
        """
        template_file = "o11nplugin-core/constants.java.tpl"
        base_name = "Constants"
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=output_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   name=self._name,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   product_name=self._product_name,
                   package_name=package_name,
                   specification_set=specifications,
                   specifications=list(specifications.values()))

    def _write_sessionmanager(self, output_directory, package_name):
        """
        """
        template_file = "o11nplugin-core/sessionmanager.java.tpl"
        base_name = "SessionManager"
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=output_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   name=self._name,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=package_name)

    def _write_modelhelper(self, specifications, output_directory, package_name):
        """
        """
        template_file = "o11nplugin-core/modelhelper.java.tpl"
        base_name = "ModelHelper"
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=output_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   name=self._name,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   product_name=self._product_name,
                   package_name=package_name,
                   specification_set=specifications,
                   specifications=list(specifications.values()))

    def _write_action_files(self, specification, attribute, package_name, output_directory):
        """
        """
        action_unique_name = "action-" + specification.entity_name.encode('ascii') + '-get-' + attribute.local_name.encode('ascii')
        action_id = uuid.uuid5(uuid.NAMESPACE_OID, action_unique_name)

        action_directory = "%s/%s" % (output_directory, self._package_subdir)
        if not os.path.exists(action_directory):
            makedirs(action_directory)

        action_name = "get%s%s" %(specification.entity_name, attribute.local_name[0:1].upper() + attribute.local_name[1:])
        self._write_action_file(specification=specification, attribute=attribute, action_directory=action_directory, template_file="o11nplugin-package/get_entity_attribute_action.element_info.xml.tpl", filename="%s.element_info.xml" % (action_name), action_name=action_name, action_id=action_id)
        self._write_action_file(specification=specification, attribute=attribute, action_directory=action_directory, template_file="o11nplugin-package/get_entity_attribute_action.xml.tpl", filename="%s.xml" % (action_name), action_name=action_name, action_id=action_id)

    def _write_action_file(self, specification, attribute, action_directory, template_file, filename, action_name, action_id):
        """
        """
        self.write(destination=action_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._name,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_prefix=self._package_prefix,
                   package_name=self._package_name,
                   specification=specification,
                   attribute=attribute,
                   action_name = action_name,
                   action_id=action_id,
                   workflow_version=self.workflow_version)

    def _write_workflow_files(self, specification, specification_set, output_directory, workflow_type, attrs_includes, attrs_excludes, workflow_name, workflow_package, parent_spec = None):
        """
        """
        workflow_unique_name = specification.entity_name.encode('ascii') + '-' + workflow_type + ('-' + parent_spec.entity_name.encode('ascii') if parent_spec else "")
        workflow_id = uuid.uuid5(uuid.NAMESPACE_OID, workflow_unique_name)

        workflow_directory = "%s/Library/VSPK/Basic/%s" % (output_directory, workflow_package)
        if not os.path.exists(workflow_directory):
            makedirs(workflow_directory)

        self._write_workflow_file(specification=specification, specification_set=specification_set, workflow_directory=workflow_directory, template_file="o11nplugin-package/%s_workflow.element_info.xml.tpl" % (workflow_type), filename="%s.element_info.xml" % (workflow_name), workflow_type=workflow_type, workflow_id=workflow_id, attrs_includes=attrs_includes, attrs_excludes=attrs_excludes, workflow_name=workflow_name, workflow_package=workflow_package, parent_spec=parent_spec)
        self._write_workflow_file(specification=specification, specification_set=specification_set, workflow_directory=workflow_directory, template_file="o11nplugin-package/%s_workflow.xml.tpl" % (workflow_type), filename="%s.xml" % (workflow_name), workflow_type=workflow_type, workflow_id=workflow_id, attrs_includes=attrs_includes, attrs_excludes=attrs_excludes, workflow_name=workflow_name, workflow_package=workflow_package, parent_spec=parent_spec)

    def _write_workflow_file(self, specification, specification_set, workflow_directory, template_file, filename, workflow_type, workflow_id, attrs_includes, attrs_excludes, workflow_name, workflow_package, parent_spec):
        """
        """
        self.write(destination=workflow_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._name,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_prefix=self._package_prefix,
                   package_name=self._package_name,
                   specification=specification,
                   specification_set=specification_set,
                   workflow_type=workflow_type,
                   workflow_id=workflow_id,
                   attrs_includes=attrs_includes,
                   attrs_excludes=attrs_excludes,
                   workflow_name=workflow_name,
                   parent_spec=parent_spec,
                   workflow_version=self.workflow_version,
                   workflow_package=workflow_package)

    def _write_enum(self, specification, attribute, output_directory, package_name):
        """ Write autogenerate specification file

        """
        enum_name = specification.entity_name + attribute.local_name[0:1].upper() + attribute.local_name[1:]
        template_file = "o11nplugin-core/enum.java.tpl"
        destination = "%s%s" % (output_directory, self.enums_path)
        filename = "%s%s.java" % (self._class_prefix, enum_name)

        self.write(destination=destination,
                   filename=filename, 
                   template_name=template_file,
                   header=self.header_content,
                   specification=specification,
                   package_name=package_name,
                   enum_name=enum_name,
                   attribute=attribute)

        return (filename, specification.entity_name)

    def _write_file(self, output_directory, template_file, filename):
        """ 
        """
        self.write(destination=output_directory,
                   filename=filename,
                   template_name=template_file,
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._name,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_prefix=self._package_prefix,
                   package_name=self._package_name,
                   plugin_version=self.plugin_version)

    def _extract_override_content(self, name):
        """
        """
        # find override file
        specific_override_path = "%s/%s_%s%s.override.java" % (self.override_folder, self.api_version, self._class_prefix, name.title())
        generic_override_path = "%s/%s%s.override.java" % (self.override_folder, self._class_prefix, name.title())
        final_path = specific_override_path if os.path.exists(specific_override_path) else generic_override_path

        # Read override from file
        override_content = None
        if os.path.isfile(final_path):
            override_content = open(final_path).read()

        return override_content

    def _get_package_prefix(self, url):
        ""
        ""
        hostname_parts = self._get_hostname_parts(url)

        package_name = ""
        for index, hostname_part in enumerate(reversed(hostname_parts)):
            package_name = package_name + hostname_part
            if index < len(hostname_parts) - 1:
                package_name = package_name + '.'

        return package_name

    def _get_hostname_parts(self, url):
        ""
        ""
        if url.find("http://") != 0:
            url = "http://" + url

        hostname = urlparse(url).hostname
        hostname_parts = hostname.split('.')

        valid_hostname_parts = []
        for hostname_part in hostname_parts:
            if hostname_part != "www":
                valid_hostname_parts.append(hostname_part)

        return valid_hostname_parts

    # Custom version of this method until the main one gets fixed
    def _resolve_parent_apis(self, specifications):
        """
        """
        for specification_rest_name, specification in specifications.items():
            specification.parent_apis[:] = []
            for rest_name, remote_spec in specifications.items():
                for related_child_api in remote_spec.child_apis:
                    if related_child_api.rest_name == specification.rest_name:
                        parent_api = SpecificationAPI(specification=remote_spec)
                        parent_api.rest_name = remote_spec.rest_name
                        if related_child_api.allows_get:
                            parent_api.allows_get = True
                        if related_child_api.allows_create:
                            parent_api.allows_create = True
                        if related_child_api.allows_update:
                            parent_api.allows_update = True
                        if related_child_api.allows_delete:
                            parent_api.allows_Delete = True

                        specification.parent_apis.append(parent_api)

    def _set_local_and_workflow_type(self, specifications):
        ""
        ""
        for rest_name, specification in specifications.items():
            for attribute in specification.attributes:
                if attribute.type == "string":
                    attribute.workflow_type = "string"
                elif attribute.type == "integer":
                    attribute.workflow_type = "number"
                elif attribute.type == "boolean":
                    attribute.workflow_type = "boolean"
                elif attribute.type == "time":
                    attribute.workflow_type = "number"
                elif attribute.type == "float":
                    attribute.workflow_type = "number"
                elif attribute.type == "enum":
                    enum_type = specification.entity_name + attribute.local_name[0:1].upper() + attribute.local_name[1:]
                    attribute.local_type = enum_type
                    attribute.workflow_type = self._name.upper() + ':' + enum_type
                elif attribute.type == "object":
                    attr_type = "Object"
                    if self.attrs_types.has_option(specification.entity_name, attribute.local_name):
                        type = self.attrs_types.get(specification.entity_name, attribute.local_name)
                        if type:
                            attr_type = type
                    attribute.local_type = attr_type
                    attribute.workflow_type = self._name.upper() + ':' + attr_type
                elif attribute.type == "list":
                    if attribute.subtype == "enum":
                        enum_subtype = specification.entity_name + attribute.local_name[0:1].upper() + attribute.local_name[1:]
                        attribute.local_type = "java.util.List<" + enum_subtype + ">"
                        attribute.workflow_type = "Array/" + self._name.upper() + ':' + enum_subtype
                    elif attribute.subtype == "object":
                        attr_subtype = "com.fasterxml.jackson.databind.JsonNode"
                        if self.attrs_types.has_option(specification.entity_name, attribute.local_name):
                            subtype = self.attrs_types.get(specification.entity_name, attribute.local_name)
                            if subtype:
                                attr_subtype = subtype
                        attribute.local_type = "java.util.List<" + attr_subtype + ">"
                        attribute.workflow_type = "Array/" + self._name.upper() + ':' + attr_subtype
                    elif attribute.subtype == "entity":
                        attribute.local_type = "java.util.List<com.fasterxml.jackson.databind.JsonNode>"
                        attribute.workflow_type = "Array/string"
                    else:
                        attribute.local_type = "java.util.List<String>"
                        attribute.workflow_type = "Array/string"

    def _copyfile(self, filename, input_directory, output_directory):
         ""
         ""
         input_file = "%s/%s" % (input_directory, filename)
         if os.path.isfile(input_file):
             output_file = "%s/%s" % (output_directory, filename)
             copyfile(input_file, output_file)

    def _get_entity_list_filter(self, collection, section, tag):
        ""
        ""
        entities = []

        if collection.has_option("all", tag):
            entity_list_str = collection.get("all", tag)
            entities = entities + entity_list_str.split(", ")

        if collection.has_option(section, tag):
            entity_list_str = collection.get(section, tag)
            entities = entities + entity_list_str.split(", ")

        return entities
