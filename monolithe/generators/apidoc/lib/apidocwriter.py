# -*- coding: utf-8 -*-

import os
import shutil

from monolithe.lib import TaskManager, Printer
from monolithe.generators.lib.writers import TemplateFileWriter


class APIDocWriter(object):
    """ Writer of the Python SDK Documentation

    """

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None
        self.monolithe_config = monolithe_config
        self._rest_user_api = self.monolithe_config.get_option("rest_user_api")

    def write(self, resources, apiversion):
        """
        """
        filenames = dict()
        task_manager = TaskManager()

        self.writer = APIDocFileWriter(monolithe_config=self.monolithe_config, apiversion=apiversion)

        for model in resources:
            task_manager.start_task(method=self._write_model, model=model, filenames=filenames)

        task_manager.wait_until_exit()

        self.writer.write_index(resources)

    def _write_model(self, model, filenames):
        """
        """
        if model.remote_name != self._rest_user_api:
            (filename, classname) = self.writer.write_model(model=model)
            filenames[filename] = classname


class APIDocFileWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config, apiversion):
        """
        """
        super(APIDocFileWriter, self).__init__(package='monolithe.generators.apidoc')

        self.monolithe_config = monolithe_config
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._apidoc_output = self.monolithe_config.get_option("apidoc_output", "apidoc")
        self._product_name = self.monolithe_config.get_option("product_name")

        self.output_directory = "%s/%s/%s" % (self._apidoc_output, self._sdk_name, apiversion)


    def write_model(self, model):
        """
        """
        filename = '%s.html' % model.remote_name.lower()

        self.write( destination=self.output_directory, filename=filename, template_name="object.html.tpl",
                    model=model,
                    product_name=self._product_name)

        return (filename, model.name)

    def write_index(self, models):
        """
        """
        filename = 'index.html'

        self.write( destination=self.output_directory, filename=filename, template_name="index.html.tpl",
                    models=models,
                    product_name=self._product_name)
