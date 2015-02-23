# -*- coding: utf-8 -*-

import os
import shutil

from copy import deepcopy
from jinja2 import Environment, PackageLoader

from .printer import Printer
from .managers import TaskManager
from .utils import Utils

__all__ = ['HTMLFileWriter', 'VSDKFileWriter', 'CourgetteWriter']

RESTUSER = 'RESTUser'


class FileWriter(object):
    """ Basic file writer to write a file.

        This object will be inherited to create Python
        and HTML files.

        See below for `VSDKFileWriter` and `HTMLFileWriter`

    """
    def __init__(self, directory):
        """ Initializes a FileWriter

        """
        self.env = Environment(loader=PackageLoader('vsdgenerators', 'templates'), extensions=["jinja2.ext.do"])
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


class CourgetteFileWriter(FileWriter):
    """ Provide usefull method to write Python files.
        Will be used by CourgetteWriter

    """
    GETALL_ENVIRONMENT_TEMPLATE = 'courgette/getall_environment.py.tpl'
    ENVIRONMENT_TEMPLATE = 'courgette/environment.py.tpl'
    ENVIRONMENT_PATH = '/environments'

    TEST_TEMPLATE = 'courgette/tests.py.tpl'
    TEST_PATH = '/tests/functional'

    def write_environment(self, model):
        """ Write Environment

        """
        template = self.env.get_template(CourgetteFileWriter.ENVIRONMENT_TEMPLATE)
        destination = '%s%s' % (self.directory, CourgetteFileWriter.ENVIRONMENT_PATH)
        filename = 'nu%s.py' % model.environment_name.lower()

        self.write(template=template, destination=destination, filename=filename, model=model)

        return (filename, model.name)

    def write_getall_environment(self, model):
        """ Write getall environment

        """
        template = self.env.get_template(CourgetteFileWriter.GETALL_ENVIRONMENT_TEMPLATE)
        destination = '%s%s' % (self.directory, CourgetteFileWriter.ENVIRONMENT_PATH)
        filename = 'nu%s.py' % model.getall_environment_name.lower()

        self.write(template=template, destination=destination, filename=filename, model=model)

        return (filename, model.name)

    def write_test(self, model, allowed_methods):
        """ Write test

        """
        template = self.env.get_template(CourgetteFileWriter.TEST_TEMPLATE)
        destination = '%s%s' % (self.directory, CourgetteFileWriter.TEST_PATH)
        filename = 'nu%s.py' % model.environment_name.lower()

        self.write(template=template, destination=destination, filename=filename, model=model, allowed_methods=allowed_methods)

        return (filename, model.name)

    def _write_file(self, destination, filename, content):
        """ Write filename at the given destination with the given content

            Args:
                destination: the destination where to create the file
                filename: the file name
                content: the content to write

        """
        filepath = '%s/%s' % (destination, filename)

        if not os.path.exists(filepath):
            super(CourgetteFileWriter, self)._write_file(destination, filename, content)


class VSDKFileWriter(FileWriter):
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

    def write_setup_file(self, version, revision):
        """ Write setup.py file

            Will generate a setup.py with version set to version-revision

            Args:
                version: version of the package
                revision: number of the revision

            Example:
                setup.py with version 3.0-1

        """
        template = self.env.get_template(VSDKFileWriter.SETUP_TEMPLATE)
        destination = '%s/../' % self.directory
        filename = 'setup.py'

        self.write(template=template, destination=destination, filename=filename, apiversion=version, revisionnumber=revision)

    def write_model(self, model):
        """ Write autogenerate model file

        """
        template = self.env.get_template(VSDKFileWriter.MODEL_TEMPLATE)

        destination = '%s%s' % (self.directory, VSDKFileWriter.AUTOGENERATE_PATH)
        filename = 'nu%s.py' % model.name.lower()

        self.write(template=template, destination=destination, filename=filename, model=model)

        return (filename, model.name)

    def write_restuser_model(self, model):
        """ Write autogenerate rest user model file

        """

        template = self.env.get_template(VSDKFileWriter.RESTUSER_TEMPLATE)
        destination = '%s%s' % (self.directory, VSDKFileWriter.AUTOGENERATE_PATH)
        filename = 'nu%s.py' % model.name.lower()

        self.write(template=template, destination=destination, filename=filename, model=model)

        return (filename, model.name)

    def write_model_override(self, model):
        """ Write model override

        """
        template = self.env.get_template(VSDKFileWriter.MODEL_OVERRIDE_TEMPLATE)
        destination = self.directory
        filename = 'nu%s.py' % model.name.lower()

        file_path = '%s/%s' % (destination, filename)

        if not os.path.isfile(file_path):
            self.write(template=template, destination=destination, filename=filename, model=model)
            return (filename, model.name)

        return None

    def write_fetcher(self, model):
        """ Write fetcher

        """
        template = self.env.get_template(VSDKFileWriter.FETCHER_TEMPLATE)
        destination = '%s%s' % (self.directory, VSDKFileWriter.FETCHERS_PATH)
        filename = 'nu%s_fetcher.py' % model.name.lower()

        self.write(template=template, destination=destination, filename=filename, model=model)

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


class HTMLFileWriter(FileWriter):
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
        template = self.env.get_template(HTMLFileWriter.MODEL_TEMPLATE)
        destination = self.directory
        filename = '%s.html' % model.name.lower()
        self.write(template=template, destination=destination, filename=filename, model=model)
        return (filename, model.name)

    def write_index(self, packages, models):
        """ Write HTML index to link all filenames

            Args:
                models: dict of all models

        """
        template = self.env.get_template(HTMLFileWriter.INDEX_TEMPLATE)
        destination = self.directory
        filename = 'index.html'

        self.write(template=template, destination=destination, filename=filename, packages=packages, models=models)


class SDKWriter(object):
    """ Writer of the Python VSD SDK

    """
    VSDK_PATH = '/vsdk'
    VANILLA_SRC_PATH = './vanilla/sdk/'

    IGNORED_ATTRIBUTES = ["ID", "externalID", "parentID", "parentType", "owner", "creationDate", "lastUpdatedDate", "lastUpdatedBy", "_fetchers"]
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

    def _remove_ignored_attributes(self, model):
        """ Removes attributes that should be ignored

        """
        model.attributes = [attribute for attribute in model.attributes if attribute.remote_name not in SDKWriter.IGNORED_ATTRIBUTES]

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
            self._remove_ignored_attributes(model)
            task_manager.start_task(method=self._write_autogenerate_file, model=model, filenames=filenames)
            task_manager.start_task(method=self._write_override_file, model=model)
            task_manager.start_task(method=self._write_fetcher_file, model=model, filenames=filenames)

        task_manager.wait_until_exit()
        self._clean_files(except_files=filenames.keys())

        writer = VSDKFileWriter(directory=self.writer_directory)
        writer.write_setup_file(version=apiversion, revision=revision)

        Printer.success('Successfully generated files for %s objects' % len(resources))

    def _write_autogenerate_file(self, model, filenames):
        """ Write the autogenerate file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        writer = VSDKFileWriter(directory=self.writer_directory)

        if model.name != RESTUSER:
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

        if model.name != RESTUSER:
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
    VANILLA_SRC_PATH = './vanilla/docs/'

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


class CourgetteWriter(object):
    """ Writer for courgette

    """
    IGNORED_ATTRIBUTES = ["ID", "externalID", "parentID", "parentType", "owner", "creationDate", "lastUpdatedDate", "lastUpdatedBy", "_fetchers"]

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        self.writer_directory = directory

        if not os.path.exists(self.writer_directory):
            raise Exception('Unknown %s directory' % self.writer_directory)

    def _get_root_objects(self, resources):
        """

        """
        roots = dict()

        for model_name, model in resources.iteritems():

            parent_names = self._get_parent_names(model)
            allowed_methods = self._get_allowed_methods(model)

            if len(parent_names) == 0 and 'POST' in allowed_methods:
                model.parent = 'csproot'
                model.environment_name = model.name
                model.parent_environment_name = None
                roots[model_name] = model

        return roots

    def _traverse_model(self, model, resources, origin=None):
        """ Traverse the current model, and write it!

        """
        self._remove_ignored_attributes(model)
        self._write_environment(model)
        self._write_getall_environment(model)
        self._write_tests(model)

        for relation in model.relations:

            child_remote_name = relation.remote_name
            child_model = self._get_model_from_remote_name(child_remote_name, resources)

            if not self._can_create_child_from_parent(child=child_model, parent=model):
                continue

            child_model.parent = model
            parent_names = self._get_parent_names(child_model)

            if len(parent_names) == 0:
                continue

            elif len(parent_names) == 1:
                child_model.environment_name = '%s%s' % (model.environment_name, child_model.name) if origin else child_model.name
                child_model.parent_environment_name = model.environment_name
                self._traverse_model(model=child_model, resources=resources, origin=origin)

            else:
                m = deepcopy(child_model)
                m.environment_name = '%s%s' % (model.environment_name, m.name) if origin else '%s%s' % (model.name, m.name)
                m.parent_environment_name = model.environment_name
                self._traverse_model(model=m, resources=resources, origin=model)

    def write(self, resources):
        """ Write all environments and tests files for courgette

            Args:
                resources: A list of all resources to manage

            Returns:
                Writes all html files into the directory

        """
        roots = self._get_root_objects(resources)

        for name, model in roots.iteritems():
            self._traverse_model(model, resources)

        Printer.success('Successfully generated tests files for %s objects' % len(resources))

    def _remove_ignored_attributes(self, model):
        """ Removes attributes that should be ignored

        """
        model.attributes = [attribute for attribute in model.attributes if attribute.remote_name not in SDKWriter.IGNORED_ATTRIBUTES]

    def _get_parent_names(self, model):
        """ Get parents remote name of the given model

            Args:
                model: the model

            Returns:
                A list of parent remote names
        """
        names = []
        for api in model.apis:
            for operation in api.operations:
                if operation['method'] == 'POST' and api.parent_remote_name:
                    names.append(api.parent_remote_name)

        return names

    def _can_create_child_from_parent(self, child, parent):
        """ Check if the child can be created from the parent
            model

            Args:
                child: the child
                parent: the parent

            Returns:
                True or False
        """
        if child is None or parent is None:
            return False

        for api in child.apis:
            if api.parent_remote_name == parent.remote_name:
                for operation in api.operations:
                    if operation['method'] == 'POST':
                        return True
        return False

    def _write_environment(self, model):
        """ Write an environment for single model
            and the given parent

            Args:
                model: the model
                parent: the parent

            Returns:
                Nothing yet
        """
        writer = CourgetteFileWriter(directory=self.writer_directory)
        writer.write_environment(model=model)

    def _write_getall_environment(self, model):
        """ Write an environment for a getAll model
            and the given parent

            Args:
                model: the model

            Returns:
                Nothing yet
        """
        model.getall_environment_name = Utils.get_plural_name(model.environment_name)
        writer = CourgetteFileWriter(directory=self.writer_directory)
        writer.write_getall_environment(model=model)

    def _write_tests(self, model):
        """ Write tests for the model
            and the given parent

            Args:
                model: the model

            Returns:
                Nothing yet
        """
        allowed_methods = self._get_allowed_methods(model)

        if 'POST' not in allowed_methods:
            allowed_methods.append('POST')

        writer = CourgetteFileWriter(directory=self.writer_directory)
        writer.write_test(model=model, allowed_methods=allowed_methods)

    # Utilities

    def _get_model_from_remote_name(self, remote_name, models):
        """ Return model with the given remote_name in models

            Args:
                remote_name: the remote name
                models: the list of models

            Returns:
                A model or None
        """
        for name, model in models.iteritems():
            if model.remote_name == remote_name:
                return model

        return None

    def _get_allowed_methods(self, model):
        """ Return a list of allowed HTTP methods for
            the given model

            Args:
                model: the model

            Returns:
                A list of HTTP Methods

        """
        path = '/%s' % model.resource_name
        paths = [path, '%s/{id}' % path]
        return self._get_allowed_methods_for_paths(model, paths)

    def _get_allowed_methods_for_paths(self, model, paths=[]):
        """ Return a list of allowed HTTP methods
            for all paths of the given model

            Args:
                model: the model
                paths: a list of path

            Returns:
                A list of HTTP methods
        """
        methods = []

        for api in model.apis:
            if api.path in paths:
                for operation in api.operations:
                    methods.append(operation['method'])

        return methods
