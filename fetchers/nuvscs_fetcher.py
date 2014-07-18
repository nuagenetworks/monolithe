# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUVSCsFetcher(NURESTFetcher):
    """ VSC fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVSC
        return NUVSC