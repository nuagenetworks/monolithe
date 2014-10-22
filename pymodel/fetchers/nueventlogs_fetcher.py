# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUEventLogsFetcher(NURESTFetcher):
    """ EventLog fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUEventLog
        return NUEventLog