# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUFlowSecurityPoliciesFetcher(NURESTFetcher):
    """ FlowSecurityPolicy fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUFlowSecurityPolicy
        return NUFlowSecurityPolicy