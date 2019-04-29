# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#

from bambou2 import NURESTFetcher


class GARootsFetcher(NURESTFetcher):
    """ Represents a GARoots fetcher

        Notes:
            This fetcher enables to fetch GARoot objects.

        See:
            bambou2.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return GARoot class that is managed.

            Returns:
                .GARoot: the managed class
        """

        from .. import GARoot
        return GARoot

    
