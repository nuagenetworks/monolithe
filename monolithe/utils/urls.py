# -*- coding: utf-8 -*-

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
    def split_resource_path(self, resource_path):
        """ Split resource path to retrieve the package and the resource name

            Args:
                resource_path (string): the resource path

            Returns:
                (package, resource_name)

            Example:
                split_resource_path('/usermgmt/User')
                >>> (/usermgmt, User)
        """

        return resource_path.rsplit('/', 1)
