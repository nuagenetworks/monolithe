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
        self._root_api = self.monolithe_config.get_option("root_api")

    def write(self, specifications, apiversion):
        """
        """
        filenames = dict()
        task_manager = TaskManager()

        self.writer = APIDocFileWriter(monolithe_config=self.monolithe_config, apiversion=apiversion)

        for specification in specifications:
            task_manager.start_task(method=self._write_specification, specification=specification, filenames=filenames)

        task_manager.wait_until_exit()

        self.writer.write_index(specifications)

    def _write_specification(self, specification, filenames):
        """
        """
        if specification.remote_name != self._root_api:
            (filename, classname) = self.writer.write_specification(specification=specification)
            filenames[filename] = classname


class APIDocFileWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config, apiversion):
        """
        """
        super(APIDocFileWriter, self).__init__(package="monolithe.generators.apidoc")

        self.monolithe_config = monolithe_config
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._apidoc_output = self.monolithe_config.get_option("apidoc_output", "apidoc")
        self._product_name = self.monolithe_config.get_option("product_name")

        self.output_directory = "%s/%s/%s" % (self._apidoc_output, self._sdk_name, apiversion)


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
