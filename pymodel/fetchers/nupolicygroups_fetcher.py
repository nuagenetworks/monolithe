# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUPolicyGroupsFetcher(NURESTFetcher):
    """ PolicyGroup fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUPolicyGroup
        return NUPolicyGroup