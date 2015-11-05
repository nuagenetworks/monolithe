# -*- coding: utf-8 -*-

import os
import subprocess

from unittest import TestCase


class FunctionalTestCase(TestCase):
    """ Functional TestCase

    """

    # Utils

    def get_base_path(self):
        """
        """
        return "%s/examples" % os.getcwd()

    # Assertions

    def assertDirectoriesEquals(self, base_dir, output_dir):
        """
        """
        print subprocess.call(["diff", "-r", base_dir, output_dir])
        self.assertEquals(subprocess.call(["diff", "-r", base_dir, output_dir]), 0, "Generated sources in %s have some differences with %s" % (output_dir, base_dir))
