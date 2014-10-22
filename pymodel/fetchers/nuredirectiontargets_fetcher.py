# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NURedirectionTargetsFetcher(NURESTFetcher):
    """ RedirectionTarget fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NURedirectionTarget
        return NURedirectionTarget