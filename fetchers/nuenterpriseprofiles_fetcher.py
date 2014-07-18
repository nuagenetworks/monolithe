# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUEnterpriseProfilesFetcher(NURESTFetcher):
    """ EnterpriseProfile fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUEnterpriseProfile
        return NUEnterpriseProfile