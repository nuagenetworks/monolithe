# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUBridgeInterfacesFetcher(NURESTFetcher):
    """ BridgeInterface fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUBridgeInterface
        return NUBridgeInterface