# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUGroupsFetcher(NURESTFetcher):
    """ Group fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUGroup
        return NUGroup