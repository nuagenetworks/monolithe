# -*- coding: utf-8 -*-

import os
import shutil
import sys

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.lib import Printer

from .lib import SDKWriter
from .sdkapiversiongenerator import SDKAPIVersionGenerator
from monolithe.specifications import RepositoryManager, FolderManager


class SDKGenerator(object):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        self.monolithe_config = monolithe_config
        self._sdk_user_vanilla = self.monolithe_config.get_option("sdk_user_vanilla", "sdk")
        self._sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")


    def _install_system_vanilla(self):
        """
        """
        if os.path.exists(self._sdk_output):
            shutil.rmtree(self._sdk_output)

        system_vanilla_path = os.path.join(os.path.dirname(__file__), "vanilla");
        shutil.copytree(system_vanilla_path, self._sdk_output)

    def _install_user_vanilla(self):
        """
        """
        if self._sdk_user_vanilla:
            if os.path.exists(self._sdk_user_vanilla):
                for item in os.listdir(self._sdk_user_vanilla):
                    s = os.path.join(self._sdk_user_vanilla, item)
                    d = os.path.join(self._sdk_output, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d, False, None)
                    else:
                        shutil.copy2(s, d)
            else:
                self._cleanup()
                Printer.raiseError("Could not find user vanilla folder at path %s" % self._sdk_user_vanilla)

        shutil.move("%s/%s" % (self._sdk_output, "__sdk"), "%s/%s" % (self._sdk_output, self._sdk_name))

    def _cleanup(self):
        """
        """
        overrides_path = "%s/__overrides" % self._sdk_output
        attrs_defaults_path = "%s/__attributes_defaults" % self._sdk_output

        if os.path.exists(overrides_path): shutil.rmtree(overrides_path)
        if os.path.exists(attrs_defaults_path): shutil.rmtree(attrs_defaults_path)

    def generate_from_folder(self, folder):
        """
        """
        specification_info = {}

        Printer.log("retrieving specifications from folder \"%s\"" % (folder))
        self.folder_manager = FolderManager(folder=folder, monolithe_config=self.monolithe_config)
        apiversion = self.folder_manager.get_api_version()
        specification_info[apiversion] = self.folder_manager.get_all_specifications()
        Printer.log("%d specifications retrieved from folder \"%s\" (api version: %s)" % (len(specification_info[apiversion]), folder, apiversion))

        self.generate(specification_info=specification_info)

    def generate_from_repo(self, api_url, login_or_token, password, organization, repository, branches):
        """
        """
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

        self.generate(specification_info=specification_info)

    def generate(self, specification_info):
        """
        """
        self._install_system_vanilla()
        self._install_user_vanilla()

        generator = SDKAPIVersionGenerator(monolithe_config=self.monolithe_config)
        apiversions = []

        for apiversion, specifications in specification_info.iteritems():
            Printer.log("generating %s package for api version: %s" % (self._sdk_name, apiversion))
            apiversions.append(apiversion)
            generator.generate(specification_info=specification_info, apiversion=apiversion)

        Printer.log("assembling all packages...")
        sdk_writer = SDKWriter(monolithe_config=self.monolithe_config)
        sdk_writer.write(apiversions=apiversions)

        self._cleanup()

        Printer.success("%s generation complete and available at \"%s\"" % (self._sdk_name, self._sdk_output))