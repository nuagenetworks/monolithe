# -*- coding: utf-8 -*-

import re

from .printer import Printer


class Utils(object):
    """ utils """

    INVARIANT_NAMES = ['qos', 'vrs', 'cms', 'statistics']

    @classmethod
    def _string_clean(cls, string):
        """ String cleaning for specific cases

            This is very specific and is used to force
            some underscore while using get_python_name.

            Args:
                string: the string to clean

            Returns:
                Returns a clean string
        """
        rep = {
            "VPort": "Vport",
            "IPID": "IpID"
        }

        rep = dict((re.escape(k), v) for k, v in rep.iteritems())
        pattern = re.compile("|".join(rep.keys()))
        return pattern.sub(lambda m: rep[re.escape(m.group(0))], string)

    @classmethod
    def get_python_name(cls, name):
        """ Transform a given name to python name """
        first_cap_re = re.compile('(.)([A-Z](?!s([A-Z])*)[a-z]+)')
        all_cap_re = re.compile('([a-z0-9])([A-Z])')

        s1 = first_cap_re.sub(r'\1_\2', Utils._string_clean(name))
        return all_cap_re.sub(r'\1_\2', s1).lower()

    @classmethod
    def get_python_type_name(cls, type_name, attribute_name=None, object_name=None):
        """ Returns a python type according to a java type """

        if type_name in ['string', 'str', 'enum']:
            return 'str'

        if type_name == 'long':
            return 'long'

        if type_name == 'boolean':
            return 'bool'

        if type_name in ['int', 'integer']:
            return 'int'

        if type_name in ['date', 'datetime', 'time']:
            return 'time'

        if type_name in ['double', 'float']:
            return 'float'

        # Known as wrong on the server side.
        if type_name in ['GWPersonality','ManagedObjectType','ActionType','Action','VPortTagEndPointType','TriggerType','FlowRedirectTargetType']:
            return 'str'

        clean_name = type_name.lower().strip()
        if clean_name.startswith('array') or clean_name.startswith('collection'):
            return 'list'

        # Special cases where we need to handle nested objects...
        if clean_name in ['vmresync', 'qosprimitive', 'egressqosprimitive', 'statisticspolicy', 'map', 'diffresult', 'object']:
            return 'object'

        return None

    @classmethod
    def get_singular_name(cls, plural_name):
        """ Returns the singular name of the plural name """

        if plural_name in Utils.INVARIANT_NAMES:
            return plural_name

        if plural_name[-3:] == 'ies':
            return plural_name[:-3] + 'y'

        if plural_name[-1] == 's':
            return plural_name[:-1]

        return plural_name

    @classmethod
    def get_plural_name(cls, singular_name):
        """ Returns the plural name of the singular name """

        if singular_name in Utils.INVARIANT_NAMES:
            return singular_name

        vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        if singular_name[-1] == 'y' and singular_name[-2] not in vowels:
            return singular_name[:-1] + 'ies'

        if singular_name[-1] != 's':
            return singular_name + 's'

        return singular_name

    @classmethod
    def get_version(self, server_version):
        """ Parse Server Api version to have a
            proper float version

            Args:
                server_version: version that can be like V3_0

            Returns:
                return a float number

        """
        if server_version.startswith('V'):
            server_version = server_version[1:]

        server_version = server_version.replace('_', '.')

        try:
            version = float(server_version)
        except:
            Printer.warn("Could not get a valid version from %s" % server_version)
            version = 0.0

        return version

    @classmethod
    def remove_slash(cls, path):
        """ Removes last slash

        """
        if path is None or len(path) == 0:
            return None

        if path[-1] == '/':
            return path[:-1]

        return path

    @classmethod
    def get_vspk_version(cls, version):
        """ Get the vspk version according to the given version

            Args:
                version (int): the version

            Returns:
                version as string

            Example:
                get_vspk_version(3.1)
                >>> v3_1

        """
        return ('v%s' % version).replace('.', '_')
