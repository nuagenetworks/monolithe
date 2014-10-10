# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUInfrastructureGatewayProfilesFetcher(NURESTFetcher):
    """ InfrastructureGatewayProfile fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUInfrastructureGatewayProfile
        return NUInfrastructureGatewayProfile