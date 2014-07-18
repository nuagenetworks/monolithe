# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUAddressRangesFetcher(NURESTFetcher):
    """ AddressRange fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUAddressRange
        return NUAddressRange