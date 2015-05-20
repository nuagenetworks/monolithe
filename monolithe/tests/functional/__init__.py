# -*- coding: utf-8 -*-

import os

from unittest import TestCase


class FunctionalTest(TestCase):
    """ Define a Functional Test Case

    """
    def __init__(self, methodName='runTest'):
        """ Initializes

        """
        TestCase.__init__(self, methodName=methodName)

        self.maxDiff = None  # Display all differences when assertion fails

    @classmethod
    def get_valid_path(cls):
        """ Returns swagger path """

        return '%s/monolithe/tests/static/V3_1' % os.getcwd()
