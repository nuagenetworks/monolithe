# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUDomainsFetcher(NURESTFetcher):
    """ Domain fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from courgette.models import NUDomain
        return NUDomain
