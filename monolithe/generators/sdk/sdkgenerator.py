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

    def run(self, api_url, login_or_token, password, organization, repository):
        """
        """
        self.generate(api_url, login_or_token, password, organization, repository)

    def generate(self, api_url, login_or_token, password, organization, repository):
        """
        """

        if os.path.exists(self.codegen_directory):
            shutil.rmtree(self.codegen_directory)

        shutil.copytree(self.sdk_vanilla_path, self.codegen_directory)
        shutil.move('%s/%s' % (self.codegen_directory, '__sdk_name__'), '%s/%s' % (self.codegen_directory, self.sdk_name))

        for apiversion in self.apiversions:

            if apiversion == 'master':
                Printer.warn('master branch should be used for development purpose only.')

            generator = SDKAPIVersionGenerator(apiversion=apiversion)

            generator.run(api_url, login_or_token, password, organization, repository)

        sdk_writer = SDKWriter(self.codegen_directory, self.apiversions)
        sdk_writer.write()

        shutil.rmtree("%s/%s/__sdk_api_version__" % (self.codegen_directory, self.sdk_name))
        shutil.rmtree("%s/%s/__overrides__" % (self.codegen_directory, self.sdk_name))
