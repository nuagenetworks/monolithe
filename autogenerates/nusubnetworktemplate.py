# -*- coding: utf-8 -*-

from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUAddressRangesFetcher
from ..fetchers import NUSubNetworksFetcher
from ..fetchers import NUQosPrimitivesFetcher

from restnuage import NURESTObject


class NUSubNetworkTemplate(NURESTObject):
    """ Represents a SubNetworkTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUSubNetworkTemplate, self).__init__()

        # Read/Write Attributes
        
        self.address = None
        self.description = None
        self.gateway = None
        self.ip_type = None
        self.name = None
        self.netmask = None
        self.multicast = None
        self.associated_multicast_channel_map_id = None
        self.proxy_arp = None
        self.split_subnet = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str)
        self.expose_attribute(local_name=u"proxy_arp", remote_name=u"proxyARP", attribute_type=bool)
        self.expose_attribute(local_name=u"split_subnet", remote_name=u"splitSubnet", attribute_type=bool)

        # Fetchers
        
        self.eventlogs = []
        self._eventlogs_fetcher = NUEventLogsFetcher.fetcher_with_entity(entity=self, local_name=u"eventlogs")
        
        self.addressranges = []
        self._addressranges_fetcher = NUAddressRangesFetcher.fetcher_with_entity(entity=self, local_name=u"addressranges")
        
        self.subnets = []
        self._subnets_fetcher = NUSubNetworksFetcher.fetcher_with_entity(entity=self, local_name=u"subnets")
        
        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"subnettemplate"

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
    
    def create_addressrange(self, addressrange, async=False, callback=None):
        """ Create a addressrange
            :param addressrange: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=addressrange, async=async, callback=callback)

    def delete_addressrange(self, addressrange, async=False, callback=None):
        """ Removes a addressrange
            :param addressrange: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=addressrange, async=async, callback=callback)

    def fetch_addressranges(self, filter=None, page=None, order_by=None):
        """ Fetch AddressRanges """

        if order_by:
            self._addressranges_fetcher.order_by = order_by

        return self._addressranges_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_subnet(self, subnet, async=False, callback=None):
        """ Create a subnet
            :param subnet: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=subnet, async=async, callback=callback)

    def delete_subnet(self, subnet, async=False, callback=None):
        """ Removes a subnet
            :param subnet: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=subnet, async=async, callback=callback)

    def fetch_subnets(self, filter=None, page=None, order_by=None):
        """ Fetch SubNetworks """

        if order_by:
            self._subnets_fetcher.order_by = order_by

        return self._subnets_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_qo(self, qo, async=False, callback=None):
        """ Create a qo
            :param qo: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=qo, async=async, callback=callback)

    def delete_qo(self, qo, async=False, callback=None):
        """ Removes a qo
            :param qo: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=qo, async=async, callback=callback)

    def fetch_qos(self, filter=None, page=None, order_by=None):
        """ Fetch QosPrimitives """

        if order_by:
            self._qos_fetcher.order_by = order_by

        return self._qos_fetcher.fetch_matching_entities(filter=filter, page=page)
    