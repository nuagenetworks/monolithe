# -*- coding: utf-8 -*-

from unittest import TestCase
from monolithe.lib.utils.urls import URLUtils


class IsURLTest(TestCase):
    """ Test for is_url function

    """
    def test_is_url(self):
        """ Verify that URLUtils.is_url returns True correctly

        """
        self.assertTrue(URLUtils.is_url('http://www.google.fr'))
        self.assertTrue(URLUtils.is_url('https://www.google.fr'))
        self.assertTrue(URLUtils.is_url('ftp://www.google.fr'))

    def test_is_not_url(self):
        """ Verify that URLUtils.is_url returns False when necessary

        """
        self.assertFalse(URLUtils.is_url(None))
        self.assertFalse(URLUtils.is_url(''))
        self.assertFalse(URLUtils.is_url('file://path/to/something'))
        self.assertFalse(URLUtils.is_url('/absolute/path'))
