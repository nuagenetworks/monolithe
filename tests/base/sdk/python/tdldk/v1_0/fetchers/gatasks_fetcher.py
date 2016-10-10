# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#

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

    
    ## Custom methods
    def is_this_test_usesless(self):
        """
        Just an example
        """
        return True
    