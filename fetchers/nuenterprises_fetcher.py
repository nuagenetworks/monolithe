# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUEnterprisesFetcher(NURESTFetcher):
    """ Enterprise fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUEnterprise
        return NUEnterprise