# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUMultiCastRangesFetcher(NURESTFetcher):
    """ MultiCastRange fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUMultiCastRange
        return NUMultiCastRange