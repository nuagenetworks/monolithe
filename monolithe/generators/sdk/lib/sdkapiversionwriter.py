# -*- coding: utf-8 -*-

import os
import shutil

from monolithe.lib import Printer, SDKUtils, TaskManager
from monolithe.generators.lib import TemplateFileWriter


class SDKAPIVersionWriter(object):
    """ Writer of the Python SDK SDK

    """
    COMMON_ATTRIBUTES = ["multicast", "iptype", "maintenancemode", "permittedaction", "connectionstate", "forwardingclasses"]

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None

        self.monolithe_config = monolithe_config


    def _prepare_constants(self, specification, constants):
        """ Removes attributes and computes constants

        """
        attributes = list()
        for attribute in specification.attributes:

            attributes.append(attribute)

            if attribute.allowed_choices and len(attribute.allowed_choices) > 0:

                if attribute.remote_name.lower() not in SDKAPIVersionWriter.COMMON_ATTRIBUTES:
                    name = "%s%s%s" % (specification.name, attribute.remote_name[0].upper(), attribute.remote_name[1:])
                else:
                    name = "%s%s" % (attribute.remote_name[0].upper(), attribute.remote_name[1:])

                constants[name] = self._make_constants_value(attribute.allowed_choices)

    def _make_constants_value(self, choices):
        """ Create a dictionary for constants

        """
        results = dict()

        for choice in choices:
            results[choice] = choice

        return results

    def write(self, specifications, api_info):
        """ Write all files according to data

            Args:
                specifications: A list of all specifications to manage
                api_info: the version of the api

            Returns:
                Writes specifications and fetchers files

        """
        autogenerate_filenames = dict()
        fetcher_filenames = dict()
        override_filenames = dict()
        constants = dict()

        self.api_info = api_info

        self.writer = _SDKAPIVersionFileWriter(monolithe_config=self.monolithe_config, api_info=self.api_info)

        task_manager = TaskManager()

        for specification in specifications:
            self._prepare_constants(specification=specification, constants=constants)
            task_manager.start_task(method=self._write_autogenerate_file, specification=specification, filenames=autogenerate_filenames)
            task_manager.start_task(method=self._write_override_file, specification=specification, filenames=override_filenames)
            task_manager.start_task(method=self._write_fetcher_file, specification=specification, filenames=fetcher_filenames)

        task_manager.wait_until_exit()

        self.writer.write_constants(constants=constants)
        self.writer.write_session()
        self.writer.write_init_autogenerates(filenames=autogenerate_filenames)
        self.writer.write_init_fetchers(filenames=fetcher_filenames)
        self.writer.write_init_overrides(filenames=override_filenames)
        self.writer.copy_attrs_defaults()

    def _write_autogenerate_file(self, specification, filenames):
        """ Write the autogenerate file for the specification

            Args:
                specification: the specification to write
                filenames: list of generates filenames

        """
        if specification.remote_name == self.api_info["root"]:
            (filename, classname) = self.writer.write_root_specification(specification=specification)
        else:
            (filename, classname) = self.writer.write_specification(specification=specification)

        filenames[filename] = classname

    def _write_override_file(self, specification, filenames):
        """ Write the override file for the specification

            Args:
                specification: the specification to write

        """
        (filename, classname) = self.writer.write_specification_override(specification=specification)

        filenames[filename] = classname

    def _write_fetcher_file(self, specification, filenames):
        """ Write the fetcher file for the specification

            Args:
                specification: the specification to write
                filenames: list of generates filenames

        """
        if specification.name != self.api_info["root"]:
            (filename, classname) = self.writer.write_fetcher(specification=specification)
            filenames[filename] = classname


class _SDKAPIVersionFileWriter(TemplateFileWriter):
    """ Provide usefull method to write Python files.

    """
    def __init__(self, monolithe_config, api_info):
        """ Initializes a _SDKAPIVersionFileWriter

        """
        super(_SDKAPIVersionFileWriter, self).__init__(package="monolithe.generators.sdk")

        self.api_version = api_info["version"]
        self.api_root = api_info["root"]
        self.api_prefix = api_info["prefix"]

        self.monolithe_config = monolithe_config
        self._sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._sdk_class_prefix = self.monolithe_config.get_option("sdk_class_prefix", "sdk")
        self._product_accronym = self.monolithe_config.get_option("product_accronym")

        self.output_directory = "%s/%s/%s" % (self._sdk_output, self._sdk_name, SDKUtils.get_string_version(self.api_version))
        self.override_folder = os.path.normpath("%s/../../__overrides" % self.output_directory)
        self.autogenerate_path = "/autogenerates/"
        self.fetchers_path = "/fetchers/"

    def _attr_defaults_file(self):
        """
        """
        attrs_defaults_path = "%s/../../__attributes_defaults" % self.output_directory

        if not os.path.exists(attrs_defaults_path):
            return None

        defaults_name = "attrs_defaults.ini"
        specific_defaults_name = "%s_attrs_defaults.ini" % self.api_version
        target_folder = "%s/resources" % self.output_directory

        specific_defaults_path = "%s/%s" % (attrs_defaults_path, specific_defaults_name)
        if os.path.exists(specific_defaults_path):
            return (specific_defaults_path, "%s/%s" % (target_folder, defaults_name), target_folder)

        general_defaults_path  = "%s/%s" % (attrs_defaults_path, defaults_name)
        if os.path.exists(general_defaults_path):
            return (general_defaults_path, "%s/%s" % (target_folder, defaults_name), target_folder)

    def write_constants(self, constants):
        """ Write constants file

            Args:
                constants (dict): dict of constants

        """
        self.write(destination=self.output_directory, filename="constants.py", template_name="constants.py.tpl",
                    constants=constants,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

    def write_init_autogenerates(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = "%s%s" % (self.output_directory, self.autogenerate_path)

        self.write(destination=destination, filename="__init__.py", template_name="__autogenerate_init__.py.tpl",
                    filenames=filenames,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

    def write_init_fetchers(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = "%s%s" % (self.output_directory, self.fetchers_path)
        self.write(destination=destination, filename="__init__.py", template_name="__fetcher_init__.py.tpl",
                    filenames=filenames,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

    def write_init_overrides(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        self.write(destination=self.output_directory, filename="__init__.py", template_name="__override_init__.py.tpl",
                    filenames=filenames,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

    def write_session(self):
        """ Write SDK session file

            Args:
                version (str): the version of the server

        """
        filename = "%s%ssession.py" % (self._sdk_class_prefix.lower(),  self._product_accronym.lower())
        self.write(destination=self.output_directory, filename=filename, template_name="session.py.tpl",
                    version=self.api_version,
                    product_accronym=self._product_accronym,
                    sdk_class_prefix=self._sdk_class_prefix,
                    sdk_root_api=self.api_root,
                    sdk_api_prefix=self.api_prefix)

    def write_specification(self, specification):
        """ Write autogenerate specification file

        """
        destination = "%s%s" % (self.output_directory, self.autogenerate_path)
        filename = "%s%s.py" % (self._sdk_class_prefix.lower(), specification.name.lower())

        self.write(destination=destination, filename=filename, template_name="object_autogenerate.py.tpl",
                    specification=specification,
                    version=self.api_version,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

        return (filename, specification.name)

    def write_root_specification(self, specification):
        """ Write autogenerate rest user specification file

        """
        destination = "%s%s" % (self.output_directory, self.autogenerate_path)
        filename = "%s%s.py" % (self._sdk_class_prefix.lower(), specification.name.lower())

        self.write(destination=destination, filename=filename, template_name="object_root.py.tpl",
                    specification=specification,
                    version=self.api_version,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym,
                    sdk_root_api=self.api_root)

        return (filename, specification.name)

    def write_specification_override(self, specification):
        """ Write specification override

        """
        destination = self.output_directory
        filename = "%s%s.py" % (self._sdk_class_prefix.lower(), specification.name.lower())

        # find override file
        specific_override_path = "%s/%s_%s%s.override.py" % (self.override_folder, self.api_version, self._sdk_class_prefix.lower(), specification.name.lower())
        generic_override_path = "%s/%s%s.override.py" % (self.override_folder, self._sdk_class_prefix.lower(), specification.name.lower())
        final_path = specific_override_path if os.path.exists(specific_override_path) else generic_override_path

        # Read override from file
        override_content = None
        if os.path.isfile(final_path):
            override_content = open(final_path).read()

        self.write(destination=destination, filename=filename, template_name="object_override.py.tpl",
                    specification=specification,
                    override_content=override_content,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

        return (filename, specification.name)

    def write_fetcher(self, specification):
        """ Write fetcher

        """
        destination = "%s%s" % (self.output_directory, self.fetchers_path)
        filename = "%s%s_fetcher.py" % (self._sdk_class_prefix.lower(), specification.plural_name.lower())

        self.write(destination=destination, filename=filename, template_name="object_fetcher.py.tpl",
                    specification=specification,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

        return (filename, specification.plural_name)


    def copy_attrs_defaults(self):
        """
        """
        attributes_file = self._attr_defaults_file()

        if not attributes_file:
            return

        src, dst, target = attributes_file

        if not os.path.exists(target):
            os.makedirs(target)

        shutil.copyfile(src, dst)
