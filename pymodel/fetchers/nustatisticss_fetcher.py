# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUStatisticssFetcher(NURESTFetcher):
    """ Statistics fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUStatistics
        return NUStatistics