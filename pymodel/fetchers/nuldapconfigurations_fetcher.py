# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NULDAPConfigurationsFetcher(NURESTFetcher):
    """ LDAPConfiguration fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NULDAPConfiguration
        return NULDAPConfiguration