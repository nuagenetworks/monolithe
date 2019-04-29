# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#

from bambou2 import NURESTFetcher


class GAMetadatasFetcher(NURESTFetcher):
    """ Represents a GAMetadatas fetcher

        Notes:
            This fetcher enables to fetch GAMetadata objects.

        See:
            bambou2.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return GAMetadata class that is managed.

            Returns:
                .GAMetadata: the managed class
        """

        from .. import GAMetadata
        return GAMetadata

    
