# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUSubNetworkTemplatesFetcher(NURESTFetcher):
    """ SubNetworkTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUSubNetworkTemplate
        return NUSubNetworkTemplate