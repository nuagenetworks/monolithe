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
    def __init__(self):
        """ Initialize a SDKGenerator

        """
        self.temp_doc_path = "/tmp/docgen/sdkdoc"
        self.sdkdoc_output = MonolitheConfig.get_option("sdkdoc_output", "sdkdoc")
        self.sdkdoc_user_vanilla = MonolitheConfig.get_option("sdkdoc_user_vanilla", "sdkdoc")
        self.sdk_path = MonolitheConfig.get_option("sdk_output", "sdk")
        self.sdk_name = MonolitheConfig.get_option("sdk_name", "sdk")


    def _install_system_vanilla(self):
        """
        """
        if os.path.exists(self.temp_doc_path):
            shutil.rmtree(self.temp_doc_path)

        if os.path.exists(self.sdkdoc_output):
            shutil.rmtree(self.sdkdoc_output)

        system_vanilla_path = os.path.join(os.path.dirname(__file__), "vanilla");
        shutil.copytree(system_vanilla_path, self.temp_doc_path)

    def _install_user_vanilla(self):
        """
        """
        if not os.path.exists(self.sdkdoc_user_vanilla):
            return

        for item in os.listdir(self.sdkdoc_user_vanilla):
            s = os.path.join(self.sdkdoc_user_vanilla, item)
            d = os.path.join(self.temp_doc_path, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)

    def _cleanup(self):
        """
        """
        shutil.rmtree('%s/_modules' % self.sdkdoc_output)
        shutil.rmtree('%s/_sources' % self.sdkdoc_output)
        # shutil.rmtree(self.temp_doc_path)

    def run(self):
        """
        """
        Printer.log("Generating %s documentation..." % self.sdk_name)

        sys.path.append(self.sdk_path)
        subprocess_environ = {"PYTHONPATH": ":".join(sys.path), "PATH": os.environ["PATH"]}

        self._install_system_vanilla()
        self._install_user_vanilla()

        writer = SDKDocWriter(directory=self.temp_doc_path)
        writer.write()

        origin_path = os.getcwd()
        os.chdir(self.temp_doc_path)
        process = subprocess.Popen(['make', 'html'], env=subprocess_environ)
        process.communicate()
        os.chdir(origin_path)

        if os.path.exists(self.sdkdoc_output):
            shutil.rmtree(self.sdkdoc_output)

        shutil.copytree("%s/_build/html/" % self.temp_doc_path, self.sdkdoc_output)

        self._cleanup()

        Printer.success("Generated SDK documentation")
