# -*- coding: utf-8 -*-

import json
import os
import sys

from monolithe.utils.constants import Constants
from monolithe.utils.printer import Printer


class ParsingUtils(object):
    """ Parsing Utilities

    """

    @classmethod
    def get_package_name(cls, package_name):
        """ Returns the package name

            Args:
                package_name (string): the package name

            Returns:
                Returns the corresponding name

        """
        if package_name in Constants.PACKAGE_MAPPING:
            return Constants.PACKAGE_MAPPING[package_name]

        return package_name

    @classmethod
    def get_correct_name(cls, name):
        """ Returns the correct name of the entity

            Args:
                resource_name (string): the resource_name name

            Returns:
                Returns the corresponding name

        """
        if name in Constants.RESOURCE_MAPPING:
            return Constants.RESOURCE_MAPPING[name]

        return name

    @classmethod
    def parseJSON(self, filepath):
        """

        """
        if not os.path.isfile(filepath):
            Printer.raiseError("[File Path] Could not access %s" % (filepath))

        data = None
        try:
            data = json.load(open(filepath))
        except Exception:
            e = sys.exc_info()[1]
            Printer.raiseError("[File Path] Could load json file %s due to following error:\n%s" % (filepath, e.args[0]))

        return data
