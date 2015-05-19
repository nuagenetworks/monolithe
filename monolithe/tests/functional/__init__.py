# -*- coding: utf-8 -*-

import os

from unittest import TestCase


class FunctionalTest(TestCase):
    """

    """
    def __init__(self, methodName='runTest'):
        TestCase.__init__(self, methodName=methodName)

        self.maxDiff = None  # Display all differences when assertion fails

    def get_valid_path(self):
        """ Returns swagger path """

        return '%s/monolithe/tests/static/V3_1' % os.getcwd()
