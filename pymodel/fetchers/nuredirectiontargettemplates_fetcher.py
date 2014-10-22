# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NURedirectionTargetTemplatesFetcher(NURESTFetcher):
    """ RedirectionTargetTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NURedirectionTargetTemplate
        return NURedirectionTargetTemplate