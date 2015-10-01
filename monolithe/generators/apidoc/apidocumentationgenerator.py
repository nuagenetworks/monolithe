# -*- coding: utf-8 -*-
import os
import shutil

from monolithe.lib import Printer
from monolithe.specifications import RepositoryManager, FolderManager
from monolithe.generators.lib import Generator
from .lib import APIDocWriter


class APIDocumentationGenerator(Generator):
    """ Generate SDK API Documentation

    """
    def __init__(self, monolithe_config):
        """
        """
        super(APIDocumentationGenerator, self).__init__(monolithe_config=monolithe_config)

        self._apidoc_output = self.monolithe_config.get_option("apidoc_output", "apidoc")
        self._apidoc_user_vanilla = self.monolithe_config.get_option("apidoc_user_vanilla", "apidoc")
        self._sdk_name = self.monolithe_config.get_option("product_name")
        self._product_name = self.monolithe_config.get_option("product_name")

    def generate(self, specification_info):
        """ Start generation ofthe API Documentation

        """
        writer = APIDocWriter(self.monolithe_config)
        apiversions = []

        for info in specification_info:

            vanilla_output_path = "%s/%s/%s" % (self._apidoc_output, self._sdk_name, info["api"]["version"])

            self.install_system_vanilla(current_file=__file__, output_path=vanilla_output_path)
            self.install_user_vanilla(user_vanilla_path=self._apidoc_user_vanilla, output_path=vanilla_output_path)

            Printer.log("generating %s api documentation for api version: %s" % (self._product_name, info["api"]["version"]))
            writer.write(specifications=info["specifications"], api_info=info["api"])

        Printer.success("%s api documentation generation complete and available at \"%s\"" % (self._product_name, self._apidoc_output))
