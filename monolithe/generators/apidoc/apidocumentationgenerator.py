# -*- coding: utf-8 -*-
import os
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import Printer

from monolithe import MonolitheConfig
from monolithe.specifications import RepositoryManager
from monolithe.generators.apidoc.lib import APIDocWriter


class APIDocumentationGenerator(object):
    """ Generate VSD API Documentation

    """
    def __init__(self, apiversions=[]):
        """
        """
        self.apiversions = apiversions
        self.apidoc_output = MonolitheConfig.get_option("apidoc_output", "apidoc")
        self.apidoc_user_vanilla = MonolitheConfig.get_option("apidoc_user_vanilla", "apidoc")

    def _install_system_vanilla(self, apiversion):
        """
        """
        apidocversion_output = "%s/%s" % (self.apidoc_output, apiversion)

        if os.path.exists(apidocversion_output):
            shutil.rmtree(apidocversion_output)

        system_vanilla_path = os.path.join(os.path.dirname(__file__), "vanilla");
        shutil.copytree(system_vanilla_path, apidocversion_output)

    def _install_user_vanilla(self, apiversion):
        """
        """
        if not os.path.exists(self.apidoc_user_vanilla):
            return

        apidocversion_output = "%s/%s" % (self.apidoc_output, apiversion)

        for item in os.listdir(self.apidoc_user_vanilla):
            s = os.path.join(self.apidoc_user_vanilla, item)
            d = os.path.join("%s/%s" % (apidocversion_output, item))
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)

    def run(self, api_url, login_or_token, password, organization, repository):
        """
        """

        self.repository_manager = RepositoryManager(api_url=api_url,
                                                    login_or_token=login_or_token,
                                                    password=password,
                                                    organization=organization,
                                                    repository=repository)
        for apiversion in self.apiversions:
            Printer.log("Getting specifications from branch `%s` of repository `%s`" % (apiversion, self.repository_manager.repository))
            specifications = self.repository_manager.get_all_specifications(branch=apiversion)
            self.generate(specifications, apiversion)


    def generate(self, specifications, apiversion):
        """ Start generation ofthe API Documentation

        """
        Printer.log("Generating API documentation from branch `%s` of repository `%s`" % (apiversion, self.repository_manager.repository))

        self._install_system_vanilla(apiversion=apiversion)
        self._install_user_vanilla(apiversion=apiversion)

        directory = '%s/%s' % (self.apidoc_output, apiversion)
        APIDocWriter(directory=directory).write(resources=specifications, apiversion=apiversion)

        Printer.success("Generated %s documentation files for API version %s" % (len(specifications), apiversion))
