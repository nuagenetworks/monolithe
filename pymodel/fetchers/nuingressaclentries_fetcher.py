# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUIngressACLEntriesFetcher(NURESTFetcher):
    """ IngressACLEntry fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUIngressACLEntry
        return NUIngressACLEntry