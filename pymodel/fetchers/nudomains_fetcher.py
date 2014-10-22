# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUDomainsFetcher(NURESTFetcher):
    """ Domain fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUDomain
        return NUDomain