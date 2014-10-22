# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUZoneTemplatesFetcher(NURESTFetcher):
    """ ZoneTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUZoneTemplate
        return NUZoneTemplate