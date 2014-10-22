# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NULocationsFetcher(NURESTFetcher):
    """ Location fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NULocation
        return NULocation