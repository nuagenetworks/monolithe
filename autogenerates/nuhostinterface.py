# -*- coding: utf-8 -*-

from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUMultiCastChannelMapsFetcher
from ..fetchers import NUStaticRoutesFetcher
from ..fetchers import NUPolicyDecisionsFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUVPortTagsFetcher

from restnuage import NURESTObject


class NUHostInterface(NURESTObject):
    """ Represents a HostInterface object """

    def __init__(self):
        """ Initializing object """

        super(NUHostInterface, self).__init__()

        # Read/Write Attributes
        
        self.ip_address = None
        self.mac = None
        self.name = None
        self.associated_floating_ip_address = None
        self.attached_network_id = None
        self.attached_network_type = None
        self.domain_id = None
        self.domain_name = None
        self.gateway = None
        self.netmask = None
        self.network_name = None
        self.policy_decision_id = None
        self.v_port_id = None
        self.v_port_name = None
        self.zone_id = None
        self.zone_name = None
        
        self.expose_attribute(local_name=u"ip_address", remote_name=u"IPAddress", attribute_type=str)
        self.expose_attribute(local_name=u"mac", remote_name=u"MAC", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"associated_floating_ip_address", remote_name=u"associatedFloatingIPAddress", attribute_type=str)
        self.expose_attribute(local_name=u"attached_network_id", remote_name=u"attachedNetworkID", attribute_type=str)
        self.expose_attribute(local_name=u"attached_network_type", remote_name=u"attachedNetworkType", attribute_type=str)
        self.expose_attribute(local_name=u"domain_id", remote_name=u"domainID", attribute_type=str)
        self.expose_attribute(local_name=u"domain_name", remote_name=u"domainName", attribute_type=str)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"network_name", remote_name=u"networkName", attribute_type=str)
        self.expose_attribute(local_name=u"policy_decision_id", remote_name=u"policyDecisionID", attribute_type=str)
        self.expose_attribute(local_name=u"v_port_id", remote_name=u"VPortID", attribute_type=str)
        self.expose_attribute(local_name=u"v_port_name", remote_name=u"VPortName", attribute_type=str)
        self.expose_attribute(local_name=u"zone_id", remote_name=u"zoneID", attribute_type=str)
        self.expose_attribute(local_name=u"zone_name", remote_name=u"zoneName", attribute_type=str)

        # Fetchers
        
        self.eventlogs = []
        self._eventlogs_fetcher = NUEventLogsFetcher.fetcher_with_entity(entity=self, local_name=u"eventlogs")
        
        self.dhcpoptions = []
        self._dhcpoptions_fetcher = NUDHCPOptionsFetcher.fetcher_with_entity(entity=self, local_name=u"dhcpoptions")
        
        self.multicastchannelmaps = []
        self._multicastchannelmaps_fetcher = NUMultiCastChannelMapsFetcher.fetcher_with_entity(entity=self, local_name=u"multicastchannelmaps")
        
        self.staticroutes = []
        self._staticroutes_fetcher = NUStaticRoutesFetcher.fetcher_with_entity(entity=self, local_name=u"staticroutes")
        
        self.policydecisions = []
        self._policydecisions_fetcher = NUPolicyDecisionsFetcher.fetcher_with_entity(entity=self, local_name=u"policydecisions")
        
        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        
        self.statistics = []
        self._statistics_fetcher = NUStatisticssFetcher.fetcher_with_entity(entity=self, local_name=u"statistics")
        
        self.tcas = []
        self._tcas_fetcher = NUTCAsFetcher.fetcher_with_entity(entity=self, local_name=u"tcas")
        
        self.policygroups = []
        self._policygroups_fetcher = NUPolicyGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"policygroups")
        
        self.redirectiontargets = []
        self._redirectiontargets_fetcher = NUVPortTagsFetcher.fetcher_with_entity(entity=self, local_name=u"redirectiontargets")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"hostinterface"

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
    
    def create_dhcpoption(self, dhcpoption, async=False, callback=None):
        """ Create a dhcpoption
            :param dhcpoption: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=dhcpoption, async=async, callback=callback)

    def delete_dhcpoption(self, dhcpoption, async=False, callback=None):
        """ Removes a dhcpoption
            :param dhcpoption: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=dhcpoption, async=async, callback=callback)

    def fetch_dhcpoptions(self, filter=None, page=None, order_by=None):
        """ Fetch DHCPOptions """

        if order_by:
            self._dhcpoptions_fetcher.order_by = order_by

        return self._dhcpoptions_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_staticroute(self, staticroute, async=False, callback=None):
        """ Create a staticroute
            :param staticroute: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=staticroute, async=async, callback=callback)

    def delete_staticroute(self, staticroute, async=False, callback=None):
        """ Removes a staticroute
            :param staticroute: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=staticroute, async=async, callback=callback)

    def fetch_staticroutes(self, filter=None, page=None, order_by=None):
        """ Fetch StaticRoutes """

        if order_by:
            self._staticroutes_fetcher.order_by = order_by

        return self._staticroutes_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_policydecision(self, policydecision, async=False, callback=None):
        """ Create a policydecision
            :param policydecision: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=policydecision, async=async, callback=callback)

    def delete_policydecision(self, policydecision, async=False, callback=None):
        """ Removes a policydecision
            :param policydecision: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=policydecision, async=async, callback=callback)

    def fetch_policydecisions(self, filter=None, page=None, order_by=None):
        """ Fetch PolicyDecisions """

        if order_by:
            self._policydecisions_fetcher.order_by = order_by

        return self._policydecisions_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_statistic(self, statistic, async=False, callback=None):
        """ Create a statistic
            :param statistic: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=statistic, async=async, callback=callback)

    def delete_statistic(self, statistic, async=False, callback=None):
        """ Removes a statistic
            :param statistic: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=statistic, async=async, callback=callback)

    def fetch_statistics(self, filter=None, page=None, order_by=None):
        """ Fetch Statisticss """

        if order_by:
            self._statistics_fetcher.order_by = order_by

        return self._statistics_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_tca(self, tca, async=False, callback=None):
        """ Create a tca
            :param tca: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=tca, async=async, callback=callback)

    def delete_tca(self, tca, async=False, callback=None):
        """ Removes a tca
            :param tca: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=tca, async=async, callback=callback)

    def fetch_tcas(self, filter=None, page=None, order_by=None):
        """ Fetch TCAs """

        if order_by:
            self._tcas_fetcher.order_by = order_by

        return self._tcas_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_policygroup(self, policygroup, async=False, callback=None):
        """ Create a policygroup
            :param policygroup: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=policygroup, async=async, callback=callback)

    def delete_policygroup(self, policygroup, async=False, callback=None):
        """ Removes a policygroup
            :param policygroup: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=policygroup, async=async, callback=callback)

    def fetch_policygroups(self, filter=None, page=None, order_by=None):
        """ Fetch PolicyGroups """

        if order_by:
            self._policygroups_fetcher.order_by = order_by

        return self._policygroups_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_redirectiontarget(self, redirectiontarget, async=False, callback=None):
        """ Create a redirectiontarget
            :param redirectiontarget: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=redirectiontarget, async=async, callback=callback)

    def delete_redirectiontarget(self, redirectiontarget, async=False, callback=None):
        """ Removes a redirectiontarget
            :param redirectiontarget: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=redirectiontarget, async=async, callback=callback)

    def fetch_redirectiontargets(self, filter=None, page=None, order_by=None):
        """ Fetch VPortTags """

        if order_by:
            self._redirectiontargets_fetcher.order_by = order_by

        return self._redirectiontargets_fetcher.fetch_matching_entities(filter=filter, page=page)
    