# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUIngressACLTemplatesFetcher(NURESTFetcher):
    """ IngressACLTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUIngressACLTemplate
        return NUIngressACLTemplate