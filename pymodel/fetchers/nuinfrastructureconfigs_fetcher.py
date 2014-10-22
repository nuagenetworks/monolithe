# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUInfrastructureConfigsFetcher(NURESTFetcher):
    """ InfrastructureConfig fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUInfrastructureConfig
        return NUInfrastructureConfig