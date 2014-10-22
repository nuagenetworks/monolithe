# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUVirtualIPsFetcher(NURESTFetcher):
    """ VirtualIP fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVirtualIP
        return NUVirtualIP