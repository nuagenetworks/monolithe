# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.
# NU{{ model.plural_name }}Fetcher

from bambou import NURESTFetcher


class NU{{ model.plural_name }}Fetcher(NURESTFetcher):
    """ Represents a NU{{ model.plural_name }} fetcher

        Notes:
            This fetcher enables to fetch NU{{ model.name }} objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return NU{{ model.name }} class that is managed.

            Returns:
                vsdk.NU{{ model.name }}: the managed class
        """

        from .. import NU{{ model.name }}
        return NU{{ model.name }}

