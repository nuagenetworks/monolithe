# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUEgressACLEntriesFetcher(NURESTFetcher):
    """ EgressACLEntry fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUEgressACLEntry
        return NUEgressACLEntry