# -*- coding: utf-8 -*-

import os
import shutil

from jinja2 import Environment, PackageLoader
from printer import Printer
from managers import TaskManager

__all__ = ['HTMLFileWriter', 'PythonFileWriter']


class FileWriter(object):
    """ Basic file writer to write a file.

        This object will be inherited to create Python
        and HTML files.

        See below for `PythonFileWriter` and `HTMLFileWriter`

    """
    def __init__(self, directory):
        """ Initializes a FileWriter

        """
        self.env = Environment(loader=PackageLoader('src', 'templates'), extensions=["jinja2.ext.do"])
        self.directory = directory

    def write(self, template, destination, filename, **kwargs):
        """ Write the model according to the template of the writer

            template: the Jinja template object
            destination: the path to the destination folder
            filename: the filename to create
            kwargs: data that will be transmitted to the template

        """
        if not os.path.exists(destination):
            try:
                os.makedirs(destination)
            except:  # The directory can be created while creating it.
                pass

        content = template.render(kwargs)
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


class PythonFileWriter(FileWriter):
    """ Provide usefull method to write Python files.
        Will be used by SDKWriter

    """
    AUTOGENERATE_PATH = '/autogenerates/'
    FETCHERS_PATH = '/fetchers/'

    SETUP_TEMPLATE = 'setup.py.tpl'
    FETCHER_TEMPLATE = 'nuobject_fetcher.py.tpl'
    MODEL_OVERRIDE_TEMPLATE = 'nuobject_override.py.tpl'
    MODEL_TEMPLATE = 'nuobject_autogenerate.py.tpl'

    def write_setup_file(self, version, revision):
        """ Write setup.py file

            Will generate a setup.py with version set to version-revision

            Args:
                version: version of the package
                revision: number of the revision

            Example:
                setup.py with version 3.0-1

        """
        template = self.env.get_template(PythonFileWriter.SETUP_TEMPLATE)
        destination = '%s/../' % self.directory
        filename = 'setup.py'

        self.write(template=template, destination=destination, filename=filename, apiversion=version, revisionnumber=revision)

    def write_model(self, model):
        """ Write autogenerate model file

        """
        template = self.env.get_template(PythonFileWriter.MODEL_TEMPLATE)
        destination = '%s%s' % (self.directory, PythonFileWriter.AUTOGENERATE_PATH)
        filename = 'nu%s.py' % model['name'].lower()

        self.write(template=template, destination=destination, filename=filename, model=model)

        return (filename, model['name'])

    def write_model_override(self, model):
        """ Write model override

        """
        template = self.env.get_template(PythonFileWriter.MODEL_OVERRIDE_TEMPLATE)
        destination = self.directory
        filename = 'nu%s.py' % model['name'].lower()

        file_path = '%s/%s' % (destination, filename)

        if not os.path.isfile(file_path):
            self.write(template=template, destination=destination, filename=filename, model=model)
            return (filename, model['name'])

        return None

    def write_fetcher(self, model):
        """ Write fetcher

        """
        template = self.env.get_template(PythonFileWriter.FETCHER_TEMPLATE)
        destination = '%s%s' % (self.directory, PythonFileWriter.FETCHERS_PATH)
        filename = 'nu%s_fetcher.py' % model['name'].lower()

        self.write(template=template, destination=destination, filename=filename, model=model)

        return (filename, model['name'])

    def clean(self, except_files):
        """ Clean folder to remove all files except those generated

            Args:
                except_files: list of generated files to avoid removing
        """
        self._clean_folder(folder=PythonFileWriter.AUTOGENERATE_PATH, except_files=except_files)
        self._clean_folder(folder=PythonFileWriter.FETCHERS_PATH, except_files=except_files)
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


class HTMLFileWriter(FileWriter):
    """ Provides usefull method for generating
        HTML documentation.

        Used by DocWriter

    """
    MODEL_TEMPLATE = 'object.html.tpl'
    INDEX_TEMPLATE = 'index.html.tpl'

    def write_model(self, model):
        """ Write the HTML file for the given model

            Args:
                model: the model to write

        """
        template = self.env.get_template(HTMLFileWriter.MODEL_TEMPLATE)
        destination = self.directory
        filename = '%s.html' % model['name'].lower()
        from pprint import pprint
        pprint(model)
        self.write(template=template, destination=destination, filename=filename, model=model)
        return (filename, model['name'])

    def write_index(self, filenames):
        """ Write HTML index to link all filenames

            Args:
                filenames: dict of filename -> object

        """
        template = self.env.get_template(HTMLFileWriter.INDEX_TEMPLATE)
        destination = self.directory
        filename = 'index.html'

        self.write(template=template, destination=destination, filename=filename, filenames=filenames)


class SDKWriter(object):
    """ Writer of the Python VSD SDK

    """
    VSDK_PATH = '/vsdk'
    VANILLA_SRC_PATH = '../vanilla/sdk/'

    IGNORED_ATTRIBUTES = ["ID", "externalID", "parentID", "parentType", "owner", "creationDate", "lastUpdatedDate", "lastUpdatedBy", "_fetchers"]
    IGNORED_RESOURCES = ['EventLog']
    IGNORED_FILES = ['__init__.py', 'nuvsdsession.py', 'utils.py', 'nurestuser.py', 'constants.py']

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        self.writer_directory = '%s%s' % (directory, SDKWriter.VSDK_PATH)

        if not os.path.exists(self.writer_directory):
            Printer.log("Copying default sources...")
            shutil.copytree(SDKWriter.VANILLA_SRC_PATH, directory)

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
        self._clean_files(except_files=filenames.keys())

        writer = PythonFileWriter(directory=self.writer_directory)
        writer.write_setup_file(version=apiversion, revision=revision)

        Printer.success('Successfully generated files for %s objects' % len(resources))

    def _write_autogenerate_file(self, model, filenames):
        """ Write the autogenerate file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = PythonFileWriter(directory=self.writer_directory)
        (filename, classname) = writer.write_model(model=model)

        filenames[filename] = classname

    def _write_override_file(self, model):
        """ Write the override file for the model

            Args:
                model: the model to write

        """
        writer = PythonFileWriter(directory=self.writer_directory)
        writer.write_model_override(model=model)

    def _write_fetcher_file(self, model, filenames):
        """ Write the fetcher file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = PythonFileWriter(directory=self.writer_directory)
        (filename, classname) = writer.write_fetcher(model=model)

        filenames[filename] = classname

    def _clean_files(self, except_files):
        """ Removes not generated files

            Args:
                except_files: dictionary of filenames to avoid removing

        """

        except_files = list(set(except_files + SDKWriter.IGNORED_FILES))

        writer = PythonFileWriter(directory=self.writer_directory)
        writer.clean(except_files=except_files)


class DocWriter(object):
    """ Writer of the Python VSD Documentation

    """
    VANILLA_SRC_PATH = '../vanilla/docs/'

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        self.writer_directory = directory

        if os.path.exists(self.writer_directory):
            shutil.rmtree(self.writer_directory)

        shutil.copytree(DocWriter.VANILLA_SRC_PATH, self.writer_directory)

        # raise Exception(directory)

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

        writer = HTMLFileWriter(directory=self.writer_directory)
        writer.write_index(filenames)

        Printer.success('Successfully generated documentation files for %s objects' % len(resources))

    def _write_model(self, model, filenames):
        """ Write the HTML file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = HTMLFileWriter(directory=self.writer_directory)
        (filename, classname) = writer.write_model(model=model)

        filenames[filename] = classname
