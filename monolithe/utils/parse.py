# -*- coding: utf-8 -*-

import json
import os
import sys

from collections import OrderedDict

from monolithe.utils.constants import Constants
from monolithe.utils.printer import Printer
from difflib import SequenceMatcher


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
    def parseJSON(cls, filepath):
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

    @classmethod
    def are_similar_strings(cls, string1, string2, ratio=0.8):
        """

        """
        r = SequenceMatcher(None, string1, string2).ratio()

        if r >= ratio:
            return True

        return False

    @classmethod
    def have_similar_strings(cls, string1, strings, ratio=0.8):
        """

        """
        for string in strings:
            if cls.are_similar_strings(string1, string):
                return True

        return False

    @classmethod
    def reverse_filters(cls, filters):
        """ Reverse filters according to resource mapping constants

        """
        valid_names = Constants.RESOURCE_MAPPING.values()
        rest_names = [name.lower() for name in Constants.RESOURCE_MAPPING.keys()]

        new_filters = []
        for f in filters:
            try:
                index = valid_names.index(f)
                name = rest_names[index]
            except ValueError:
                name = f

            new_filters.append(name)

        return new_filters

    @classmethod
    def order(cls, results):
        """ Returns an Ordered Dictionary of the results

            Args:
                results (dict): a dictionary

            Returns:
                An ordrered dictionary structure

        """
        return OrderedDict(sorted(results.items(), key=lambda t: t[0]))
