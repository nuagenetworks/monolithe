# -*- coding: utf-8 -*-

import os

from unittest import TestCase
from vsdgenerators.lib.parsers import SwaggerFileParser
from vsdgenerators.lib.processors import ModelsProcessor

def get_valid_path():
    """ Returns swagger path """

    return '%s/vsdgenerators/tests/functionnal/V3_1' % os.getcwd()


class ModelsProcessorTests(TestCase):
    """ Tests for SwaggerParser using file option

    """
    @classmethod
    def setUpClass(cls):
        """ Set up context

        """
        parser = SwaggerFileParser(path=get_valid_path())
        cls.resources = parser.grab_all()

    def test_process_resources(self):
        """ ModelsProcessor process resources

        """
        processed_resources = ModelsProcessor.process(resources=self.resources)
        self.assertEquals(len(processed_resources), 95)

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
        self.assertEquals(len(model_enterprise.relations), 26)

        # Attributes
        attributes = model_enterprise.attributes
        resource_properies = self.resources['Enterprise']['models']['Enterprise']['properties']

        self.assertEquals(len(attributes), 21)

        for attribute in attributes:
            self.assertIn(attribute.remote_name, resource_properies)

