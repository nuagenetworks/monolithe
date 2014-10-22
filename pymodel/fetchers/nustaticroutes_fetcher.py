# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUStaticRoutesFetcher(NURESTFetcher):
    """ StaticRoute fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUStaticRoute
        return NUStaticRoute