# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUSystemConfigsFetcher(NURESTFetcher):
    """ SystemConfig fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUSystemConfig
        return NUSystemConfig