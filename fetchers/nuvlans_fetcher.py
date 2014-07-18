# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUVlansFetcher(NURESTFetcher):
    """ Vlan fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVlan
        return NUVlan