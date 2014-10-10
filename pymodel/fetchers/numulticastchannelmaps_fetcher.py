# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUMultiCastChannelMapsFetcher(NURESTFetcher):
    """ MultiCastChannelMap fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUMultiCastChannelMap
        return NUMultiCastChannelMap