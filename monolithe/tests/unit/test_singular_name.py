# -*- coding: utf-8 -*-

from unittest import TestCase
from monolithe.lib.utils.vsdk import VSDKUtils


class GetSingularNameTest(TestCase):
    """ Test for get_singular_name function

    """
    def assertSingularNameEquals(self, plural_name, singular_name):
        """ Check that the remote name is well converted to
            the python name

        """
        self.assertEqual(VSDKUtils.get_singular_name(plural_name), singular_name)

    def test_get_singular_name(self):
        """ Compute singular names properly

        """
        self.assertSingularNameEquals('enterprises', 'enterprise')
        self.assertSingularNameEquals('enterprise', 'enterprise')
        self.assertSingularNameEquals('Enterprises', 'Enterprise')
        self.assertSingularNameEquals('Enterprise', 'Enterprise')
        self.assertSingularNameEquals('policies', 'policy')
        self.assertSingularNameEquals('qoss', 'qos')
        self.assertSingularNameEquals('gateways', 'gateway')
