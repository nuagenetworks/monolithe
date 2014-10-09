# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUVRSsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVirtualMachinesFetcher
from ..fetchers import NUBridgeInterfacesFetcher
from ..fetchers import NUHostInterfacesFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUVPortMirrorsFetcher
from ..fetchers import NURedirectionTargetsFetcher

from restnuage import NURESTObject


class NUVPort(NURESTObject):
    """ Represents a VPort object """

    def __init__(self):
        """ Initializing object """

        super(NUVPort, self).__init__()

        # Read/Write Attributes
        
        self.active = None
        self.address_spoofing = None
        self.vlanid = None
        self.description = None
        self.domain_id = None
        self.multicast = None
        self.associated_floating_ipid = None
        self.has_attached_interfaces = None
        self.associated_multicast_channel_map_id = None
        self.multi_nicv_port_id = None
        self.name = None
        self.operational_state = None
        self.system_type = None
        self.type = None
        self.zone_id = None
        
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool)
        self.expose_attribute(local_name=u"address_spoofing", remote_name=u"addressSpoofing", attribute_type=str)
        self.expose_attribute(local_name=u"vlanid", remote_name=u"VLANID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"domain_id", remote_name=u"domainID", attribute_type=str)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str)
        self.expose_attribute(local_name=u"associated_floating_ipid", remote_name=u"associatedFloatingIPID", attribute_type=str)
        self.expose_attribute(local_name=u"has_attached_interfaces", remote_name=u"hasAttachedInterfaces", attribute_type=bool)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str)
        self.expose_attribute(local_name=u"multi_nicv_port_id", remote_name=u"multiNICVPortID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"operational_state", remote_name=u"operationalState", attribute_type=str)
        self.expose_attribute(local_name=u"system_type", remote_name=u"systemType", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)
        self.expose_attribute(local_name=u"zone_id", remote_name=u"zoneID", attribute_type=str)

        # Fetchers
        
        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")
        
        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        
        self.statistics = []
        self._statistics_fetcher = NUStatisticssFetcher.fetcher_with_entity(entity=self, local_name=u"statistics")
        
        self.statisticspolicies = []
        self._statisticspolicies_fetcher = NUStatisticsPoliciesFetcher.fetcher_with_entity(entity=self, local_name=u"statisticspolicies")
        
        self.tcas = []
        self._tcas_fetcher = NUTCAsFetcher.fetcher_with_entity(entity=self, local_name=u"tcas")
        
        self.vrss = []
        self._vrss_fetcher = NUVRSsFetcher.fetcher_with_entity(entity=self, local_name=u"vrss")
        
        self.vminterfaces = []
        self._vminterfaces_fetcher = NUVMInterfacesFetcher.fetcher_with_entity(entity=self, local_name=u"vminterfaces")
        
        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")
        
        self.bridgeinterfaces = []
        self._bridgeinterfaces_fetcher = NUBridgeInterfacesFetcher.fetcher_with_entity(entity=self, local_name=u"bridgeinterfaces")
        
        self.hostinterfaces = []
        self._hostinterfaces_fetcher = NUHostInterfacesFetcher.fetcher_with_entity(entity=self, local_name=u"hostinterfaces")
        
        self.policygroups = []
        self._policygroups_fetcher = NUPolicyGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"policygroups")
        
        self.vportmirrors = []
        self._vportmirrors_fetcher = NUVPortMirrorsFetcher.fetcher_with_entity(entity=self, local_name=u"vportmirrors")
        
        self.redirectiontargets = []
        self._redirectiontargets_fetcher = NURedirectionTargetsFetcher.fetcher_with_entity(entity=self, local_name=u"redirectiontargets")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vport"

    # REST methods
    
    def create_alarm(self, alarm, async=False, callback=None):
        """ Create a alarm
            :param alarm: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=alarm, async=async, callback=callback)

    def delete_alarm(self, alarm, async=False, callback=None):
        """ Removes a alarm
            :param alarm: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=alarm, async=async, callback=callback)

    def fetch_alarms(self, filter=None, page=None, order_by=None):
        """ Fetch Alarms """

        if order_by:
            self._alarms_fetcher.order_by = order_by

        return self._alarms_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_statisticspolicy(self, statisticspolicy, async=False, callback=None):
        """ Create a statisticspolicy
            :param statisticspolicy: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=statisticspolicy, async=async, callback=callback)

    def delete_statisticspolicy(self, statisticspolicy, async=False, callback=None):
        """ Removes a statisticspolicy
            :param statisticspolicy: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=statisticspolicy, async=async, callback=callback)

    def fetch_statisticspolicies(self, filter=None, page=None, order_by=None):
        """ Fetch StatisticsPolicies """

        if order_by:
            self._statisticspolicies_fetcher.order_by = order_by

        return self._statisticspolicies_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_vrs(self, vrs, async=False, callback=None):
        """ Create a vrs
            :param vrs: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vrs, async=async, callback=callback)

    def delete_vrs(self, vrs, async=False, callback=None):
        """ Removes a vrs
            :param vrs: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vrs, async=async, callback=callback)

    def fetch_vrss(self, filter=None, page=None, order_by=None):
        """ Fetch VRSs """

        if order_by:
            self._vrss_fetcher.order_by = order_by

        return self._vrss_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_vminterface(self, vminterface, async=False, callback=None):
        """ Create a vminterface
            :param vminterface: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vminterface, async=async, callback=callback)

    def delete_vminterface(self, vminterface, async=False, callback=None):
        """ Removes a vminterface
            :param vminterface: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vminterface, async=async, callback=callback)

    def fetch_vminterfaces(self, filter=None, page=None, order_by=None):
        """ Fetch VMInterfaces """

        if order_by:
            self._vminterfaces_fetcher.order_by = order_by

        return self._vminterfaces_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_vm(self, vm, async=False, callback=None):
        """ Create a vm
            :param vm: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vm, async=async, callback=callback)

    def delete_vm(self, vm, async=False, callback=None):
        """ Removes a vm
            :param vm: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vm, async=async, callback=callback)

    def fetch_vms(self, filter=None, page=None, order_by=None):
        """ Fetch VirtualMachines """

        if order_by:
            self._vms_fetcher.order_by = order_by

        return self._vms_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_bridgeinterface(self, bridgeinterface, async=False, callback=None):
        """ Create a bridgeinterface
            :param bridgeinterface: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=bridgeinterface, async=async, callback=callback)

    def delete_bridgeinterface(self, bridgeinterface, async=False, callback=None):
        """ Removes a bridgeinterface
            :param bridgeinterface: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=bridgeinterface, async=async, callback=callback)

    def fetch_bridgeinterfaces(self, filter=None, page=None, order_by=None):
        """ Fetch BridgeInterfaces """

        if order_by:
            self._bridgeinterfaces_fetcher.order_by = order_by

        return self._bridgeinterfaces_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_hostinterface(self, hostinterface, async=False, callback=None):
        """ Create a hostinterface
            :param hostinterface: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=hostinterface, async=async, callback=callback)

    def delete_hostinterface(self, hostinterface, async=False, callback=None):
        """ Removes a hostinterface
            :param hostinterface: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=hostinterface, async=async, callback=callback)

    def fetch_hostinterfaces(self, filter=None, page=None, order_by=None):
        """ Fetch HostInterfaces """

        if order_by:
            self._hostinterfaces_fetcher.order_by = order_by

        return self._hostinterfaces_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_vportmirror(self, vportmirror, async=False, callback=None):
        """ Create a vportmirror
            :param vportmirror: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vportmirror, async=async, callback=callback)

    def delete_vportmirror(self, vportmirror, async=False, callback=None):
        """ Removes a vportmirror
            :param vportmirror: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vportmirror, async=async, callback=callback)

    def fetch_vportmirrors(self, filter=None, page=None, order_by=None):
        """ Fetch VPortMirrors """

        if order_by:
            self._vportmirrors_fetcher.order_by = order_by

        return self._vportmirrors_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
        """ Fetch RedirectionTargets """

        if order_by:
            self._redirectiontargets_fetcher.order_by = order_by

        return self._redirectiontargets_fetcher.fetch_matching_entities(filter=filter, page=page)
    