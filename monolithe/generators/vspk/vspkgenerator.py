# -*- coding: utf-8 -*-

import os
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.lib import Printer


class VSPKGenerator(object):
    """ Create a VSPK Package containing SDK versions

    """
    def __init__(self, versions, output_path=None):
        """ Initialize a VSPKGenerator

        """
        self.versions = versions

        self._path_vanilla_vspk = '%s/vanilla/vspk' % os.path.dirname(os.path.realpath(__file__))
        self._path_codegen = output_path if output_path else MonolitheConfig.get_config('codegen_directory')
        self._path_generated_vspk = "%s/vspk" % self._path_codegen

    def run(self):
        """ Create the VSPK package

        """
        self.generate()

    def generate(self):
        """
        """
        self._prepare_vspk_destination(self._path_vanilla_vspk, self._path_generated_vspk)

        for version in self.versions:

            if version == 'master':
                Printer.warn('master branch should be used for development purpose only.')

            self._include_vsdk(version, self._path_codegen, self._path_generated_vspk)

    def _prepare_vspk_destination(self, source_path, destination_path):
        """ Clean up detination environement

        """
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)

        shutil.copytree(source_path, destination_path)

    def _include_vsdk(self, vsdk_version, vsdk_base_path, vspk_path):
        """ Install Generated version of vsdk to vspk"

        """
        parsed_version = SDKUtils.get_string_version(vsdk_version)
        source_sdk_path = "%s/%s/vsdk/" % (vsdk_base_path, vsdk_version)
        dest_sdk_path = "%s/vspk/vsdk/%s" % (vspk_path, parsed_version)

        Printer.success("Adding VSDK version %s to VSPK" % vsdk_version)

        shutil.copytree(source_sdk_path, dest_sdk_path)
