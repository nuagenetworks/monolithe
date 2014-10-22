# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUTiersFetcher(NURESTFetcher):
    """ Tier fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUTier
        return NUTier