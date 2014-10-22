# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUZonesFetcher(NURESTFetcher):
    """ Zone fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUZone
        return NUZone