# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NUBootstrapActivationsFetcher(NURESTFetcher):
    """ BootstrapActivation fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUBootstrapActivation
        return NUBootstrapActivation