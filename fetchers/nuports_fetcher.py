# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUPortsFetcher(NURESTFetcher):
    """ Port fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUPort
        return NUPort