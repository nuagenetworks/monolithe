# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUPublicNetworkMacrosFetcher(NURESTFetcher):
    """ PublicNetworkMacro fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUPublicNetworkMacro
        return NUPublicNetworkMacro