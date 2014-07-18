# -*- coding: utf-8 -*-

from restnuage import NURESTFetcher


class NULicensesFetcher(NURESTFetcher):
    """ License fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NULicense
        return NULicense