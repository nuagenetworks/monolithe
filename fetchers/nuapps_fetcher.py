# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUAppsFetcher(NURESTFetcher):
    """ App fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUApp
        return NUApp