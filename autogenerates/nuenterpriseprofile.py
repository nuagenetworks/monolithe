# -*- coding: utf-8 -*-

from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUMultiCastChannelMapsFetcher
from ..fetchers import NUEnterprisesFetcher

from restnuage import NURESTObject


class NUEnterpriseProfile(NURESTObject):
    """ Represents a EnterpriseProfile object """

    def __init__(self):
        """ Initializing object """

        super(NUEnterpriseProfile, self).__init__()

        # Read/Write Attributes
        
        self.allow_advanced_qos_configuration = None
        self.allowed_forwarding_classes = None
        self.allow_gateway_management = None
        self.allow_trusted_forwarding_class = None
        self.description = None
        self.floating_i_ps_quota = None
        self.name = None
        
        self.expose_attribute(local_name=u"allow_advanced_qos_configuration", remote_name=u"allowAdvancedQOSConfiguration", attribute_type=bool)
        self.expose_attribute(local_name=u"allowed_forwarding_classes", remote_name=u"allowedForwardingClasses", attribute_type=str)
        self.expose_attribute(local_name=u"allow_gateway_management", remote_name=u"allowGatewayManagement", attribute_type=bool)
        self.expose_attribute(local_name=u"allow_trusted_forwarding_class", remote_name=u"allowTrustedForwardingClass", attribute_type=bool)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"floating_i_ps_quota", remote_name=u"floatingIPsQuota", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers
        
        self.eventlogs = []
        self._eventlogs_fetcher = NUEventLogsFetcher.fetcher_with_entity(entity=self, local_name=u"eventlogs")
        
        self.multicastchannelmaps = []
        self._multicastchannelmaps_fetcher = NUMultiCastChannelMapsFetcher.fetcher_with_entity(entity=self, local_name=u"multicastchannelmaps")
        
        self.enterprises = []
        self._enterprises_fetcher = NUEnterprisesFetcher.fetcher_with_entity(entity=self, local_name=u"enterprises")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"enterpriseprofile"

    # REST methods
    
    def create_eventlog(self, eventlog, async=False, callback=None):
        """ Create a eventlog
            :param eventlog: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=eventlog, async=async, callback=callback)

    def delete_eventlog(self, eventlog, async=False, callback=None):
        """ Removes a eventlog
            :param eventlog: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=eventlog, async=async, callback=callback)

    def fetch_eventlogs(self, filter=None, page=None, order_by=None):
        """ Fetch EventLogs """

        if order_by:
            self._eventlogs_fetcher.order_by = order_by

        return self._eventlogs_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_multicastchannelmap(self, multicastchannelmap, async=False, callback=None):
        """ Create a multicastchannelmap
            :param multicastchannelmap: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=multicastchannelmap, async=async, callback=callback)

    def delete_multicastchannelmap(self, multicastchannelmap, async=False, callback=None):
        """ Removes a multicastchannelmap
            :param multicastchannelmap: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=multicastchannelmap, async=async, callback=callback)

    def fetch_multicastchannelmaps(self, filter=None, page=None, order_by=None):
        """ Fetch MultiCastChannelMaps """

        if order_by:
            self._multicastchannelmaps_fetcher.order_by = order_by

        return self._multicastchannelmaps_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_enterprise(self, enterprise, async=False, callback=None):
        """ Create a enterprise
            :param enterprise: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=enterprise, async=async, callback=callback)

    def delete_enterprise(self, enterprise, async=False, callback=None):
        """ Removes a enterprise
            :param enterprise: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=enterprise, async=async, callback=callback)

    def fetch_enterprises(self, filter=None, page=None, order_by=None):
        """ Fetch Enterprises """

        if order_by:
            self._enterprises_fetcher.order_by = order_by

        return self._enterprises_fetcher.fetch_matching_entities(filter=filter, page=page)
    