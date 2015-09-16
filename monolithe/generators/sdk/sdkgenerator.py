# -*- coding: utf-8 -*-

import os
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.lib import Printer

from .lib import SDKWriter
from .sdkapiversiongenerator import SDKAPIVersionGenerator


class SDKGenerator(object):
    """ Create a SDK Package containing SDK versions

    """
    def __init__(self, apiversions):
        """
        """
        self.sdk_name = MonolitheConfig.get_option("sdk_name")
        self.codegen_directory = MonolitheConfig.get_option("codegen_directory")
        self.sdk_vanilla_path = MonolitheConfig.get_option("sdk_vanilla_path")
        self.apiversions = apiversions

    def _install_static(self):
        """
        """
        if os.path.exists(self.codegen_directory):
            shutil.rmtree(self.codegen_directory)

        static_sdk_path = os.path.join(os.path.dirname(__file__), 'static');
        shutil.copytree(static_sdk_path, self.codegen_directory)

    def _install_vanilla(self):
        """
        """
        for item in os.listdir(self.sdk_vanilla_path):
            s = os.path.join(self.sdk_vanilla_path, item)
            d = os.path.join(self.codegen_directory, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)

        shutil.move('%s/%s' % (self.codegen_directory, '__sdk'), '%s/%s' % (self.codegen_directory, self.sdk_name))

    def run(self, api_url, login_or_token, password, organization, repository):
        """
        """
        self.generate(api_url, login_or_token, password, organization, repository)

    def generate(self, api_url, login_or_token, password, organization, repository):
        """
        """

        self._install_static()
        self._install_vanilla()

        for apiversion in self.apiversions:

            if apiversion == 'master':
                Printer.warn('master branch should be used for development purpose only.')

            generator = SDKAPIVersionGenerator(apiversion=apiversion)

            generator.run(api_url, login_or_token, password, organization, repository)

        sdk_writer = SDKWriter(self.codegen_directory, self.apiversions)
        sdk_writer.write()

        shutil.rmtree("%s/%s/__sdkapiversion" % (self.codegen_directory, self.sdk_name))
        shutil.rmtree("%s/__overrides" % self.codegen_directory)
