# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUGatewayTemplatesFetcher(NURESTFetcher):
    """ GatewayTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUGatewayTemplate
        return NUGatewayTemplate
