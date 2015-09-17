# -*- coding: utf-8 -*-

import os
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.lib import Printer

from .lib import SDKWriter
from .sdkapiversiongenerator import SDKAPIVersionGenerator
from monolithe.specifications import RepositoryManager


class SDKGenerator(object):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        self.monolithe_config = monolithe_config
        self.sdk_user_vanilla = self.monolithe_config.get_option("sdk_user_vanilla", "sdk")
        self.sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        self.sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")


    def _install_system_vanilla(self):
        """
        """
        if os.path.exists(self.sdk_output):
            shutil.rmtree(self.sdk_output)

        system_vanilla_path = os.path.join(os.path.dirname(__file__), "vanilla");
        shutil.copytree(system_vanilla_path, self.sdk_output)

    def _install_user_vanilla(self):
        """
        """

        if os.path.exists(self.sdk_user_vanilla):
            for item in os.listdir(self.sdk_user_vanilla):
                s = os.path.join(self.sdk_user_vanilla, item)
                d = os.path.join(self.sdk_output, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, False, None)
                else:
                    shutil.copy2(s, d)

        shutil.move('%s/%s' % (self.sdk_output, '__sdk'), '%s/%s' % (self.sdk_output, self.sdk_name))

    def _cleanup(self):
        """
        """
        overrides_path = "%s/__overrides" % self.sdk_output
        attrs_defaults_path = "%s/__attributes_defaults" % self.sdk_output

        if os.path.exists(overrides_path): shutil.rmtree(overrides_path)
        if os.path.exists(attrs_defaults_path): shutil.rmtree(attrs_defaults_path)


    def run(self, api_url, login_or_token, password, organization, repository, apiversions):
        """
        """
        self.generate(api_url=api_url, login_or_token=login_or_token, password=password, organization=organization, repository=repository, apiversions=apiversions)

    def generate(self, specification_info=None, api_url=None, login_or_token=None, password=None, organization=None, repository=None, apiversions=None):
        """
        """
        self._install_system_vanilla()
        self._install_user_vanilla()

        # if specification_info:
        #
        #     apiversions = []
        #
        #     for apiversion, specifications in specification_info.iteritems():
        #
        #         apiversions.append(apiversion)
        #
        #         generator = SDKAPIVersionGenerator(monolithe_config=self.monolithe_config)
        #         generator.generate(specifications=specifications, apiversion=apiversion)
        #
        # elif api_url and login_or_token and password and organization and repository and apiversions:
        for apiversion in apiversions:
            generator = SDKAPIVersionGenerator(monolithe_config=self.monolithe_config)
            generator.run(  api_url=api_url,
                            login_or_token=login_or_token,
                            password=password,
                            organization=organization,
                            repository=repository,
                            apiversion=apiversion)


        sdk_writer = SDKWriter(monolithe_config=self.monolithe_config)
        sdk_writer.write(apiversions=apiversions)

        self._cleanup()