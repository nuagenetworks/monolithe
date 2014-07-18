# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUDSCPForwardingClassMappingsFetcher(NURESTFetcher):
    """ DSCPForwardingClassMapping fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUDSCPForwardingClassMapping
        return NUDSCPForwardingClassMapping