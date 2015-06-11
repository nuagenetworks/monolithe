# -*- coding: utf-8 -*-

import re

from .constants import Constants


class URLUtils(object):
    """ URL Utilities

    """
    @classmethod
    def remove_slash(cls, path):
        """ Removes last slash

            Args:
                path (string): the path to manipulate

            Returns:
                A path with the truncated slash

        """
        if path is None or len(path) == 0:
            return None

        if path[-1] == '/':
            return path[:-1]

        return path

    @classmethod
    def is_url(self, path):
        """ Verify if the path is a url of a file path

            Args:
                path (string): the path to verify

            Returns:
                True if the path respects HTTP protocols.
                False otherwise

            Examples:

                is_url('http://www.google.fr')
                >>> True

                is_url('/path/to/file')
                >>> False

        """
        if path is None:
            return False

        for protocol in Constants.HTTP_PROTOCOLS:
            if path.startswith(protocol):
                return True

        return False

    @classmethod
    def is_root_url(self, path, methods):
        """ Verify if the path and methods corresponds to a root url

            Args:
                path (string): the path to verify
                methods (list): a list of methods ['GET', 'POST', ...]

            Returns:
                True if the path is a root url
                False otherwise

            Examples:

                is_root_url('/enterprises/{id}', ['PUT'])
                >>> False

                is_root_url('/enterprises/{id}', ['GET'])
                >>> True

                is_root_url('/enterprises', ['POST'])
                >>> True

        """
        return 'POST' in methods or ('{id}' not in path and 'GET' in methods)

    @classmethod
    def split_package_path(cls, package_path):
        """ Split package path to retrieve the package and the resource name

            Args:
                package_path (string): the package path

            Returns:
                (package, resource_name)

            Example:
                split_package_path('/usermgmt/User')
                >>> (/usermgmt, User)
        """

        return package_path.rsplit('/', 1)

    @classmethod
    def resources_from_path(cls, path):
        """ Retrieve all resources names from the given path

            Args:
                path (string): the path

            Returns:
                A list of resources

            Examples:
                resources_from_path('/enterprises/{id}/domain')
                >>> ['enterprises', 'domains']

        """
        if path is None:
            return None

        return filter(bool, re.split('/\{id\}?/?', path[1:] if path.startswith('/') else path))
