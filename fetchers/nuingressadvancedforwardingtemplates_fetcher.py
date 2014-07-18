# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUIngressAdvancedForwardingTemplatesFetcher(NURESTFetcher):
    """ IngressAdvancedForwardingTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUIngressAdvancedForwardingTemplate
        return NUIngressAdvancedForwardingTemplate