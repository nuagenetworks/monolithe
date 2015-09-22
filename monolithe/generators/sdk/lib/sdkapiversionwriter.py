# -*- coding: utf-8 -*-

import os
import shutil

from monolithe.lib import Printer, SDKUtils, TaskManager
from monolithe.generators.lib.writers import TemplateFileWriter


class SDKAPIVersionWriter(object):
    """ Writer of the Python SDK SDK

    """
    COMMON_ATTRIBUTES = ["multicast", "iptype", "maintenancemode", "permittedaction", "connectionstate", "forwardingclasses"]

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None

        self.monolithe_config = monolithe_config
        self._root_api = self.monolithe_config.get_option("root_api")


    def _prepare_attributes(self, model, constants):
        """ Removes attributes and computes constants

        """
        attributes = list()
        for attribute in model.attributes:

            attributes.append(attribute)

            if attribute.allowed_choices and len(attribute.allowed_choices) > 0:

                if attribute.remote_name.lower() not in SDKAPIVersionWriter.COMMON_ATTRIBUTES:
                    name = "%s%s%s" % (model.name, attribute.remote_name[0].upper(), attribute.remote_name[1:])
                else:
                    name = "%s%s" % (attribute.remote_name[0].upper(), attribute.remote_name[1:])

                constants[name] = self._make_constants_value(attribute.allowed_choices)

        model.attributes = attributes

    def _make_constants_value(self, choices):
        """ Create a dictionary for constants

        """
        results = dict()

        for choice in choices:
            results[choice] = choice

        return results

    def write(self, resources, apiversion):
        """ Write all files according to data

            Args:
                resources: A list of all resources to manage
                apiversion: the version of the api

            Returns:
                Writes models and fetchers files

        """
        autogenerate_filenames = dict()
        fetcher_filenames = dict()
        override_filenames = dict()
        constants = dict()

        self.writer = _SDKAPIVersionFileWriter(monolithe_config=self.monolithe_config, apiversion=apiversion)

        task_manager = TaskManager()

        for model in resources:
            self._prepare_attributes(model=model, constants=constants)
            task_manager.start_task(method=self._write_autogenerate_file, model=model, filenames=autogenerate_filenames)
            task_manager.start_task(method=self._write_override_file, model=model, filenames=override_filenames)
            task_manager.start_task(method=self._write_fetcher_file, model=model, filenames=fetcher_filenames)

        task_manager.wait_until_exit()

        self.writer.write_constants_file(constants=constants)
        self.writer.write_session_file()
        self.writer.write_init_autogenerate_files(filenames=autogenerate_filenames)
        self.writer.write_init_fetcher_files(filenames=fetcher_filenames)
        self.writer.write_init_override_files(filenames=override_filenames)
        self.writer.copy_attrs_defaults()

    def _write_autogenerate_file(self, model, filenames):
        """ Write the autogenerate file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        if model.remote_name == self._root_api:
            (filename, classname) = self.writer.write_root_model(model=model)
        else:
            (filename, classname) = self.writer.write_model(model=model)

        filenames[filename] = classname

    def _write_override_file(self, model, filenames):
        """ Write the override file for the model

            Args:
                model: the model to write

        """
        (filename, classname) = self.writer.write_model_override(model=model)

        filenames[filename] = classname

    def _write_fetcher_file(self, model, filenames):
        """ Write the fetcher file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        if model.name != self._root_api:
            (filename, classname) = self.writer.write_fetcher(model=model)
            filenames[filename] = classname


class _SDKAPIVersionFileWriter(TemplateFileWriter):
    """ Provide usefull method to write Python files.

    """
    def __init__(self, monolithe_config, apiversion):
        """ Initializes a _SDKAPIVersionFileWriter

        """
        super(_SDKAPIVersionFileWriter, self).__init__(package="monolithe.generators.sdk")

        self.monolithe_config = monolithe_config
        self._sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._sdk_class_prefix = self.monolithe_config.get_option("sdk_class_prefix", "sdk")
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._root_api = self.monolithe_config.get_option("root_api")

        self.apiversion = apiversion
        self.output_directory = "%s/%s/%s" % (self._sdk_output, self._sdk_name, SDKUtils.get_string_version(apiversion))
        self.override_folder = "%s/../../__overrides" % self.output_directory
        self.autogenerate_path = "/autogenerates/"
        self.fetchers_path = "/fetchers/"

    def _attr_defaults_file(self):
        """
        """
        attrs_defaults_path = "%s/../../__attributes_defaults" % self.output_directory

        if not os.path.exists(attrs_defaults_path):
            return None

        defaults_name = "attrs_defaults.ini"
        specific_defaults_name = "%s_attrs_defaults.ini" % self.apiversion
        target_folder = "%s/resources" % self.output_directory

        specific_defaults_path = "%s/%s" % (attrs_defaults_path, specific_defaults_name)
        if os.path.exists(specific_defaults_path):
            return (specific_defaults_path, "%s/%s" % (target_folder, defaults_name), target_folder)

        general_defaults_path  = "%s/%s" % (attrs_defaults_path, defaults_name)
        if os.path.exists(general_defaults_path):
            return (general_defaults_path, "%s/%s" % (target_folder, defaults_name), target_folder)

    def write_constants_file(self, constants):
        """ Write constants file

            Args:
                constants (dict): dict of constants

        """
        self.write(destination=self.output_directory, filename="constants.py", template_name="constants.py.tpl",
                    constants=constants,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

    def write_init_autogenerate_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = "%s%s" % (self.output_directory, self.autogenerate_path)

        self.write(destination=destination, filename="__init__.py", template_name="__autogenerate_init__.py.tpl",
                    filenames=filenames,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

    def write_init_fetcher_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = "%s%s" % (self.output_directory, self.fetchers_path)
        self.write(destination=destination, filename="__init__.py", template_name="__fetcher_init__.py.tpl",
                    filenames=filenames,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

    def write_init_override_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        self.write(destination=self.output_directory, filename="__init__.py", template_name="__override_init__.py.tpl",
                    filenames=filenames,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

    def write_session_file(self):
        """ Write SDK session file

            Args:
                version (str): the version of the server

        """
        filename = "%s%ssession.py" % (self._sdk_class_prefix.lower(),  self._product_accronym.lower())
        self.write(destination=self.output_directory, filename=filename, template_name="session.py.tpl",
                    version=self.apiversion,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym,
                    root_api=self._root_api)

    def write_model(self, model):
        """ Write autogenerate model file

        """
        destination = "%s%s" % (self.output_directory, self.autogenerate_path)
        filename = "%s%s.py" % (self._sdk_class_prefix.lower(), model.name.lower())

        self.write(destination=destination, filename=filename, template_name="object_autogenerate.py.tpl",
                    model=model,
                    version=self.apiversion,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

        return (filename, model.name)

    def write_root_model(self, model):
        """ Write autogenerate rest user model file

        """
        destination = "%s%s" % (self.output_directory, self.autogenerate_path)
        filename = "%s%s.py" % (self._sdk_class_prefix.lower(), model.name.lower())

        self.write(destination=destination, filename=filename, template_name="root.py.tpl",
                    model=model,
                    version=self.apiversion,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym,
                    root_api=self._root_api)

        return (filename, model.name)

    def write_model_override(self, model):
        """ Write model override

        """
        destination = self.output_directory
        filename = "%s%s.py" % (self._sdk_class_prefix.lower(), model.name.lower())

        # find override file
        specific_override_path = "%s/%s_%s%s.override.py" % (self.override_folder, self.apiversion, self._sdk_class_prefix.lower(), model.name.lower())
        generic_override_path = "%s/%s%s.override.py" % (self.override_folder, self._sdk_class_prefix.lower(), model.name.lower())
        final_path = specific_override_path if os.path.exists(specific_override_path) else generic_override_path

        # Read override from file
        override_content = None
        if os.path.isfile(final_path):
            override_content = open(final_path).read()

        self.write(destination=destination, filename=filename, template_name="object_override.py.tpl",
                    model=model,
                    override_content=override_content,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

        return (filename, model.name)

    def write_fetcher(self, model):
        """ Write fetcher

        """
        destination = "%s%s" % (self.output_directory, self.fetchers_path)
        filename = "%s%s_fetcher.py" % (self._sdk_class_prefix.lower(), model.plural_name.lower())

        self.write(destination=destination, filename=filename, template_name="object_fetcher.py.tpl",
                    model=model,
                    sdk_class_prefix=self._sdk_class_prefix,
                    product_accronym=self._product_accronym)

        return (filename, model.plural_name)

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
