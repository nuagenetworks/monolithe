# -*- coding: utf-8 -*-

import os

from tests.functional import FunctionalTestCase
from monolithe import MonolitheConfig
from monolithe.generators import SDKGenerator


class SDKOutputTest(FunctionalTestCase):
    """ Test Monolithe SDK output

    """
    def setUp(self):
        """ Generate a new SDK

        """
        base_path = self.get_base_path()

        monolithe_config = MonolitheConfig.config_with_path("%s/conf/conf.ini" % base_path)
        generator = SDKGenerator(monolithe_config=monolithe_config)
        generator.initialize_folder_manager(folder="%s/specifications" % base_path)
        generator.generate_from_folder()

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
