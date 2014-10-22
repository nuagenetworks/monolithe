# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUFloatingIpsFetcher(NURESTFetcher):
    """ FloatingIp fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUFloatingIp
        return NUFloatingIp