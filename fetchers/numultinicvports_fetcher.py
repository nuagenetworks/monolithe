# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUMultiNICVPortsFetcher(NURESTFetcher):
    """ MultiNICVPort fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUMultiNICVPort
        return NUMultiNICVPort