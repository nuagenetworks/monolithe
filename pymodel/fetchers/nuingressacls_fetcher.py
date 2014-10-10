# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUIngressACLsFetcher(NURESTFetcher):
    """ IngressACL fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUIngressACL
        return NUIngressACL