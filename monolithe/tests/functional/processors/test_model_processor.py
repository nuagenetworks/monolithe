# -*- coding: utf-8 -*-

from monolithe.tests.functional import FunctionalTest
from monolithe.lib.parsers import SwaggerParser
from monolithe.lib.transformers import SwaggerTransformer
from monolithe.lib.processors import ModelsProcessor


class ModelsProcessorTests(FunctionalTest):
    """ Tests for SwaggerParser using file option

    """
    @classmethod
    def setUpClass(cls):
        """ Set up context

        """
        parser = SwaggerParser(path=cls.get_valid_path(), vsdurl=None, apiversion=None)
        swagger_resources = parser.run()

        cls.resources = SwaggerTransformer.convert(resources=swagger_resources)

    def test_process_resources(self):
        """ ModelsProcessor process resources

        """
        processed_resources = ModelsProcessor.process(resources=self.resources)

        self.assertEquals(len(processed_resources), 96)

        # Normal resource
        self.assertIn('enterprise', processed_resources)  # Rest names
        self.assertNotIn('Enterprise', processed_resources)

        # Mapped resources
        self.assertIn('subnet', processed_resources)
        self.assertNotIn('SubNetwork', processed_resources)

        # Ignored resources
        self.assertNotIn('PublicNetworkMacro', processed_resources)

        # Special cases
        self.assertIn('eventlog', processed_resources.keys())
        self.assertIn('alarm', processed_resources.keys())
        self.assertNotIn('allalarm', processed_resources.keys())

        # Model information
        model_enterprise = processed_resources['enterprise']
        self.assertEquals(model_enterprise.name, 'Enterprise')
        self.assertEquals(model_enterprise.plural_name, 'Enterprises')
        self.assertEquals(model_enterprise.instance_name, 'enterprise')
        self.assertEquals(model_enterprise.instance_plural_name, 'enterprises')
        self.assertEquals(len(model_enterprise.apis['children']), 26)

        # Attributes
        attributes = model_enterprise.attributes
        resource_properies = self.resources['enterprise']['model']['attributes']

        self.assertEquals(len(attributes), 13)

        for attribute in attributes:
            self.assertIn(attribute.remote_name, resource_properies)
