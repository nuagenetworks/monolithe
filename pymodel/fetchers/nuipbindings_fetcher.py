# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUIPBindingsFetcher(NURESTFetcher):
    """ IPBinding fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUIPBinding
        return NUIPBinding