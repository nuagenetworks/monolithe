# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUJobsFetcher(NURESTFetcher):
    """ Job fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUJob
        return NUJob