# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUZoneTemplatesFetcher(NURESTFetcher):
    """ NUZoneTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUZoneTemplate
        return NUZoneTemplate
