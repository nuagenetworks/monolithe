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
    def __init__(self, monolithe_config, branch="master"):
        """
        """
        self.monolithe_config = monolithe_config
        self.branch = branch
        self.repository_manager = None

        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")

    def run(self, api_url, login_or_token, password, organization, repository, apiversion):
        """ Start the SDK generation

        """
        self.repository_manager = RepositoryManager(monolithe_config=self.monolithe_config,
                                                    api_url=api_url,
                                                    login_or_token=login_or_token,
                                                    password=password,
                                                    organization=organization,
                                                    repository=repository)

        Printer.log("Getting specifications from branch `%s` of repository `%s`" % (self.branch, self.repository_manager.repository))

        specifications = self.repository_manager.get_all_specifications(branch=self.branch)

        self.generate(specifications=specifications, apiversion=apiversion)

    def generate(self, specifications, apiversion):
        """
        """
        Printer.log("Generating %s v%s from %s specifications..." % (self._sdk_name, apiversion, len(specifications)))

        writer = SDKAPIVersionWriter(monolithe_config=self.monolithe_config)
        writer.write(resources=specifications, apiversion=apiversion)

        Printer.success("Done")

