# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUInfrastructureVlanProfilesFetcher(NURESTFetcher):
    """ InfrastructureVlanProfile fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUInfrastructureVlanProfile
        return NUInfrastructureVlanProfile