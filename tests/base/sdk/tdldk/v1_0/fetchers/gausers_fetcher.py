# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#

from bambou import NURESTFetcher


class GAUsersFetcher(NURESTFetcher):
    """ Represents a GAUsers fetcher

        Notes:
            This fetcher enables to fetch GAUser objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return GAUser class that is managed.

            Returns:
                .GAUser: the managed class
        """

        from .. import GAUser
        return GAUser

    