# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUBootstrapsFetcher(NURESTFetcher):
    """ Bootstrap fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUBootstrap
        return NUBootstrap