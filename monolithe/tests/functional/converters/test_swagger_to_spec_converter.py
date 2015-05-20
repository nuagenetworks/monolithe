# -*- coding: utf-8 -*-

from monolithe.tests.functional import FunctionalTest
from monolithe.lib.parsers import SwaggerParser
from monolithe.lib.converters import SwaggerToSpecConverter


class SwaggerToSpecConverterTests(FunctionalTest):
    """ Tests for SwaggerParser using file option

    """
    def setUp(cls):
        """ Set up context

        """
        parser = SwaggerParser(path=cls.get_valid_path(), vsdurl=None, apiversion=None)
        cls.swagger_resources = parser.run()

    def tearDown(cls):
        """ Clean up context
        """
        cls.swagger_resources = None

    def test_swagger_resources_keys_are_rest_names(self):
        """ SwaggerToSpecConverter uses rest names
        """

        resources = SwaggerToSpecConverter.convert(resources=self.swagger_resources)

        self.assertEqual(len(resources), 96)
        self.assertIn('eventlog', resources.keys())
        self.assertIn('alarm', resources.keys())
        self.assertNotIn('allalarm', resources.keys())
        self.assertIn('RESTUser', resources.keys())
