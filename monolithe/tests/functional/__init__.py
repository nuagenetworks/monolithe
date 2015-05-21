# -*- coding: utf-8 -*-

import os

from unittest2 import TestCase
from monolithe.utils.parse import ParsingUtils


class FunctionalTest(TestCase):
    """ Define a Functional Test Case

    """
    TMP_PATH = './tmp'
    _static_path = "%s/monolithe/tests" % os.getcwd()

    def __init__(self, methodName='runTest'):
        """ Initializes

        """
        TestCase.__init__(self, methodName=methodName)
        self.maxDiff = None

    @classmethod
    def get_swagger_files_path(cls):
        """ Returns swagger path """

        return '%s/monolithe/tests/static/V3_1' % os.getcwd()

    @classmethod
    def get_specificication_files_path(cls):
        """ Returns swagger path """

        return '%s/monolithe/tests/static/specifications' % os.getcwd()

    @classmethod
    def get_static_autogenerates_path(cls, filename):
        """ Returns swagger path """

        return '%s/monolithe/tests/static/vsdk/autogenerates/%s.py' % (os.getcwd(), filename)

    @classmethod
    def get_tmp_autogenerates_path(cls, filename):
        """ Returns swagger path """

        return '%s/3.1/vsdk/autogenerates/%s.py' % (cls.TMP_PATH, filename)

    # Assertions

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

    def assertFileOutputEqual(self, filename, message):
        """

        """
        valid_content = self._read_file(self.get_static_autogenerates_path(filename))
        expected_content = self._read_file(self.get_tmp_autogenerates_path(filename))

        self.assertEquals(valid_content, expected_content, message)

    # Utilities

    def _read_file(self, path):
        """ Read file at path and returns its content """
        file = open(path, 'r')
        content = file.read()
        file.close()

        return content
