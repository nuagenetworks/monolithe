# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUVPNConnectsFetcher(NURESTFetcher):
    """ VPNConnect fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVPNConnect
        return NUVPNConnect