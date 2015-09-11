# -*- coding: utf-8 -*-

import json
import os
import sys

from collections import OrderedDict
from difflib import SequenceMatcher


from monolithe.lib.utils.printer import Printer
from monolithe.lib.utils.vsdk import VSDKUtils


class ParsingUtils(object):
    """ Parsing Utilities

    """

    @classmethod
    def order(cls, results):
        """ Returns an Ordered Dictionary of the results

            Args:
                results (dict): a dictionary

            Returns:
                An ordrered dictionary structure

        """
        return OrderedDict(sorted(results.items(), key=lambda t: t[0]))

    @classmethod
    def order_by(cls, results, attribute_name, reverse=False):
        """ Returns list of objects ordered by attribute_name

            Args:
                results (list): a list of python objects
                attribute_name (string): the name of the attribute to sort
                reverse (bool): order asc (default) or desc

            Returns:
                A new list of objects

        """
        return sorted(results, key=lambda x: getattr(x, attribute_name), reverse=reverse)
