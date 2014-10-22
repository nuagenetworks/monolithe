# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUPortTemplatesFetcher(NURESTFetcher):
    """ PortTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUPortTemplate
        return NUPortTemplate