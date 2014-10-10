# -*- coding: utf-8 -*-

from ..fetchers import NUFlowForwardingPoliciesFetcher
from ..fetchers import NUFlowSecurityPoliciesFetcher

from restnuage import NURESTObject


class NUFlow(NURESTObject):
    """ Represents a Flow object """

    def __init__(self):
        """ Initializing object """

        super(NUFlow, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.destination_tier_id = None
        self.metadata = None
        self.name = None
        self.origin_tier_id = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"destination_tier_id", remote_name=u"destinationTierID", attribute_type=str)
        self.expose_attribute(local_name=u"metadata", remote_name=u"metadata", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"origin_tier_id", remote_name=u"originTierID", attribute_type=str)

        # Fetchers
        
        self.flowforwardingpolicies = []
        self._flowforwardingpolicies_fetcher = NUFlowForwardingPoliciesFetcher.fetcher_with_entity(entity=self, local_name=u"flowforwardingpolicies")
        
        self.flowsecuritypolicies = []
        self._flowsecuritypolicies_fetcher = NUFlowSecurityPoliciesFetcher.fetcher_with_entity(entity=self, local_name=u"flowsecuritypolicies")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"flow"

    # REST methods
    
    def create_flowforwardingpolicy(self, flowforwardingpolicy, async=False, callback=None):
        """ Create a flowforwardingpolicy
            :param flowforwardingpolicy: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=flowforwardingpolicy, async=async, callback=callback)

    def delete_flowforwardingpolicy(self, flowforwardingpolicy, async=False, callback=None):
        """ Removes a flowforwardingpolicy
            :param flowforwardingpolicy: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=flowforwardingpolicy, async=async, callback=callback)

    def fetch_flowforwardingpolicies(self, filter=None, page=None, order_by=None):
        """ Fetch FlowForwardingPolicies """

        if order_by:
            self._flowforwardingpolicies_fetcher.order_by = order_by

        return self._flowforwardingpolicies_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_flowsecuritypolicy(self, flowsecuritypolicy, async=False, callback=None):
        """ Create a flowsecuritypolicy
            :param flowsecuritypolicy: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=flowsecuritypolicy, async=async, callback=callback)

    def delete_flowsecuritypolicy(self, flowsecuritypolicy, async=False, callback=None):
        """ Removes a flowsecuritypolicy
            :param flowsecuritypolicy: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=flowsecuritypolicy, async=async, callback=callback)

    def fetch_flowsecuritypolicies(self, filter=None, page=None, order_by=None):
        """ Fetch FlowSecurityPolicies """

        if order_by:
            self._flowsecuritypolicies_fetcher.order_by = order_by

        return self._flowsecuritypolicies_fetcher.fetch_matching_entities(filter=filter, page=page)
    