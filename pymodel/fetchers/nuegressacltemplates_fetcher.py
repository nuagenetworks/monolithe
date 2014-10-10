# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUEgressACLTemplatesFetcher(NURESTFetcher):
    """ EgressACLTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUEgressACLTemplate
        return NUEgressACLTemplate