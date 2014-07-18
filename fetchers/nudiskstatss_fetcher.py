# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUDiskStatssFetcher(NURESTFetcher):
    """ DiskStats fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUDiskStats
        return NUDiskStats