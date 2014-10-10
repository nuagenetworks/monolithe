# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NURedirectionTargetsFetcher(NURESTFetcher):
    """ RedirectionTarget fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NURedirectionTarget
        return NURedirectionTarget