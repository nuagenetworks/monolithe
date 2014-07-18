# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUSharedNetworkResourcesFetcher(NURESTFetcher):
    """ SharedNetworkResource fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUSharedNetworkResource
        return NUSharedNetworkResource