# -*- coding: utf-8 -*-

from unittest import TestCase
from monolithe.lib import SDKUtils


class GetPluralNameTest(TestCase):
    """ Test for get_entity_name_plural function

    """
    def assertPluralNameEquals(self, singular_name, entity_name_plural):
        """ Check that the remote name is well converted to
            the python name

        """
        self.assertEqual(SDKUtils.get_plural(singular_name), entity_name_plural)

    def test_get_entity_name_plural(self):
        """ Compute plural names properly

        """
        self.assertPluralNameEquals('enterprise', 'enterprises')
        self.assertPluralNameEquals('enterprises', 'enterprises')
        self.assertPluralNameEquals('Enterprise', 'Enterprises')
        self.assertPluralNameEquals('Enterprises', 'Enterprises')
        self.assertPluralNameEquals('policy', 'policies')
        self.assertPluralNameEquals('gateway', 'gateways')
        self.assertPluralNameEquals('Gateway', 'Gateways')
        self.assertPluralNameEquals('qos', 'qos')
        self.assertPluralNameEquals('vrs', 'vrs')
        self.assertPluralNameEquals('VCenterHypervisor', 'VCenterHypervisors')
        self.assertPluralNameEquals('statistics', 'statistics')
