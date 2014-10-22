# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUInfrastructureGatewayProfilesFetcher(NURESTFetcher):
    """ InfrastructureGatewayProfile fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUInfrastructureGatewayProfile
        return NUInfrastructureGatewayProfile