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
        self.sdk_name = MonolitheConfig.get_option("sdk_name", "sdk")
        self.sdk_output = MonolitheConfig.get_option("sdk_output", "sdk")
        self.sdk_user_vanilla = MonolitheConfig.get_option("sdk_user_vanilla", "sdk")
        self.apiversions = apiversions

    def _install_static(self):
        """
        """
        if os.path.exists(self.sdk_output):
            shutil.rmtree(self.sdk_output)

        static_sdk_path = os.path.join(os.path.dirname(__file__), 'static');
        shutil.copytree(static_sdk_path, self.sdk_output)

    def _install_vanilla(self):
        """
        """
        for item in os.listdir(self.sdk_user_vanilla):
            s = os.path.join(self.sdk_user_vanilla, item)
            d = os.path.join(self.sdk_output, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)

        shutil.move('%s/%s' % (self.sdk_output, '__sdk'), '%s/%s' % (self.sdk_output, self.sdk_name))

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

        sdk_writer = SDKWriter(self.sdk_output, self.apiversions)
        sdk_writer.write()

        shutil.rmtree("%s/%s/__sdkapiversion" % (self.sdk_output, self.sdk_name))
        shutil.rmtree("%s/__overrides" % self.sdk_output)
