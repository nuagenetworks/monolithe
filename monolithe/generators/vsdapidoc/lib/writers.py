# -*- coding: utf-8 -*-

import os
import shutil

from monolithe.lib.utils.printer import Printer
from monolithe.lib.utils.constants import Constants
from monolithe.lib.managers import TaskManager
from monolithe.lib.writers import TemplateFileWriter


class APIDocWriter(object):
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

        writer = self.get_writer()
        writer.copy_default_files()

    def get_writer(self):
        """ Get a writer to write content

        """
        return APIDocFileWriter(directory=self.writer_directory)

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

        writer = self.get_writer()
        writer.write_index(packages, resources)

    def _write_model(self, model, filenames):
        """ Write the HTML file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        if model.name != Constants.RESTUSER:
            writer = self.get_writer()
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


class APIDocFileWriter(TemplateFileWriter):
    """ Provides usefull method for generating
        HTML documentation.

        Used by DocWriter

    """

    def __init__(self, directory):
        """ Initializes a VSDKFileWriter

        """
        super(APIDocFileWriter, self).__init__(directory=directory, package='monolithe.generators.vsdapidoc')

        self._vanilla_path = '%s/../vanilla' % os.path.dirname(os.path.realpath(__file__))

        self._template_folder = 'templates'
        self._model_template = 'object.html.tpl'
        self._index_template = 'index.html.tpl'

    def copy_default_files(self):
        """ Copy default sources to the output directory

        """
        shutil.copytree(self._vanilla_path, self.directory)

    def write_model(self, model):
        """ Write the HTML file for the given model

            Args:
                model: the model to write

        """
        destination = self.directory
        filename = '%s.html' % model.remote_name.lower()

        self.write(destination=destination, filename=filename, template_name=self._model_template, model=model)
        return (filename, model.name)

    def write_index(self, packages, models):
        """ Write HTML index to link all filenames

            Args:
                models: dict of all models

        """
        destination = self.directory
        filename = 'index.html'

        self.write(destination=destination, filename=filename, template_name=self._index_template, packages=packages, models=models)
