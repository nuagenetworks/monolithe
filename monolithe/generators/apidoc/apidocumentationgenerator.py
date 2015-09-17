# -*- coding: utf-8 -*-
import os
import shutil

from monolithe.lib import Printer
from monolithe.specifications import RepositoryManager
from monolithe.generators.apidoc.lib import APIDocWriter


class APIDocumentationGenerator(object):
    """ Generate VSD API Documentation

    """
    def __init__(self, monolithe_config):
        """
        """
        self.monolithe_config = monolithe_config
        self._apidoc_output = self.monolithe_config.get_option("apidoc_output", "apidoc")
        self._apidoc_user_vanilla = self.monolithe_config.get_option("apidoc_user_vanilla", "apidoc")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")

    def _install_system_vanilla(self, apiversion):
        """
        """
        apidocversion_output = "%s/%s/%s" % (self._apidoc_output, self._sdk_name, apiversion)

        if os.path.exists(apidocversion_output):
            shutil.rmtree(apidocversion_output)

        system_vanilla_path = os.path.join(os.path.dirname(__file__), "vanilla");
        shutil.copytree(system_vanilla_path, apidocversion_output)

    def _install_user_vanilla(self, apiversion):
        """
        """
        if not os.path.exists(self._apidoc_user_vanilla):
            return

        apidocversion_output = "%s/%s/%s" % (self._apidoc_output, self._sdk_name, apiversion)

        for item in os.listdir(self._apidoc_user_vanilla):
            s = os.path.join(self._apidoc_user_vanilla, item)
            d = os.path.join("%s/%s" % (apidocversion_output, item))
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)

    def run(self, api_url, login_or_token, password, organization, repository, apiversions):
        """
        """

        self.repository_manager = RepositoryManager(monolithe_config=self.monolithe_config,
                                                    api_url=api_url,
                                                    login_or_token=login_or_token,
                                                    password=password,
                                                    organization=organization,
                                                    repository=repository)
        for apiversion in apiversions:
            Printer.log("Getting specifications from branch `%s` of repository `%s`" % (apiversion, self.repository_manager.repository))
            specifications = self.repository_manager.get_all_specifications(branch=apiversion)
            self.generate(specifications, apiversion)


    def generate(self, specifications, apiversion):
        """ Start generation ofthe API Documentation

        """
        Printer.log("Generating API documentation from branch `%s` of repository `%s`" % (apiversion, self.repository_manager.repository))

        self._install_system_vanilla(apiversion=apiversion)
        self._install_user_vanilla(apiversion=apiversion)

        directory = '%s/%s' % (self._apidoc_output, apiversion)

        writer = APIDocWriter(self.monolithe_config)
        writer.write(resources=specifications, apiversion=apiversion)

        Printer.success("Generated %s documentation files for API version %s" % (len(specifications), apiversion))
