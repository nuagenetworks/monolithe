# -*- coding: utf-8 -*-

import os
import shutil

from jinja2 import Environment, PackageLoader

from monolithe.utils.printer import Printer
from monolithe.utils.constants import Constants
from monolithe.utils.parse import ParsingUtils

from monolithe.lib.managers import TaskManager

__all__ = ['HTMLFileWriter', 'VSDKFileWriter']

RESTUSER = 'RESTUser'
VANILLA_PATH = '%s/../vanilla' % os.path.dirname(os.path.realpath(__file__))


class FileWriter(object):
    """ Writer a file content

    """
    def write(self, destination, filename, content):
        """ Write a file at the specific destination with the content.

            Args:
                destination (string): the destination location
                filename (string): the filename that will be written
                content (string): the content of the filename

        """
        if not os.path.exists(destination):
            try:
                os.makedirs(destination)
            except:  # The directory can be created while creating it.
                pass

        filepath = '%s/%s' % (destination, filename)

        f = open(filepath, 'w+')
        f.write(content)
        f.close()


class TemplateFileWriter(FileWriter):
    """ Write a template file

    """

    def __init__(self, directory):
        """ Initializes a FileWriter

        """
        super(TemplateFileWriter, self).__init__()
        self.env = Environment(loader=PackageLoader('monolithe', 'templates'), extensions=["jinja2.ext.do"])
        self.directory = directory

    def write(self, destination, filename, template_name, **kwargs):
        """ Write a file according to the template name

            Args:
                destination (string): the destination location
                filename (string): the filename that will be written
                template_name (string): the name of the template
                kwargs (dict): all attribute that will be passed to the template
        """
        template = self.env.get_template(template_name)
        content = template.render(kwargs)
        super(TemplateFileWriter, self).write(destination=destination, filename=filename, content=content)


class VSDKFileWriter(TemplateFileWriter):
    """ Provide usefull method to write Python files.
        Will be used by SDKWriter

    """
    AUTOGENERATE_PATH = '/autogenerates/'
    FETCHERS_PATH = '/fetchers/'

    SETUP_TEMPLATE = 'vsdk/setup.py.tpl'
    FETCHER_TEMPLATE = 'vsdk/nuobject_fetcher.py.tpl'
    MODEL_OVERRIDE_TEMPLATE = 'vsdk/nuobject_override.py.tpl'
    MODEL_TEMPLATE = 'vsdk/nuobject_autogenerate.py.tpl'
    RESTUSER_TEMPLATE = 'vsdk/nurestuser.py.tpl'
    CONSTANTS_TEMPLATE = 'vsdk/constants.py.tpl'

    OVERRIDE_PATH = '%s/vsdk/overrides' % VANILLA_PATH

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

        self.write(destination=destination, filename=filename, template_name=VSDKFileWriter.SETUP_TEMPLATE,  apiversion=version, revisionnumber=revision)

    def write_constants_file(self, constants):
        """ Write constants file

            Args:
                constants (dict): dict of constants

        """
        destination = self.directory
        filename = 'constants.py'

        self.write(destination=destination, filename=filename, template_name=VSDKFileWriter.CONSTANTS_TEMPLATE, constants=constants)

    def write_model(self, model):
        """ Write autogenerate model file

        """
        destination = '%s%s' % (self.directory, VSDKFileWriter.AUTOGENERATE_PATH)
        filename = 'nu%s.py' % model.name.lower()

        self.write(destination=destination, filename=filename, template_name=VSDKFileWriter.MODEL_TEMPLATE, model=model)

        return (filename, model.name)

    def write_restuser_model(self, model):
        """ Write autogenerate rest user model file

        """
        destination = '%s%s' % (self.directory, VSDKFileWriter.AUTOGENERATE_PATH)
        filename = 'nu%s.py' % model.name.lower()

        self.write(destination=destination, filename=filename, template_name=VSDKFileWriter.RESTUSER_TEMPLATE, model=model)

        return (filename, model.name)

    def write_model_override(self, model):
        """ Write model override

        """
        destination = self.directory
        filename = 'nu%s.py' % model.name.lower()

        # Read override from file
        override_path = '%s/%s' % (VSDKFileWriter.OVERRIDE_PATH, 'nu%s.override.py' % model.name.lower())
        override_content = None
        if os.path.isfile(override_path):
            override_content = open(override_path).read()

        self.write(destination=destination, filename=filename, template_name=VSDKFileWriter.MODEL_OVERRIDE_TEMPLATE, model=model, override_content=override_content)
        return (filename, model.name)

    def write_fetcher(self, model):
        """ Write fetcher

        """
        destination = '%s%s' % (self.directory, VSDKFileWriter.FETCHERS_PATH)
        filename = 'nu%s_fetcher.py' % model.name.lower()

        self.write(destination=destination, filename=filename, template_name=VSDKFileWriter.FETCHER_TEMPLATE, model=model)

        return (filename, model.name)

    def clean(self, except_files):
        """ Clean folder to remove all files except those generated

            Args:
                except_files: list of generated files to avoid removing
        """
        self._clean_folder(folder=VSDKFileWriter.AUTOGENERATE_PATH, except_files=except_files)
        self._clean_folder(folder=VSDKFileWriter.FETCHERS_PATH, except_files=except_files)
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


class HTMLFileWriter(TemplateFileWriter):
    """ Provides usefull method for generating
        HTML documentation.

        Used by DocWriter

    """
    MODEL_TEMPLATE = 'docs/object.html.tpl'
    INDEX_TEMPLATE = 'docs/index.html.tpl'

    def write_model(self, model):
        """ Write the HTML file for the given model

            Args:
                model: the model to write

        """
        destination = self.directory
        filename = '%s.html' % model.remote_name.lower()

        self.write(destination=destination, filename=filename, template_name=HTMLFileWriter.MODEL_TEMPLATE, model=model)
        return (filename, model.name)

    def write_index(self, packages, models):
        """ Write HTML index to link all filenames

            Args:
                models: dict of all models

        """
        destination = self.directory
        filename = 'index.html'

        self.write(destination=destination, filename=filename, template_name=HTMLFileWriter.INDEX_TEMPLATE, packages=packages, models=models)


class SDKWriter(object):
    """ Writer of the Python VSD SDK

    """
    VSDK_PATH = '/vsdk'
    VANILLA_SRC_PATH = '%s/vsdk/base/' % VANILLA_PATH

    IGNORED_FILES = ['__init__.py', 'nuvsdsession.py', 'utils.py', 'nurestuser.py', 'constants.py']

    GENERAL_CONSTANTS = ['multicast', 'iptype', 'maintenancemode', 'permittedaction', 'connectionstate', 'forwardingclasses']

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        self.writer_directory = '%s%s' % (directory, SDKWriter.VSDK_PATH)

        if not os.path.exists(self.writer_directory):
            Printer.log("Copying default sources...")
            shutil.copytree(SDKWriter.VANILLA_SRC_PATH, directory)

    def _prepare_attributes(self, model, constants):
        """ Removes attributes and computes constants

        """
        attributes = list()
        for attribute in model.attributes:

            attributes.append(attribute)

            if attribute.allowed_choices and len(attribute.allowed_choices) > 0:

                if attribute.remote_name.lower() not in SDKWriter.GENERAL_CONSTANTS:
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
        return {choice: choice for choice in choices}

    def write(self, resources, apiversion, revision):
        """ Write all files according to data

            Args:
                resources: A list of all resources to manage
                apiversion: the version of the api
                revision: the revision number of the api

            Returns:
                Writes models and fetchers files

        """
        filenames = dict()
        constants = dict()

        task_manager = TaskManager()

        for model_name, model in resources.iteritems():
            self._prepare_attributes(model=model, constants=constants)
            task_manager.start_task(method=self._write_autogenerate_file, model=model, filenames=filenames)
            task_manager.start_task(method=self._write_override_file, model=model)
            task_manager.start_task(method=self._write_fetcher_file, model=model, filenames=filenames)

        task_manager.wait_until_exit()
        self._clean_files(except_files=filenames.keys())

        writer = VSDKFileWriter(directory=self.writer_directory)
        writer.write_setup_file(version=apiversion, revision=revision)

        constants = ParsingUtils.order(constants)

        writer.write_constants_file(constants=constants)

        Printer.success('Successfully generated files for %s objects' % len(resources))

    def _write_autogenerate_file(self, model, filenames):
        """ Write the autogenerate file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = VSDKFileWriter(directory=self.writer_directory)

        if model.name != Constants.RESTUSER:
            (filename, classname) = writer.write_model(model=model)
        else:
            (filename, classname) = writer.write_restuser_model(model=model)

        filenames[filename] = classname

    def _write_override_file(self, model):
        """ Write the override file for the model

            Args:
                model: the model to write

        """
        writer = VSDKFileWriter(directory=self.writer_directory)
        writer.write_model_override(model=model)

    def _write_fetcher_file(self, model, filenames):
        """ Write the fetcher file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = VSDKFileWriter(directory=self.writer_directory)

        if model.name != Constants.RESTUSER:
            (filename, classname) = writer.write_fetcher(model=model)
            filenames[filename] = classname

    def _clean_files(self, except_files):
        """ Removes not generated files

            Args:
                except_files: dictionary of filenames to avoid removing

        """

        except_files = list(set(except_files + SDKWriter.IGNORED_FILES))

        writer = VSDKFileWriter(directory=self.writer_directory)
        writer.clean(except_files=except_files)


class DocWriter(object):
    """ Writer of the Python VSD Documentation

    """
    VANILLA_SRC_PATH = '%s/docs/' % VANILLA_PATH

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        self.writer_directory = directory

        if os.path.exists(self.writer_directory):
            shutil.rmtree(self.writer_directory)

        shutil.copytree(DocWriter.VANILLA_SRC_PATH, self.writer_directory)

    def write(self, resources, apiversion):
        """ Write all files according to data

            Args:
                resources: A list of all resources to manage
                apiversion: the version of the api

            Returns:
                Writes all html files into the directory

        """

        filenames = dict()
        task_manager = TaskManager()

        for model_name, model in resources.iteritems():
            task_manager.start_task(method=self._write_model, model=model, filenames=filenames)

        task_manager.wait_until_exit()

        packages = self._extract_packages(resources)

        writer = HTMLFileWriter(directory=self.writer_directory)
        writer.write_index(packages, resources)

        Printer.success('Successfully generated documentation files for %s objects' % len(resources))

    def _write_model(self, model, filenames):
        """ Write the HTML file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        if model.name != RESTUSER:
            writer = HTMLFileWriter(directory=self.writer_directory)
            (filename, classname) = writer.write_model(model=model)
            filenames[filename] = classname

    def _extract_packages(self, models):
        """ Returns a dictionnary containing for each package
            a list of models name

        """
        packages = dict()

        for name, model in models.iteritems():
            package = model.package

            if package is None:
                continue

            if package not in packages:
                packages[package] = list()

            packages[package].append(name)

        return packages
