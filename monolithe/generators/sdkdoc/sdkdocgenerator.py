# -*- coding: utf-8 -*-

import sys
import importlib
import os
import shutil
import re
import inspect
import subprocess

from monolithe import MonolitheConfig
from monolithe.lib import Printer
from .lib import SDKDocWriter



class SDKDocGenerator(object):
    """
    """
    def __init__(self, monolithe_config):
        """ Initialize a SDKGenerator

        """
        self.monolithe_config = monolithe_config
        self._sdkdoc_output = self.monolithe_config.get_option("sdkdoc_output", "sdkdoc")
        self._sdkdoc_user_vanilla = self.monolithe_config.get_option("sdkdoc_user_vanilla", "sdkdoc")
        self._sdkdoc_tmp_path = self.monolithe_config.get_option("sdkdoc_tmp_path", "sdkdoc")
        self._sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")

    def _install_system_vanilla(self):
        """
        """
        if os.path.exists(self._sdkdoc_tmp_path):
            shutil.rmtree(self._sdkdoc_tmp_path)

        if os.path.exists(self._sdkdoc_output):
            shutil.rmtree(self._sdkdoc_output)

        system_vanilla_path = os.path.join(os.path.dirname(__file__), "vanilla");
        shutil.copytree(system_vanilla_path, self._sdkdoc_tmp_path)

    def _install_user_vanilla(self):
        """
        """
        if not os.path.exists(self._sdkdoc_user_vanilla):
            return

        for item in os.listdir(self._sdkdoc_user_vanilla):
            s = os.path.join(self._sdkdoc_user_vanilla, item)
            d = os.path.join(self._sdkdoc_tmp_path, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)

    def _cleanup(self):
        """
        """
        shutil.rmtree('%s/_modules' % self._sdkdoc_output)
        shutil.rmtree('%s/_sources' % self._sdkdoc_output)
        shutil.rmtree(self._sdkdoc_tmp_path)

    def run(self):
        """
        """
        Printer.log("Generating %s documentation..." % self._sdk_name)

        sys.path.append(self._sdk_output)
        subprocess_environ = {"PYTHONPATH": ":".join(sys.path), "PATH": os.environ["PATH"]}

        self._install_system_vanilla()
        self._install_user_vanilla()

        writer = SDKDocWriter(monolithe_config=self.monolithe_config)
        writer.write()

        origin_path = os.getcwd()
        os.chdir(self._sdkdoc_tmp_path)
        process = subprocess.Popen(['make', 'html'], env=subprocess_environ)
        process.communicate()
        os.chdir(origin_path)

        if os.path.exists(self._sdkdoc_output):
            shutil.rmtree(self._sdkdoc_output)

        shutil.copytree("%s/_build/html/" % self._sdkdoc_tmp_path, self._sdkdoc_output)

        self._cleanup()

        Printer.success("Generated SDK documentation")
