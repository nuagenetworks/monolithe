# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUWANServicesFetcher(NURESTFetcher):
    """ WANService fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUWANService
        return NUWANService