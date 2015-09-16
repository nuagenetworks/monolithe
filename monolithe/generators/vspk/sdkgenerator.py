# -*- coding: utf-8 -*-

import os
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.lib import Printer

from .sdkapiversiongenerator import SDKAPIVersionGenerator

class SDKGenerator(object):
    """ Create a VSPK Package containing SDK versions

    """
    def __init__(self, sdk_name, codegen_directory, sdk_vanilla_path, sdk_api_output_path, apiversions):
        """ Initialize a SDKGenerator

        """
        self.sdk_name = sdk_name
        self.codegen_directory = codegen_directory
        self.sdk_vanilla_path = sdk_vanilla_path
        self.sdk_api_output_path = sdk_api_output_path
        self.apiversions = apiversions

    def run(self, api_url, login_or_token, password, organization, repository):
        """ Create the VSPK package

        """
        self.generate(api_url, login_or_token, password, organization, repository)

    def generate(self, api_url, login_or_token, password, organization, repository):
        """
        """

        if os.path.exists(self.codegen_directory):
            shutil.rmtree(self.codegen_directory)

        shutil.copytree(self.sdk_vanilla_path, self.codegen_directory)

        for apiversion in self.apiversions:

            if apiversion == 'master':
                Printer.warn('master branch should be used for development purpose only.')

            generator = SDKAPIVersionGenerator( sdk_name=self.sdk_name,
                                                codegen_directory=self.codegen_directory,
                                                sdk_vanilla_path=self.sdk_vanilla_path,
                                                sdk_api_output_path=self.sdk_api_output_path,
                                                apiversion=apiversion)

            generator.run(api_url, login_or_token, password, organization, repository)


        shutil.rmtree("%s/%s/__base__" % (self.codegen_directory, self.sdk_api_output_path))
