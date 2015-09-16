# -*- coding: utf-8 -*-

import os
import sys
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import Printer
from monolithe.specifications import RepositoryManager
from monolithe.generators.vspk.lib import SDKWriter

RepositoryManager


class VSDKGenerator(object):
    """ Generate VSDK

    """
    def __init__(self, version=u'master', output_path=None, specifications_path=None, force_removal=False):
        """
        """
        self.version = version
        self.output_path = output_path
        self.force_removal = force_removal
        self.specifications_path = specifications_path
        self.repository_manager = None

    def run(self, api_url, login_or_token, password, organization, repository):
        """ Start the VSDK generation

        """
        self.repository_manager = RepositoryManager(api_url=api_url,
                                                    login_or_token=login_or_token,
                                                    password=password,
                                                    organization=organization,
                                                    repository=repository)
        Printer.log("Getting specifications from branch `%s` of repository `%s`" % (self.version, self.repository_manager.repository))

        specifications = self.repository_manager.get_all_specifications(branch=self.version)

        self.generate(specifications)

    def generate(self, specifications):
        """
        """
        Printer.log("Starting VSDK generation for %s files" % len(specifications))

        if self.output_path:
            directory = '%s/%s' % (self.output_path, self.version)
        else:
            directory = '%s/%s' % (MonolitheConfig.get_config('codegen_directory'), self.version)

        if self.force_removal and os.path.exists(directory):
            shutil.rmtree(directory)

        # Write Python sources
        writer = SDKWriter(directory=directory)
        writer.write(resources=specifications, apiversion=self.version, revision=1)

        Printer.success("Generated VSDK with %s objects for API version %s" % (len(specifications), self.version))
