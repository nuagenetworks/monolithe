# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUAutoDiscGatewaysFetcher(NURESTFetcher):
    """ AutoDiscGateway fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUAutoDiscGateway
        return NUAutoDiscGateway