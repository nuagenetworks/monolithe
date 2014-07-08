# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUDomainTemplatesFetcher(NURESTFetcher):
    """ DomainTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from courgette.models import NUDomainTemplate
        return NUDomainTemplate
