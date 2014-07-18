# -*- coding: utf-8 -*-

from ..fetchers import NUVPortsFetcher

from restnuage import NURESTObject


class NUPolicyGroup(NURESTObject):
    """ Represents a PolicyGroup object """

    def __init__(self):
        """ Initializing object """

        super(NUPolicyGroup, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.evpn_community_tag = None
        self.name = None
        self.template_id = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"evpn_community_tag", remote_name=u"EVPNCommunityTag", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str)

        # Fetchers
        
        self.vports = []
        self._vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u"vports")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"policygroup"

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
    