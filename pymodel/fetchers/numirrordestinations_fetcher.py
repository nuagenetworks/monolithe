# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUMirrorDestinationsFetcher(NURESTFetcher):
    """ MirrorDestination fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUMirrorDestination
        return NUMirrorDestination