# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUVlanTemplatesFetcher(NURESTFetcher):
    """ VlanTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVlanTemplate
        return NUVlanTemplate