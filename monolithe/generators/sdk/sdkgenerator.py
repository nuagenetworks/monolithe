# -*- coding: utf-8 -*-

import os
import shutil
import sys

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.lib import Printer
from monolithe.generators.lib import Generator
from .lib import SDKWriter
from .sdkapiversiongenerator import SDKAPIVersionGenerator


class SDKGenerator(Generator):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        super(SDKGenerator, self).__init__(monolithe_config=monolithe_config)

        self._sdk_user_vanilla = self.monolithe_config.get_option("sdk_user_vanilla", "sdk")
        self._sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")

    def cleanup(self):
        """
        """
        overrides_path = "%s/__overrides" % self._sdk_output
        if os.path.exists(overrides_path):
            shutil.rmtree(overrides_path)

        attrs_defaults_path = "%s/__attributes_defaults" % self._sdk_output
        if os.path.exists(attrs_defaults_path):
            shutil.rmtree(attrs_defaults_path)

    def generate(self, specification_info):
        """
        """
        self.install_system_vanilla(current_file=__file__, output_path=self._sdk_output)
        self.install_user_vanilla(user_vanilla_path=self._sdk_user_vanilla, output_path=self._sdk_output)

        generator = SDKAPIVersionGenerator(monolithe_config=self.monolithe_config)
        apiversions = []

        for apiversion, specifications in specification_info.iteritems():
            Printer.log("generating %s package for api version: %s" % (self._sdk_name, apiversion))
            apiversions.append(apiversion)
            generator.generate(specification_info=specification_info, apiversion=apiversion)

        Printer.log("assembling all packages...")
        sdk_writer = SDKWriter(monolithe_config=self.monolithe_config)
        sdk_writer.write(apiversions=apiversions)

        self.cleanup()

        Printer.success("%s generation complete and available at \"%s\"" % (self._sdk_name, self._sdk_output))