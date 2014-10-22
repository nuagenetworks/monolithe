# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUMultiCastRangesFetcher(NURESTFetcher):
    """ MultiCastRange fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUMultiCastRange
        return NUMultiCastRange