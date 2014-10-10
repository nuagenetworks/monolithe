# -*- coding: utf-8 -*-

from ..fetchers import NUMultiCastRangesFetcher

from restnuage import NURESTObject


class NUMultiCastChannelMap(NURESTObject):
    """ Represents a MultiCastChannelMap object """

    def __init__(self):
        """ Initializing object """

        super(NUMultiCastChannelMap, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.name = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers
        
        self.multicastranges = []
        self._multicastranges_fetcher = NUMultiCastRangesFetcher.fetcher_with_entity(entity=self, local_name=u"multicastranges")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"multicastchannelmap"

    # REST methods
    
    def create_multicastrange(self, multicastrange, async=False, callback=None):
        """ Create a multicastrange
            :param multicastrange: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=multicastrange, async=async, callback=callback)

    def delete_multicastrange(self, multicastrange, async=False, callback=None):
        """ Removes a multicastrange
            :param multicastrange: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=multicastrange, async=async, callback=callback)

    def fetch_multicastranges(self, filter=None, page=None, order_by=None):
        """ Fetch MultiCastRanges """

        if order_by:
            self._multicastranges_fetcher.order_by = order_by

        return self._multicastranges_fetcher.fetch_matching_entities(filter=filter, page=page)
    