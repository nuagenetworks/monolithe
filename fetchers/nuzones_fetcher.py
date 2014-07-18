# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUZonesFetcher(NURESTFetcher):
    """ Zone fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUZone
        return NUZone