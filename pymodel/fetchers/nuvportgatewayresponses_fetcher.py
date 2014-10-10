# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUVPortGatewayResponsesFetcher(NURESTFetcher):
    """ VPortGatewayResponse fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVPortGatewayResponse
        return NUVPortGatewayResponse