# -*- coding: utf-8 -*-

import os
import shutil

from jinja2 import Environment, PackageLoader
from printer import Printer
from managers import TaskManager

IGNORED_ATTRIBUTES = ["ID", "externalID", "parentID", "parentType", "owner", "creationDate", "lastUpdatedDate", "lastUpdatedBy", "_fetchers"]
IGNORED_RESOURCES = ['EventLog']
IGNORED_FILES = ['__init__.py', 'nuvsdsession.py', 'utils.py', 'nurestuser.py', 'constants.py']

AUTOGENERATE_PATH = '/autogenerates/'
FETCHERS_PATH = '/fetchers/'
VANILLA_SRC_PATH = '../vanilla/'
VSDK_PATH = '/vsdk/'


class FileWriter(object):
    """ Writer to write a file """

    def __init__(self, directory):
        """ Initializes a FileWriter

        """
        self.env = Environment(loader=PackageLoader('src', 'templates'))
        self.directory = directory

    def write_setup(self, version, revision):
        """ Write setup.py file

            Will generate a setup.py with version set to version-revision

            Args:
                version: version of the package
                revision: number of the revision

            Example:
                setup.py with version 3.0-1

        """
        template = self.env.get_template('setup.tpl')
        destination = '%s/../' % self.directory
        filename = 'setup.py'

        content = template.render(apiversion=version, revisionnumber=revision)
        self._write_file(destination=destination, filename=filename, content=content)

    def write_model(self, model):
        """ Write model

        """
        template = self.env.get_template('nuobject_autogenerate.tpl')
        destination = '%s%s' % (self.directory, AUTOGENERATE_PATH)
        filename = 'nu%s.py' % model['name'].lower()

        self._write(model=model, template=template, destination=destination, filename=filename)

        return (filename, model['name'])

    def write_fetcher(self, model):
        """ Write fetcher

        """
        template = self.env.get_template('nuobject_fetcher.tpl')
        destination = '%s%s' % (self.directory, FETCHERS_PATH)
        filename = 'nu%s_fetcher.py' % model['name'].lower()

        self._write(model=model, template=template, destination=destination, filename=filename)

        return (filename, model['name'])

    def write_model_override(self, model):
        """ Write model override

        """
        template = self.env.get_template('nuobject_override.tpl')
        destination = self.directory
        filename = 'nu%s.py' % model['name'].lower()

        if not os.path.isfile(destination+filename):
            self._write(model=model, template=template, destination=destination, filename=filename)
            return (filename, model['name'])

        return None

    def _write(self, model, template, destination, filename):
        """ Write the model according to the template of the writer

        """
        if not os.path.exists(destination):
            try:
                os.makedirs(destination)
            except:  # The directory can be created while creating it.
                pass

        content = template.render(model=model)
        self._write_file(destination=destination, filename=filename, content=content)

    def _write_file(self, destination, filename, content):
        """ Write filename at the given destination with the given content

            Args:
                destination: the destination where to create the file
                filename: the file name
                content: the content to write

        """
        filepath = '%s/%s' % (destination, filename)

        f = open(filepath, 'w+')
        f.write(content)
        f.close()

    def clean_folder(self, folder, except_files):
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
                if os.path.isfile(file_path) and file not in except_files and file not in IGNORED_FILES:
                    Printer.log("Removing file `%s` with path `%s`" % (file, file_path))
                    os.unlink(file_path)
            except:
                Printer.raiseError("An error has been raised on file %s with path %s" % (file, file_path))

class SDKWriter(object):
    """ Writer of the Python VSD SDK """

    @classmethod
    def copy_sources(self, directory):
        """ Copy default sources

            Args:
                directory: directory where to copy sources

        """
        if os.path.exists(directory):
            shutil.rmtree(directory)

        shutil.copytree(VANILLA_SRC_PATH, directory)

    @classmethod
    def _clean_files(self, directory, except_files):
        """ Removes unused files

            Args:
                except_files: dictionary of filenames to avoid removing

        """
        writer = FileWriter(directory=directory)

        writer.clean_folder(folder=AUTOGENERATE_PATH, except_files=except_files)
        writer.clean_folder(folder=FETCHERS_PATH, except_files=except_files)
        writer.clean_folder(folder='', except_files=except_files)

    @classmethod
    def write_sdk(cls, resources, directory, sdkversion):
        """ Update all files according to data

            Args:
                resources: A list of all resources to manage
                directory: the path where to write

            Returns:
                Writes models and fetchers files

        """

        directory = directory + VSDK_PATH
        filenames = dict()

        task_manager = TaskManager()

        for model_name, model in resources.iteritems():
            task_manager.start_task(method=cls._write_autogenerate_file, model=model, directory=directory, filenames=filenames)
            task_manager.start_task(method=cls._write_override_file, model=model, directory=directory)
            task_manager.start_task(method=cls._write_fetcher_file, model=model, directory=directory, filenames=filenames)

        task_manager.wait_until_exit()
        cls._clean_files(directory=directory, except_files=filenames)

        writer = FileWriter(directory=directory)
        writer.write_setup(version=sdkversion["apiversion"], revision=sdkversion['revisionnumber'])

        Printer.success('Successfully generated files for %s objects' % len(resources))

    @classmethod
    def _write_autogenerate_file(cls, model, directory, filenames):
        """ Write the autogenerate file for the model

            Args:
                model: the model to write
                directory: the path to the destination
                filenames: list of generates filenames

        """
        writer = FileWriter(directory=directory)
        (filename, classname) = writer.write_model(model=model)

        filenames[filename] = classname

    @classmethod
    def _write_override_file(cls, model, directory):
        """ Write the override file for the model

            Args:
                model: the model to write
                directory: the path to the destination

        """
        writer = FileWriter(directory=directory)
        writer.write_model_override(model=model)

    @classmethod
    def _write_fetcher_file(cls, model, directory, filenames):
        """ Write the fetcher file for the model

            Args:
                model: the model to write
                directory: the path to the destination
                filenames: list of generates filenames

        """
        writer = FileWriter(directory=directory)
        (filename, classname) = writer.write_fetcher(model=model)

        filenames[filename] = classname
