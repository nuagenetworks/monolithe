# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUAddressRangesFetcher(NURESTFetcher):
    """ AddressRange fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUAddressRange
        return NUAddressRange