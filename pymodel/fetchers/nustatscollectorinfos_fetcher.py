# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUStatsCollectorInfosFetcher(NURESTFetcher):
    """ StatsCollectorInfo fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUStatsCollectorInfo
        return NUStatsCollectorInfo