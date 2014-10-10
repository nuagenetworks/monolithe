# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUStaticRoutesFetcher(NURESTFetcher):
    """ StaticRoute fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUStaticRoute
        return NUStaticRoute