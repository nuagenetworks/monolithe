# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUInfrastructureVlanProfilesFetcher(NURESTFetcher):
    """ InfrastructureVlanProfile fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUInfrastructureVlanProfile
        return NUInfrastructureVlanProfile