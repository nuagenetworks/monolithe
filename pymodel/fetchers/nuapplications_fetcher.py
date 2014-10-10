# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUApplicationsFetcher(NURESTFetcher):
    """ Application fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUApplication
        return NUApplication