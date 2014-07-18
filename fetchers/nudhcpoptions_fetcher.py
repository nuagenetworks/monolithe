# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUDHCPOptionsFetcher(NURESTFetcher):
    """ DHCPOption fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUDHCPOption
        return NUDHCPOption