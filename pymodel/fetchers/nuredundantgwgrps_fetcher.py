# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NURedundantGWGrpsFetcher(NURESTFetcher):
    """ RedundantGWGrp fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NURedundantGWGrp
        return NURedundantGWGrp