# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUStatisticsPoliciesFetcher(NURESTFetcher):
    """ StatisticsPolicy fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUStatisticsPolicy
        return NUStatisticsPolicy