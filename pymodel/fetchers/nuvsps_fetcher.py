# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUVSPsFetcher(NURESTFetcher):
    """ VSP fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVSP
        return NUVSP