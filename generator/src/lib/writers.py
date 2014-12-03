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
VSDK_PATH = '/vsdk'


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

        self._write_model_file(model=model, template=template, destination=destination, filename=filename)

        return (filename, model['name'])

    def write_fetcher(self, model):
        """ Write fetcher

        """
        template = self.env.get_template('nuobject_fetcher.tpl')
        destination = '%s%s' % (self.directory, FETCHERS_PATH)
        filename = 'nu%s_fetcher.py' % model['name'].lower()

        self._write_model_file(model=model, template=template, destination=destination, filename=filename)

        return (filename, model['name'])

    def write_model_override(self, model):
        """ Write model override

        """
        template = self.env.get_template('nuobject_override.tpl')
        destination = self.directory
        filename = 'nu%s.py' % model['name'].lower()

        file_path = '%s/%s' % (destination, filename)

        if not os.path.isfile(file_path):
            self._write_model_file(model=model, template=template, destination=destination, filename=filename)
            return (filename, model['name'])

        return None

    def write_html_for_model(self, model):
        """ Write the HTML file for the given model

            Args:
                model: the model to write

        """
        template = self.env.get_template('object.html.tpl')
        destination = self.directory
        filename = '%s.html' % model['plural_name'].lower()

        self._write_model_file(model=model, template=template, destination=destination, filename=filename)
        return (filename, model['name'])

    def write_index_html(self, filenames):
        """ Write HTML index to link all filenames

            Args:
                filenames: dict of filename -> object

        """
        template = self.env.get_template('index.html.tpl')
        destination = self.directory
        filename = 'index.html'

        content = template.render(filenames=filenames)
        self._write_file(destination=destination, filename=filename, content=content)

    def _write_model_file(self, model, template, destination, filename):
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

    # TODO-CS: This one should not be here!
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
    """ Writer of the Python VSD SDK

    """

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """

        self.writer_directory = '%s%s' % (directory, VSDK_PATH)

        if not os.path.exists(self.writer_directory):
            Printer.log("Copying default sources...")
            shutil.copytree(VANILLA_SRC_PATH, directory)

    def _clean_files(self, except_files):
        """ Removes unused files

            Args:
                except_files: dictionary of filenames to avoid removing

        """
        writer = FileWriter(directory=self.writer_directory)

        writer.clean_folder(folder=AUTOGENERATE_PATH, except_files=except_files)
        writer.clean_folder(folder=FETCHERS_PATH, except_files=except_files)
        writer.clean_folder(folder='', except_files=except_files)

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

        task_manager = TaskManager()

        for model_name, model in resources.iteritems():
            task_manager.start_task(method=self._write_autogenerate_file, model=model, filenames=filenames)
            task_manager.start_task(method=self._write_override_file, model=model)
            task_manager.start_task(method=self._write_fetcher_file, model=model, filenames=filenames)

        task_manager.wait_until_exit()
        self._clean_files(except_files=filenames)

        writer = FileWriter(directory=self.writer_directory)
        writer.write_setup(version=apiversion, revision=revision)

        Printer.success('Successfully generated files for %s objects' % len(resources))

    def _write_autogenerate_file(self, model, filenames):
        """ Write the autogenerate file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = FileWriter(directory=self.writer_directory)
        (filename, classname) = writer.write_model(model=model)

        filenames[filename] = classname

    def _write_override_file(self, model):
        """ Write the override file for the model

            Args:
                model: the model to write

        """
        writer = FileWriter(directory=self.writer_directory)
        writer.write_model_override(model=model)

    def _write_fetcher_file(self, model, filenames):
        """ Write the fetcher file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = FileWriter(directory=self.writer_directory)
        (filename, classname) = writer.write_fetcher(model=model)

        filenames[filename] = classname


class DocWriter(object):
    """ Writer of the Python VSD Documentation

    """

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        self.writer_directory = directory

        if os.path.exists(self.writer_directory):
            shutil.rmtree(self.writer_directory)

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
            task_manager.start_task(method=self._write_html_for_model, model=model, filenames=filenames)

        task_manager.wait_until_exit()

        writer = FileWriter(directory=self.writer_directory)
        writer.write_index_html(filenames)

        Printer.success('Successfully generated documentation files for %s objects' % len(resources))

    def _write_html_for_model(self, model, filenames):
        """ Write the HTML file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = FileWriter(directory=self.writer_directory)
        (filename, classname) = writer.write_html_for_model(model=model)

        filenames[filename] = classname
