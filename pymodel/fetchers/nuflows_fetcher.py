# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUFlowsFetcher(NURESTFetcher):
    """ Flow fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUFlow
        return NUFlow