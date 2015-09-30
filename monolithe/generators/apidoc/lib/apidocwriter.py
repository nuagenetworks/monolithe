# -*- coding: utf-8 -*-

import os
import shutil

from monolithe.lib import TaskManager, Printer
from monolithe.generators.lib import TemplateFileWriter


class APIDocWriter(object):
    """ Writer of the Python SDK Documentation

    """

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None
        self.monolithe_config = monolithe_config

    def write(self, specifications, api_info):
        """
        """
        filenames = dict()
        task_manager = TaskManager()

        self.api_info = api_info
        self.writer = APIDocFileWriter(monolithe_config=self.monolithe_config, api_info=self.api_info)

        for specification in specifications:
            task_manager.start_task(method=self._write_specification, specification=specification, filenames=filenames)

        task_manager.wait_until_exit()

        self.writer.write_index(specifications)

    def _write_specification(self, specification, filenames):
        """
        """
        if specification.remote_name != self.api_info:
            (filename, classname) = self.writer.write_specification(specification=specification)
            filenames[filename] = classname


class APIDocFileWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config, api_info):
        """
        """
        super(APIDocFileWriter, self).__init__(package="monolithe.generators.apidoc")

        self.monolithe_config = monolithe_config
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._apidoc_output = self.monolithe_config.get_option("apidoc_output", "apidoc")
        self._product_name = self.monolithe_config.get_option("product_name")

        self.output_directory = "%s/%s/%s" % (self._apidoc_output, self._sdk_name, api_info["version"])


    def write_specification(self, specification):
        """
        """
        filename = "%s.html" % specification.remote_name.lower()

        self.write( destination=self.output_directory, filename=filename, template_name="object.html.tpl",
                    specification=specification,
                    product_name=self._product_name)

        return (filename, specification.name)

    def write_index(self, specifications):
        """
        """

        self.write( destination=self.output_directory, filename="index.html", template_name="index.html.tpl",
                    specifications=specifications,
                    product_name=self._product_name)
