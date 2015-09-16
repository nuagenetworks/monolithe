# -*- coding: utf-8 -*-

import os
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import Printer, SDKUtils, TaskManager
from monolithe.generators.lib.writers import TemplateFileWriter


class SDKAPIVersionWriter(object):
    """ Writer of the Python VSD SDK

    """
    IGNORED_FILES = ['__init__.py', 'nuvsdsession.py', 'utils.py', 'nurestuser.py', 'constants.py']
    COMMON_ATTRIBUTES = ['multicast', 'iptype', 'maintenancemode', 'permittedaction', 'connectionstate', 'forwardingclasses']

    def __init__(self, directory, apiversion):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        self.writer_directory = directory
        self.apiversion = apiversion

        shutil.copytree("%s/__sdk_api_version__" % directory, "%s/%s" % (directory, SDKUtils.get_string_version(self.apiversion)))

    def get_writer(self):
        """ Get a writer to write content

        """
        return _SDKAPIVersionFileWriter(directory=self.writer_directory, apiversion=self.apiversion)

    def _prepare_attributes(self, model, constants):
        """ Removes attributes and computes constants

        """
        attributes = list()
        for attribute in model.attributes:

            attributes.append(attribute)

            if attribute.allowed_choices and len(attribute.allowed_choices) > 0:

                if attribute.remote_name.lower() not in SDKAPIVersionWriter.COMMON_ATTRIBUTES:
                    name = '%s%s%s' % (model.name, attribute.remote_name[0].upper(), attribute.remote_name[1:])
                else:
                    name = '%s%s' % (attribute.remote_name[0].upper(), attribute.remote_name[1:])

                constants[name] = self._make_constants_value(attribute.allowed_choices)

        model.attributes = attributes

    def _make_constants_value(self, choices):
        """ Create a dictionary for constants

        """
        results = dict()

        for choice in choices:
            results[choice] = choice

        return results

    def write(self, resources, apiversion, revision):
        """ Write all files according to data

            Args:
                resources: A list of all resources to manage
                apiversion: the version of the api
                revision: the revision number of the api

            Returns:
                Writes models and fetchers files

        """

        autogenerate_filenames = dict()
        fetcher_filenames = dict()
        override_filenames = dict()
        constants = dict()

        task_manager = TaskManager()

        for model in resources:
            self._prepare_attributes(model=model, constants=constants)
            task_manager.start_task(method=self._write_autogenerate_file, model=model, filenames=autogenerate_filenames, version=apiversion)
            task_manager.start_task(method=self._write_override_file, model=model, filenames=override_filenames, version=apiversion)
            task_manager.start_task(method=self._write_fetcher_file, model=model, filenames=fetcher_filenames, version=apiversion)

        task_manager.wait_until_exit()

        writer = self.get_writer()

        writer.write_constants_file(constants=constants)

        # VSD Session
        writer.write_vsdsession_file(version=apiversion)

        writer.write_init_autogenerate_files(filenames=autogenerate_filenames)
        writer.write_init_fetcher_files(filenames=fetcher_filenames)
        writer.write_init_override_files(filenames=override_filenames)

    def _write_autogenerate_file(self, model, filenames, version):
        """ Write the autogenerate file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = self.get_writer()

        if model.remote_name == MonolitheConfig.get_option('rest_user_api'):
            (filename, classname) = writer.write_restuser_model(model=model, version=version)
        else:
            (filename, classname) = writer.write_model(model=model, version=version)

        filenames[filename] = classname

    def _write_override_file(self, model, filenames, version):
        """ Write the override file for the model

            Args:
                model: the model to write

        """
        writer = self.get_writer()
        (filename, classname) = writer.write_model_override(model=model, version=version)

        filenames[filename] = classname

    def _write_fetcher_file(self, model, filenames, version):
        """ Write the fetcher file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = self.get_writer()

        if model.name != MonolitheConfig.get_option('rest_user_api'):
            (filename, classname) = writer.write_fetcher(model=model, version=version)
            filenames[filename] = classname


class _SDKAPIVersionFileWriter(TemplateFileWriter):
    """ Provide usefull method to write Python files.

    """
    def __init__(self, directory, apiversion):
        """ Initializes a _SDKAPIVersionFileWriter

        """
        self._final_path = '%s/%s' % (directory, SDKUtils.get_string_version(apiversion))

        super(_SDKAPIVersionFileWriter, self).__init__(directory=self._final_path, package=u'monolithe.generators.sdk')

        self._vanilla_path = '%s/__sdk_api_version__' % directory
        self._override_path = '%s/___overrides__' % directory

        self._autogenerate_path = '/autogenerates/'
        self._fetchers_path = '/fetchers/'
        self._setup_template = 'setup.py.tpl'
        self._fetcher_template = 'nuobject_fetcher.py.tpl'
        self._model_override_template = 'nuobject_override.py.tpl'
        self._model_template = 'nuobject_autogenerate.py.tpl'
        self._restuser_template = 'nurestuser.py.tpl'
        self._constants_template = 'constants.py.tpl'
        self._vsdsession_template = 'nuvsdsession.py.tpl'
        self._autogenerate_init_template = '__autogenerate_init__.py.tpl'
        self._fetcher_init_template = '__fetcher_init__.py.tpl'
        self._override_init_template = '__override_init__.py.tpl'

    def write_constants_file(self, constants):
        """ Write constants file

            Args:
                constants (dict): dict of constants

        """
        destination = self._final_path
        filename = 'constants.py'

        self.write(destination=destination, filename=filename, template_name=self._constants_template, constants=constants)

    def write_init_autogenerate_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = '%s%s' % (self._final_path, self._autogenerate_path)
        filename = '__init__.py'

        self.write(destination=destination, filename=filename, template_name=self._autogenerate_init_template, filenames=filenames)

    def write_init_fetcher_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = '%s%s' % (self._final_path, self._fetchers_path)
        filename = '__init__.py'

        self.write(destination=destination, filename=filename, template_name=self._fetcher_init_template, filenames=filenames)

    def write_init_override_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = self._final_path
        filename = '__init__.py'

        self.write(destination=destination, filename=filename, template_name=self._override_init_template, filenames=filenames)

    def write_vsdsession_file(self, version):
        """ Write VSD session file

            Args:
                version (str): the version of the vsd

        """
        destination = self._final_path
        filename = 'nuvsdsession.py'

        self.write(destination=destination, filename=filename, template_name=self._vsdsession_template, version=version)

    def write_model(self, model, version):
        """ Write autogenerate model file

        """
        destination = '%s%s' % (self._final_path, self._autogenerate_path)
        filename = 'nu%s.py' % model.name.lower()

        self.write(destination=destination, filename=filename, template_name=self._model_template, model=model, version=version)

        return (filename, model.name)

    def write_restuser_model(self, model, version):
        """ Write autogenerate rest user model file

        """
        destination = '%s%s' % (self._final_path, self._autogenerate_path)
        filename = 'nu%s.py' % model.name.lower()

        self.write(destination=destination, filename=filename, template_name=self._restuser_template, model=model, version=version)

        return (filename, model.name)

    def write_model_override(self, model, version):
        """ Write model override

        """
        destination = self._final_path
        filename = 'nu%s.py' % model.name.lower()

        # Read override from file
        override_path = '%s/%s' % (self._override_path, 'nu%s.override.py' % model.name.lower())
        override_content = None
        if os.path.isfile(override_path):
            override_content = open(override_path).read()

        self.write(destination=destination, filename=filename, template_name=self._model_override_template, model=model, override_content=override_content)
        return (filename, model.name)

    def write_fetcher(self, model, version):
        """ Write fetcher

        """
        destination = '%s%s' % (self._final_path, self._fetchers_path)
        filename = 'nu%s_fetcher.py' % model.plural_name.lower()

        self.write(destination=destination, filename=filename, template_name=self._fetcher_template, model=model, version=version)

        return (filename, model.plural_name)

