# -*- coding: utf-8 -*-

from bambou import NURESTFetcher


class NUVPortMirrorsFetcher(NURESTFetcher):
    """ VPortMirror fetcher """

    @classmethod
    def managed_class(cls):
        """ Managed class """

        from .. import NUVPortMirror
        return NUVPortMirror