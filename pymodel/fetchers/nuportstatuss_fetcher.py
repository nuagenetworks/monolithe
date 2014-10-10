# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUPortStatussFetcher(NURESTFetcher):
    """ PortStatus fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUPortStatus
        return NUPortStatus