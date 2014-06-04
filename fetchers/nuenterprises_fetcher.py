# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUEnterprisesFetcher(NURESTFetcher):
    """ Group fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from pymodeltests.models import NUEnterprise
        return NUEnterprise
