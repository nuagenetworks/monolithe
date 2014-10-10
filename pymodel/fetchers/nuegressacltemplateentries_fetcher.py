# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUEgressACLTemplateEntriesFetcher(NURESTFetcher):
    """ EgressACLTemplateEntry fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUEgressACLTemplateEntry
        return NUEgressACLTemplateEntry