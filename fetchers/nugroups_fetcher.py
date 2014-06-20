# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUGroupsFetcher(NURESTFetcher):
    """ Group fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from courgette.models import NUGroup
        return NUGroup
