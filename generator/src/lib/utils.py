# -*- coding: utf-8 -*-

import re

from printer import Printer


class Utils(object):
    """ utils """

    @classmethod
    def get_python_name(cls, name):
        """ Transform a given name to python name """
        first_cap_re = re.compile('(.)([A-Z](?!s([A-Z])*)[a-z]+)')
        all_cap_re = re.compile('([a-z0-9])([A-Z])')

        def repl(matchobj):
            """ Replacement method """
            if matchobj.start() == 0:
                return matchobj.expand(r"\1\2")
            else:
                return matchobj.expand(r"\1_\2")

        s1 = first_cap_re.sub(repl, name)
        return all_cap_re.sub(r'\1_\2', s1).lower()

    @classmethod
    def get_python_type_name(cls, type_name, attribute_name=None, object_name=None):
        """ Returns a python type according to a java type """

        if type_name in ['string', 'actiontype', 'direction', 'flowredirecttargettype', 'diffresult']:
            return 'str'

        if type_name == 'boolean':
            return 'bool'

        if type_name in ['int', 'integer']:
            return 'int'

        if type_name == 'enum':
            return 'str'

        if type_name in ['date']:
            return 'time'

        if type_name == 'string':
            return 'str'

        if type_name in ['double', 'float']:
            return 'float'

        Printer.warn("Cannot find type '%s' for attribute '%s' of object %s. Attribute has been converted to Python string." % (type_name, attribute_name, object_name))
        return 'str'

    @classmethod
    def get_singular_name(cls, plural_name):
        """ Returns the singular name of the plural name """

        if plural_name[-3:] == 'ies':
            return plural_name[:-3] + 'y'

        if plural_name[-1] == 's':
            return plural_name[:-1]

        return plural_name

    @classmethod
    def get_plural_name(cls, singular_name):
        """ Returns the plural name of the singular name """

        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        if singular_name[-1:] == 'y' and singular_name[-2] not in vowels:
            return singular_name[:-1] + 'ies'

        return singular_name + 's'
