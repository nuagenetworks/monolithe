# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUVSDsFetcher(NURESTFetcher):
    """ VSD fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVSD
        return NUVSD