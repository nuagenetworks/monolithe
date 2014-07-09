# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUSubnetsFetcher(NURESTFetcher):
    """ NUSubnet fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUSubnet
        return NUSubnet
