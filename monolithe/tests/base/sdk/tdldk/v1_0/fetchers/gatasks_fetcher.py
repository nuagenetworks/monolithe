# -*- coding: utf-8 -*-
# TODO

from bambou import NURESTFetcher


class GATasksFetcher(NURESTFetcher):
    """ Represents a GATasks fetcher

        Notes:
            This fetcher enables to fetch GATask objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return GATask class that is managed.

            Returns:
                .GATask: the managed class
        """

        from .. import GATask
        return GATask

    