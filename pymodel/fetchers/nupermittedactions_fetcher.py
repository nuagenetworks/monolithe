# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUPermittedActionsFetcher(NURESTFetcher):
    """ PermittedAction fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUPermittedAction
        return NUPermittedAction