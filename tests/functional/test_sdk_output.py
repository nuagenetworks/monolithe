# -*- coding: utf-8 -*-

import os

from tests.functional import FunctionalTestCase
from monolithe import MonolitheConfig
from monolithe.generators import SDKGenerator
from monolithe.specifications import FolderManager


class SDKOutputTest(FunctionalTestCase):
    """ Test Monolithe SDK output

    """
    def setUp(self):
        """ Generate a new SDK

        """
        base_path = self.get_base_path()

        directory_manager = FolderManager(
            "%s/specifications" % base_path,
            config_path="%s/specifications/monolithe.ini" % base_path)
        generator = SDKGenerator(directory_manager, None)
        generator.run()

    def tearDown(self):
        """
        """
        pass

    def test_generate_sdk(self):
        """ Verify SDK generation output
        """
        base_dir = "%s/tests/base/sdk" % os.getcwd()
        output_dir = "%s/codegen" % self.get_base_path()
        self.assertDirectoriesEquals(base_dir, output_dir)
