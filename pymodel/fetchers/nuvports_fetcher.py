# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUVPortsFetcher(NURESTFetcher):
    """ VPort fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVPort
        return NUVPort