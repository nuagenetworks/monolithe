# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUL2DomainTemplatesFetcher(NURESTFetcher):
    """ L2DomainTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUL2DomainTemplate
        return NUL2DomainTemplate