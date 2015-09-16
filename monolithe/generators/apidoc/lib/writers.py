# -*- coding: utf-8 -*-

import os
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import Printer
from monolithe.lib import TaskManager
from monolithe.generators.lib.writers import TemplateFileWriter


class APIDocWriter(object):
    """ Writer of the Python VSD Documentation

    """

    def __init__(self, directory):
        """ Initializes a writer to the specific directory

            Args:
                directory: directory where to copy sources

        """
        self.writer_directory = directory

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

        for model in resources:
            task_manager.start_task(method=self._write_model, model=model, filenames=filenames)

        task_manager.wait_until_exit()

        writer = self.get_writer()
        writer.write_index(resources)

    def _write_model(self, model, filenames):
        """ Write the HTML file for the model

            Args:
                model: the model to write
                filenames: list of generates filenames

        """
        if model.remote_name != MonolitheConfig.get_option('rest_user_api'):
            writer = self.get_writer()
            (filename, classname) = writer.write_model(model=model)
            filenames[filename] = classname


class APIDocFileWriter(TemplateFileWriter):
    """ Provides usefull method for generating
        HTML documentation.

        Used by DocWriter

    """

    def __init__(self, directory):
        """ Initializes a APIDocFileWriter

        """
        super(APIDocFileWriter, self).__init__(directory=directory, package='monolithe.generators.apidoc')

    def write_model(self, model):
        """ Write the HTML file for the given model

            Args:
                model: the model to write

        """
        destination = self.directory
        filename = '%s.html' % model.remote_name.lower()

        self.write( destination=destination, filename=filename, template_name="object.html.tpl",
                    model=model,
                    product_name=MonolitheConfig.get_option("product_name"))

        return (filename, model.name)

    def write_index(self, models):
        """ Write HTML index to link all filenames

            Args:
                models: dict of all models

        """
        destination = self.directory
        filename = 'index.html'

        self.write( destination=destination, filename=filename, template_name="index.html.tpl",
                    models=models,
                    product_name=MonolitheConfig.get_option("product_name"))
