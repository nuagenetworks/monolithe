# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#

from bambou2 import NURESTFetcher


class GAListsFetcher(NURESTFetcher):
    """ Represents a GALists fetcher

        Notes:
            This fetcher enables to fetch GAList objects.

        See:
            bambou2.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return GAList class that is managed.

            Returns:
                .GAList: the managed class
        """

        from .. import GAList
        return GAList

    
