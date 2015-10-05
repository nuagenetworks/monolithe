# -*- coding: utf-8 -*-
# TODO

from bambou import NURESTFetcher


class GAListsFetcher(NURESTFetcher):
    """ Represents a GALists fetcher

        Notes:
            This fetcher enables to fetch GAList objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return GAList class that is managed.

            Returns:
                .GAList: the managed class
        """

        from .. import GAList
        return GAList

    