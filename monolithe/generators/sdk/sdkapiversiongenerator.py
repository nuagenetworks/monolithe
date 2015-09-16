# -*- coding: utf-8 -*-

import os
import sys
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import Printer
from monolithe.specifications import RepositoryManager
from monolithe.generators.sdk.lib import SDKAPIVersionWriter

RepositoryManager


class SDKAPIVersionGenerator(object):
    """ Generate SDK

    """
    def __init__(self, apiversion=u'master'):
        """
        """
        self.sdk_name = MonolitheConfig.get_option("sdk_name")
        self.codegen_directory = MonolitheConfig.get_option("codegen_directory")
        self.sdk_vanilla_path = MonolitheConfig.get_option("sdk_vanilla_path")
        self.apiversion = apiversion
        self.repository_manager = None

    def run(self, api_url, login_or_token, password, organization, repository):
        """ Start the SDK generation

        """
        self.repository_manager = RepositoryManager(api_url=api_url,
                                                    login_or_token=login_or_token,
                                                    password=password,
                                                    organization=organization,
                                                    repository=repository)
        Printer.log("Getting specifications from branch `%s` of repository `%s`" % (self.apiversion, self.repository_manager.repository))

        specifications = self.repository_manager.get_all_specifications(branch=self.apiversion)

        self.generate(specifications)

    def generate(self, specifications):
        """
        """
        Printer.log("Starting %s generation for %s files" % (self.sdk_name, len(specifications)))
        writer = SDKAPIVersionWriter(directory="%s/%s" % (self.codegen_directory, self.sdk_name), apiversion=self.apiversion)
        writer.write(resources=specifications, apiversion=self.apiversion, revision=1)
        Printer.success("Generated %s with %s objects for API version %s" % (self.sdk_name, len(specifications), self.apiversion))

