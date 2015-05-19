# -*- coding: utf-8 -*-

from monolithe.utils.constants import Constants


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
    def get_resource_name(cls, resource_name):
        """ Returns the resource name

            Args:
                resource_name (string): the resource_name name

            Returns:
                Returns the corresponding name

        """
        if resource_name in Constants.RESOURCE_MAPPING:
            return Constants.RESOURCE_MAPPING[resource_name]

        return resource_name
