# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUVPortsFetcher(NURESTFetcher):
    """ VPort fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVPort
        return NUVPort