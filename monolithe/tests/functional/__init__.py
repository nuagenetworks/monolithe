# -*- coding: utf-8 -*-

import os

from unittest import TestCase
from monolithe.utils.parse import ParsingUtils


class FunctionalTest(TestCase):
    """ Define a Functional Test Case

    """
    def __init__(self, methodName='runTest'):
        """ Initializes

        """
        TestCase.__init__(self, methodName=methodName)

    @classmethod
    def get_valid_path(cls):
        """ Returns swagger path """

        return '%s/monolithe/tests/static/V3_1' % os.getcwd()

    def assertOutputEqual(self, d1, d2, parent_key=None):
        """ Compare two dictionaries

        """
        d1 = ParsingUtils.order(d1)
        d2 = ParsingUtils.order(d2)

        self.assertEqual(d1.keys(), d2.keys())

        for key, value in d1.iteritems():
            value_type = type(value)
            value2 = d2[key]
            if value_type == dict:
                self.assertOutputEqual(value, value2, parent_key=key)
            elif value_type == list:
                self.assertEqual(value.sort(), value2.sort())
            else:
                self.assertEqual(value, value2, '%s != %s for key %s of %s' % (value, value2, key, parent_key))
