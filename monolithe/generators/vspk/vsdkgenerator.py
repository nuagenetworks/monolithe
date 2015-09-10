# -*- coding: utf-8 -*-

import os
import shutil

from monolithe.lib.utils.printer import Printer
from monolithe.lib.utils.constants import Constants
from monolithe.lib.managers import SpecificationsRepositoryManager

from monolithe.generators.vspk.lib import SDKWriter

SpecificationsRepositoryManager


class VSDKGenerator(object):
    """ Generate VSDK

    """
    def __init__(self, github_api_url, github_token, specification_organization, github_specifications_repository, version=u'master', output_path=None, specifications_path=None, force_removal=False):
        """ Initializes a VSDKGenerator

            Can be used to generate a vsdk from a remote vsdurl or a local swagger_path.

            Args:

        """
        self.version = version
        self.output_path = output_path
        self.force_removal = force_removal
        self.specifications_path = specifications_path

        self.specification_repository_manager = SpecificationsRepositoryManager(github_api_url=github_api_url, \
                                                                                github_token=github_token, \
                                                                                specification_organization=specification_organization, \
                                                                                github_specifications_repository=github_specifications_repository)

    def run(self):
        """ Start the VSDK generation

        """
        Printer.log("Starting VSDK generation from branch %s of repository %s" % (self.version, self.specification_repository_manager.github_repository))

        filenames = self.specification_repository_manager.available_specifications(specification_version=self.version)

        specifications = {}
        for filename in filenames:
            specification = self.specification_repository_manager.get_specification(specification_file=filename, specification_version=self.version)
            specifications[specification.remote_name] = specification

        if self.output_path:
            directory = '%s/%s' % (self.output_path, self.version)
        else:
            directory = '%s/%s' % (Constants.CODEGEN_DIRECTORY, self.version)

        if self.force_removal and os.path.exists(directory):
            shutil.rmtree(directory)

        # Write Python sources
        writer = SDKWriter(directory=directory)
        writer.write(resources=specifications, apiversion=self.version, revision=1)

        Printer.success("Generated VSDK with %s objects for API version %s" % (len(specifications), self.version))
