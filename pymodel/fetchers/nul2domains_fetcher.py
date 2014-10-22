# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUL2DomainsFetcher(NURESTFetcher):
    """ L2Domain fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUL2Domain
        return NUL2Domain