# -*- coding: utf-8 -*-

import os

from unittest import TestCase
from monolithe.lib.parsers import SwaggerFileParser
from monolithe.lib.converters import SwaggerToSpecConverter
from monolithe.lib.processors import ModelsProcessor

def get_valid_path():
    """ Returns swagger path """

    return '%s/monolithe/tests/static/V3_1' % os.getcwd()


class ModelsProcessorTests(TestCase):
    """ Tests for SwaggerParser using file option

    """
    @classmethod
    def setUpClass(cls):
        """ Set up context

        """
        parser = SwaggerFileParser(path=get_valid_path())
        swagger_resources = parser.grab_all()

        cls.resources = SwaggerToSpecConverter.convert(resources=swagger_resources)

    def test_process_resources(self):
        """ ModelsProcessor process resources

        """
        processed_resources = ModelsProcessor.process(resources=self.resources)
        self.assertEquals(len(processed_resources), 96)

        # Normal resource
        self.assertIn('Enterprise', processed_resources)

        # Mapped resources
        self.assertIn('Subnet', processed_resources)
        self.assertNotIn('SubNetwork', processed_resources)

        # Ignored resources
        self.assertNotIn('PublicNetworkMacro', processed_resources)

        # Model information
        model_enterprise = processed_resources['Enterprise']
        self.assertEquals(model_enterprise.name, 'Enterprise')
        self.assertEquals(model_enterprise.plural_name, 'Enterprises')
        self.assertEquals(model_enterprise.instance_name, 'enterprise')
        self.assertEquals(model_enterprise.instance_plural_name, 'enterprises')
        self.assertEquals(len(model_enterprise.apis['children']), 26)

        # Attributes
        attributes = model_enterprise.attributes
        resource_properies = self.resources['Enterprise']['model']['attributes']

        self.assertEquals(len(attributes), 21)

        for attribute in attributes:
            self.assertIn(attribute.remote_name, resource_properies)

