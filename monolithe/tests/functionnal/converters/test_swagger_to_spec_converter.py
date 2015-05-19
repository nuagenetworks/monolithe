# -*- coding: utf-8 -*-

import os

from unittest import TestCase
from monolithe.lib.parsers import SwaggerFileParser
from monolithe.lib.converters import SwaggerToSpecConverter


def get_valid_path():
    """ Returns swagger path """

    return '%s/monolithe/tests/static/V3_1' % os.getcwd()


class SwaggerToSpecConverterTests(TestCase):
    """ Tests for SwaggerParser using file option

    """
    def setUp(cls):
        """ Set up context

        """
        parser = SwaggerFileParser(path=get_valid_path())
        cls.swagger_resources = parser.grab_all()

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
