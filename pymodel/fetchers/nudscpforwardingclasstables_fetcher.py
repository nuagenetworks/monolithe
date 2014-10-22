# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUDSCPForwardingClassTablesFetcher(NURESTFetcher):
    """ DSCPForwardingClassTable fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUDSCPForwardingClassTable
        return NUDSCPForwardingClassTable