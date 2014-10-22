# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUFlowForwardingPoliciesFetcher(NURESTFetcher):
    """ FlowForwardingPolicy fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUFlowForwardingPolicy
        return NUFlowForwardingPolicy