# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUHostInterfacesFetcher(NURESTFetcher):
    """ HostInterface fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUHostInterface
        return NUHostInterface