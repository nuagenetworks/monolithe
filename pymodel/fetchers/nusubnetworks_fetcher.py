# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUSubNetworksFetcher(NURESTFetcher):
    """ SubNetwork fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUSubNetwork
        return NUSubNetwork