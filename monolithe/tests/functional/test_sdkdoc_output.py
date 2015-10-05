# -*- coding: utf-8 -*-

import os

from monolithe.tests.functional import FunctionalTestCase
from monolithe import MonolitheConfig
from monolithe.generators import SDKDocGenerator

from nose.plugins.skip import SkipTest

class SDKDocOutputTest(FunctionalTestCase):
    """ Test Monolithe SDK output

    """
    def setUp(self):
        """ Generate SDK Documentation

        """
        base_path = self.get_base_path()

        monolithe_config = MonolitheConfig.config_with_path("%s/conf/conf.ini" % base_path)
        doc_generator = SDKDocGenerator(monolithe_config=monolithe_config)
        doc_generator.generate()

    def tearDown(self):
        """
        """
        pass

    @SkipTest  # TODO: This test is skipped while the sdkdoc is broken
    def test_generate_sdkdoc(self):
        """ Verify SDK Documentation generation output
        """
        base_dir = "%s/monolithe/tests/base/sdkdoc" % os.getcwd()
        output_dir = "%s/sdkdoc" % self.get_base_path()
        self.assertDirectoriesEquals(base_dir, output_dir)
