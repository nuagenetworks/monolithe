# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUSubnetTemplatesFetcher(NURESTFetcher):
    """ NUSubnetTemplate fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUSubnetTemplate
        return NUSubnetTemplate
