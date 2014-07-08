# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUGatewaysFetcher(NURESTFetcher):
    """ Gateway fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from courgette.models import NUGateway
        return NUGateway