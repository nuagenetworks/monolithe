# -*- coding: utf-8 -*-
# TODO

from bambou import NURESTFetcher


class GARootsFetcher(NURESTFetcher):
    """ Represents a GARoots fetcher

        Notes:
            This fetcher enables to fetch GARoot objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return GARoot class that is managed.

            Returns:
                .GARoot: the managed class
        """

        from .. import GARoot
        return GARoot

    