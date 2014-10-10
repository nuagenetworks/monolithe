# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUNetworkLayoutsFetcher(NURESTFetcher):
    """ NetworkLayout fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUNetworkLayout
        return NUNetworkLayout