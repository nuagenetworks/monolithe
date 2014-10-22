# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUSubNetworkTemplatesFetcher(NURESTFetcher):
    """ SubNetworkTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUSubNetworkTemplate
        return NUSubNetworkTemplate