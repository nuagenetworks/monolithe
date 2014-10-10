# -*- coding: utf-8 -*-

from ..fetchers import NUVPortsFetcher
from ..fetchers import NUVirtualIPsFetcher

from restnuage import NURESTObject


class NUVPortTag(NURESTObject):
    """ Represents a VPortTag object """

    def __init__(self):
        """ Initializing object """

        super(NUVPortTag, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.end_point_type = None
        self.esi = None
        self.name = None
        self.redundancy_enabled = None
        self.template_id = None
        self.trigger_type = None
        self.virtual_network_id = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"end_point_type", remote_name=u"endPointType", attribute_type=str)
        self.expose_attribute(local_name=u"esi", remote_name=u"ESI", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"redundancy_enabled", remote_name=u"redundancyEnabled", attribute_type=bool)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str)
        self.expose_attribute(local_name=u"trigger_type", remote_name=u"triggerType", attribute_type=str)
        self.expose_attribute(local_name=u"virtual_network_id", remote_name=u"virtualNetworkID", attribute_type=str)

        # Fetchers
        
        self.vports = []
        self._vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u"vports")
        
        self.virtualips = []
        self._virtualips_fetcher = NUVirtualIPsFetcher.fetcher_with_entity(entity=self, local_name=u"virtualips")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"redirectiontarget"

    # REST methods
    
    def create_vport(self, vport, async=False, callback=None):
        """ Create a vport
            :param vport: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vport, async=async, callback=callback)

    def delete_vport(self, vport, async=False, callback=None):
        """ Removes a vport
            :param vport: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vport, async=async, callback=callback)

    def fetch_vports(self, filter=None, page=None, order_by=None):
        """ Fetch VPorts """

        if order_by:
            self._vports_fetcher.order_by = order_by

        return self._vports_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_virtualip(self, virtualip, async=False, callback=None):
        """ Create a virtualip
            :param virtualip: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=virtualip, async=async, callback=callback)

    def delete_virtualip(self, virtualip, async=False, callback=None):
        """ Removes a virtualip
            :param virtualip: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=virtualip, async=async, callback=callback)

    def fetch_virtualips(self, filter=None, page=None, order_by=None):
        """ Fetch VirtualIPs """

        if order_by:
            self._virtualips_fetcher.order_by = order_by

        return self._virtualips_fetcher.fetch_matching_entities(filter=filter, page=page)
    