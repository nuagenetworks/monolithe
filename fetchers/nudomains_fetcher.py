# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUDomainsFetcher(NURESTFetcher):
    """ Domain fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUDomain
        return NUDomain