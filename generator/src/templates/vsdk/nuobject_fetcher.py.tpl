# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.
# NU{{ model.plural_name }}Fetcher

from bambou import NURESTFetcher


class NU{{ model.plural_name }}Fetcher(NURESTFetcher):
    """ Represents a NU{{ model.plural_name }} fetcher """

    @classmethod
    def managed_class(cls):
        """ This fetcher manages NU{{ model.name }} objects

            Returns:
                Returns the NU{{ model.name }} class
        """

        from .. import NU{{ model.name }}
        return NU{{ model.name }}

