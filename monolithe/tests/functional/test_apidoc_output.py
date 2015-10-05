# -*- coding: utf-8 -*-

import os

from monolithe.tests.functional import FunctionalTestCase
from monolithe import MonolitheConfig
from monolithe.generators import APIDocumentationGenerator


class APIDocOutputTest(FunctionalTestCase):
    """ Test Monolithe API Documentation output

    """
    def setUp(self):
        """ Generate API Documentation

        """
        base_path = self.get_base_path()

        monolithe_config = MonolitheConfig.config_with_path("%s/conf/conf.ini" % base_path)
        generator = APIDocumentationGenerator(monolithe_config=monolithe_config)
        generator.generate_from_folder(folder="%s/specifications" % base_path)

    def tearDown(self):
        """
        """
        pass

    def test_generate_apidoc(self):
        """ Verify API Documentation generation output
        """
        base_dir = "%s/monolithe/tests/base/apidoc" % os.getcwd()
        output_dir = "%s/apidocgen" % self.get_base_path()
        self.assertDirectoriesEquals(base_dir, output_dir)
