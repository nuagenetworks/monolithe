# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.
# NUDomainsFetcher

from bambou import NURESTFetcher


class NUDomainsFetcher(NURESTFetcher):
    """ Represents a NUDomains fetcher

        Notes:
            This fetcher enables to fetch NUDomain objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return NUDomain class that is managed.

            Returns:
                vsdk.NUDomain: the managed class
        """

        from .. import NUDomain
        return NUDomain
