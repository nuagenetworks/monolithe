# -*- coding: utf-8 -*-

import os
import sys
import shutil

from ConfigParser import ConfigParser

from monolithe.lib.utils.printer import Printer
from monolithe.lib.utils.constants import Constants
from monolithe.lib.managers import SpecificationsRepositoryManager

from monolithe.generators.vspk.lib import SDKWriter

SpecificationsRepositoryManager


class VSDKGenerator(object):
    """ Generate VSDK

    """
    def __init__(self, api_url, login_or_token, password, organization, repository, version=u'master', output_path=None, specifications_path=None, force_removal=False):
        """
        """
        self.version = version
        self.output_path = output_path
        self.force_removal = force_removal
        self.specifications_path = specifications_path

        self.specification_repository_manager = SpecificationsRepositoryManager(api_url=api_url, \
                                                                                login_or_token=login_or_token, \
                                                                                password=password, \
                                                                                organization=organization, \
                                                                                repository=repository)

    def run(self):
        """ Start the VSDK generation

        """
        Printer.log("Starting VSDK generation from branch `%s` of repository `%s`" % (self.version, self.specification_repository_manager.repository))

        filenames = self.specification_repository_manager.available_specifications(version=self.version)
        specifications = self.specification_repository_manager.get_specifications(names=filenames, version=self.version)

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
