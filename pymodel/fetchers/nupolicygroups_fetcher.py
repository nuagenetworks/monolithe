# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUPolicyGroupsFetcher(NURESTFetcher):
    """ PolicyGroup fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUPolicyGroup
        return NUPolicyGroup