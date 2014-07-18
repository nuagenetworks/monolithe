# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUVMResyncsFetcher(NURESTFetcher):
    """ VMResync fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVMResync
        return NUVMResync