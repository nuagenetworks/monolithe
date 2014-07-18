# -*- coding: utf-8 -*-

from ..fetchers import NUFlowsFetcher
from ..fetchers import NUTiersFetcher

from restnuage import NURESTObject


class NUApp(NURESTObject):
    """ Represents a App object """

    def __init__(self):
        """ Initializing object """

        super(NUApp, self).__init__()

        # Read/Write Attributes
        
        self.associated_domain_id = None
        self.associated_domain_type = None
        self.associated_network_object_id = None
        self.associated_network_object_type = None
        self.description = None
        self.name = None
        
        self.expose_attribute(local_name=u"associated_domain_id", remote_name=u"associatedDomainID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_domain_type", remote_name=u"associatedDomainType", attribute_type=str)
        self.expose_attribute(local_name=u"associated_network_object_id", remote_name=u"associatedNetworkObjectID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_network_object_type", remote_name=u"associatedNetworkObjectType", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers
        
        self.flows = []
        self._flows_fetcher = NUFlowsFetcher.fetcher_with_entity(entity=self, local_name=u"flows")
        
        self.tiers = []
        self._tiers_fetcher = NUTiersFetcher.fetcher_with_entity(entity=self, local_name=u"tiers")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"application"

    # REST methods
    
    def create_flow(self, flow, async=False, callback=None):
        """ Create a flow
            :param flow: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=flow, async=async, callback=callback)

    def delete_flow(self, flow, async=False, callback=None):
        """ Removes a flow
            :param flow: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=flow, async=async, callback=callback)

    def fetch_flows(self, filter=None, page=None, order_by=None):
        """ Fetch Flows """

        if order_by:
            self._flows_fetcher.order_by = order_by

        return self._flows_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_tier(self, tier, async=False, callback=None):
        """ Create a tier
            :param tier: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=tier, async=async, callback=callback)

    def delete_tier(self, tier, async=False, callback=None):
        """ Removes a tier
            :param tier: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=tier, async=async, callback=callback)

    def fetch_tiers(self, filter=None, page=None, order_by=None):
        """ Fetch Tiers """

        if order_by:
            self._tiers_fetcher.order_by = order_by

        return self._tiers_fetcher.fetch_matching_entities(filter=filter, page=page)
    