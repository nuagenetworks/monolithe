# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUMirrorDestinationsFetcher(NURESTFetcher):
    """ MirrorDestination fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUMirrorDestination
        return NUMirrorDestination