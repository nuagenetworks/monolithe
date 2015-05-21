# -*- coding: utf-8 -*-

from monolithe.tests.functional import FunctionalTest
from monolithe.lib.parsers import SwaggerParser
from monolithe.lib.transformers import SwaggerTransformer, SpecificationTransformer


class SpecificationTransformerTests(FunctionalTest):
    """ Tests for SwaggerParser using file option

    """
    @classmethod
    def setUpClass(cls):
        """ Set up context

        """
        parser = SwaggerParser(path=cls.get_valid_path(), vsdurl=None, apiversion=None)
        swagger_resources = parser.run()

        cls.specifications = SwaggerTransformer.get_specifications(resources=swagger_resources)

    def test_process_resources(self):
        """ SpecificationTransformer process resources

        """
        objects = SpecificationTransformer.get_objects(self.specifications)
        self.assertTrue(len(objects), 99)
