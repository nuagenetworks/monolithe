# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUVRSsFetcher(NURESTFetcher):
    """ VRS fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVRS
        return NUVRS