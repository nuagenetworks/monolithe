# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUDomainTemplatesFetcher(NURESTFetcher):
    """ DomainTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUDomainTemplate
        return NUDomainTemplate
