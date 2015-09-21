# -*- coding: utf-8 -*-
import os
import shutil

from monolithe.lib import Printer
from monolithe.specifications import RepositoryManager
from monolithe.generators.apidoc.lib import APIDocWriter


class APIDocumentationGenerator(object):
    """ Generate SDK API Documentation

    """
    def __init__(self, monolithe_config):
        """
        """
        self.monolithe_config = monolithe_config
        self._apidoc_output = self.monolithe_config.get_option("apidoc_output", "apidoc")
        self._apidoc_user_vanilla = self.monolithe_config.get_option("apidoc_user_vanilla", "apidoc")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._product_name = self.monolithe_config.get_option("product_name")

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

    def generate(self, specification_info=None, api_url=None, login_or_token=None, password=None, organization=None, repository=None, branches=None):
        """ Start generation ofthe API Documentation

        """
        writer = APIDocWriter(self.monolithe_config)
        apiversions = []

        if not specification_info:

            specification_info = {}

            self.repository_manager = RepositoryManager(monolithe_config=self.monolithe_config,
                                                        api_url=api_url,
                                                        login_or_token=login_or_token,
                                                        password=password,
                                                        organization=organization,
                                                        repository=repository)


            for branch in branches:
                Printer.log("retrieving specifications from github \"%s/%s@%s\"" % (organization.lower(), repository.lower(), branch))
                apiversion = self.repository_manager.get_api_version(branch=branch)
                specifications = self.repository_manager.get_all_specifications(branch=branch)
                specification_info[apiversion] = specifications
                Printer.log("%d specifications retrieved from branch \"%s\" (api version: %s)" % (len(specifications), branch, apiversion))

        for apiversion, specifications in specification_info.iteritems():
            self._install_system_vanilla(apiversion=apiversion)
            self._install_user_vanilla(apiversion=apiversion)
            Printer.log("generating %s api documentation for api version: %s" % (self._product_name, apiversion))
            writer.write(resources=specifications, apiversion=apiversion)

        Printer.success("%s api documentation generation complete and available at \"%s\"" % (self._product_name, self._apidoc_output))
