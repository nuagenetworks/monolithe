# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUIngressAdvancedForwardingsFetcher(NURESTFetcher):
    """ IngressAdvancedForwarding fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUIngressAdvancedForwarding
        return NUIngressAdvancedForwarding