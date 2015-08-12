# -*- coding: utf-8 -*-

import os
import shutil

from monolithe.lib.utils.printer import Printer
from monolithe.lib.utils.constants import Constants
from monolithe.lib.managers import TaskManager
from monolithe.lib.utils.parse import ParsingUtils
from monolithe.generators.lib.writers import TemplateFileWriter


class SDKWriter(object):
    """ Writer of the Python VSD SDK

    """
    IGNORED_FILES = ['__init__.py', 'nuvsdsession.py', 'utils.py', 'nurestuser.py', 'constants.py']
    COMMON_ATTRIBUTES = ['multicast', 'iptype', 'maintenancemode', 'permittedaction', 'connectionstate', 'forwardingclasses']

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        if not os.path.exists(directory):
            Printer.log("Copying default sources...")
            self.writer_directory = directory
            writer = self.get_writer()
            writer.copy_default_files()

        self.writer_directory = '%s/vsdk' % directory

    def get_writer(self):
        """ Get a writer to write content

        """
        return VSDKFileWriter(directory=self.writer_directory)

    def _prepare_attributes(self, model, constants):
        """ Removes attributes and computes constants

        """
        attributes = list()
        for attribute in model.attributes:

            attributes.append(attribute)

            if attribute.allowed_choices and len(attribute.allowed_choices) > 0:

                if attribute.remote_name.lower() not in SDKWriter.COMMON_ATTRIBUTES:
                    name = '%s%s%s' % (model.name, attribute.remote_name[0].upper(), attribute.remote_name[1:])
                else:
                    name = '%s%s' % (attribute.remote_name[0].upper(), attribute.remote_name[1:])

                constants[name] = self._make_constants_value(attribute.allowed_choices)

        # Another specific case... they really love this!
        constants['ProtocolType'] = Constants.PROTOCOL_TYPES

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

        for model_name, model in resources.iteritems():
            self._prepare_attributes(model=model, constants=constants)
            task_manager.start_task(method=self._write_autogenerate_file, model=model, filenames=autogenerate_filenames, version=apiversion)
            task_manager.start_task(method=self._write_override_file, model=model, filenames=override_filenames, version=apiversion)
            task_manager.start_task(method=self._write_fetcher_file, model=model, filenames=fetcher_filenames, version=apiversion)

        task_manager.wait_until_exit()
        except_files = autogenerate_filenames.keys() + fetcher_filenames.keys() + override_filenames.keys()
        self._clean_files(except_files=except_files)

        writer = self.get_writer()
        writer.write_setup_file(version=apiversion, revision=revision)

        # Constants
        constants = ParsingUtils.order(constants)
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

        if model.name != Constants.RESTUSER:
            (filename, classname) = writer.write_model(model=model, version=version)
        else:
            (filename, classname) = writer.write_restuser_model(model=model, version=version)

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

        if model.name != Constants.RESTUSER:
            (filename, classname) = writer.write_fetcher(model=model, version=version)
            filenames[filename] = classname

    def _clean_files(self, except_files):
        """ Removes not generated files

            Args:
                except_files: dictionary of filenames to avoid removing

        """

        except_files = list(set(except_files + SDKWriter.IGNORED_FILES))

        writer = self.get_writer()
        writer.clean(except_files=except_files)


class VSDKFileWriter(TemplateFileWriter):
    """ Provide usefull method to write Python files.

    """
    def __init__(self, directory):
        """ Initializes a VSDKFileWriter

        """
        super(VSDKFileWriter, self).__init__(directory=directory, package=u'monolithe.generators.vspk')

        self._vanilla_path = '%s/../vanilla/vsdk' % os.path.dirname(os.path.realpath(__file__))
        self._override_path = '%s/overrides' % self._vanilla_path

        self._template_folder = 'templates'
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

    def copy_default_files(self):
        """ Copy default sources to the output directory

        """
        shutil.copytree('%s/base' % self._vanilla_path, self.directory)

    def write_setup_file(self, version, revision):
        """ Write setup.py file

            Will generate a setup.py with version set to version-revision

            Args:
                version: version of the package
                revision: number of the revision

            Example:
                setup.py with version 3.0-1

        """
        destination = '%s/../' % self.directory
        filename = 'setup.py'

        self.write(destination=destination, filename=filename, template_name=self._setup_template,  apiversion=version, revisionnumber=revision)

    def write_constants_file(self, constants):
        """ Write constants file

            Args:
                constants (dict): dict of constants

        """
        destination = self.directory
        filename = 'constants.py'

        self.write(destination=destination, filename=filename, template_name=self._constants_template, constants=constants)

    def write_init_autogenerate_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = '%s%s' % (self.directory, self._autogenerate_path)
        filename = '__init__.py'

        self.write(destination=destination, filename=filename, template_name=self._autogenerate_init_template, filenames=filenames)

    def write_init_fetcher_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = '%s%s' % (self.directory, self._fetchers_path)
        filename = '__init__.py'

        self.write(destination=destination, filename=filename, template_name=self._fetcher_init_template, filenames=filenames)

    def write_init_override_files(self, filenames):
        """ Write constants file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = self.directory
        filename = '__init__.py'

        self.write(destination=destination, filename=filename, template_name=self._override_init_template, filenames=filenames)

    def write_vsdsession_file(self, version):
        """ Write VSD session file

            Args:
                version (str): the version of the vsd

        """
        destination = self.directory
        filename = 'nuvsdsession.py'

        self.write(destination=destination, filename=filename, template_name=self._vsdsession_template, version=version)

    def write_model(self, model, version):
        """ Write autogenerate model file

        """
        destination = '%s%s' % (self.directory, self._autogenerate_path)
        filename = 'nu%s.py' % model.name.lower()

        self.write(destination=destination, filename=filename, template_name=self._model_template, model=model, version=version)

        return (filename, model.name)

    def write_restuser_model(self, model, version):
        """ Write autogenerate rest user model file

        """
        destination = '%s%s' % (self.directory, self._autogenerate_path)
        filename = 'nu%s.py' % model.name.lower()

        self.write(destination=destination, filename=filename, template_name=self._restuser_template, model=model, version=version)

        return (filename, model.name)

    def write_model_override(self, model, version):
        """ Write model override

        """
        destination = self.directory
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
        destination = '%s%s' % (self.directory, self._fetchers_path)
        filename = 'nu%s_fetcher.py' % model.name.lower()

        self.write(destination=destination, filename=filename, template_name=self._fetcher_template, model=model, version=version)

        return (filename, model.plural_name)

    def clean(self, except_files):
        """ Clean folder to remove all files except those generated

            Args:
                except_files: list of generated files to avoid removing
        """
        self._clean_folder(folder=self._autogenerate_path, except_files=except_files)
        self._clean_folder(folder=self._fetchers_path, except_files=except_files)
        self._clean_folder(folder='', except_files=except_files)

    def _clean_folder(self, folder, except_files):
        """ Removes all files of directory except when file name
            is in except dictionary

            Args:
                folder: the folder
                except_files: dictionary of filenames to avoid removing

        """
        path = self.directory + folder

        for file in os.listdir(path):
            file_path = os.path.join(path, file)

            try:
                if os.path.isfile(file_path) and file not in except_files:
                    Printer.log("Removing file `%s` with path `%s`" % (file, file_path))
                    os.unlink(file_path)
            except:
                Printer.raiseError("An error has been raised on file %s with path %s" % (file, file_path))
