# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUServicesFetcher(NURESTFetcher):
    """ Service fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUService
        return NUService