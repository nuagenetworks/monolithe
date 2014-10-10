# -*- coding: utf-8 -*-

from ..fetchers import NUMetadatasFetcher
from ..fetchers import NUAddressRangesFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUIPBindingsFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVMResyncsFetcher
from ..fetchers import NUVirtualMachinesFetcher
from ..fetchers import NUVPortsFetcher

from restnuage import NURESTObject


class NUSubNetwork(NURESTObject):
    """ Represents a SubNetwork object """

    def __init__(self):
        """ Initializing object """

        super(NUSubNetwork, self).__init__()

        # Read/Write Attributes
        
        self.address = None
        self.associated_application_id = None
        self.associated_application_object_id = None
        self.associated_application_object_type = None
        self.associated_shared_network_resource_id = None
        self.template_id = None
        self.description = None
        self.gateway = None
        self.gateway_mac_address = None
        self.ip_type = None
        self.maintenance_mode = None
        self.name = None
        self.netmask = None
        self.route_distinguisher = None
        self.route_target = None
        self.service_id = None
        self.vn_id = None
        self.multicast = None
        self.associated_multicast_channel_map_id = None
        self.nsg_managed = None
        self.proxy_arp = None
        self.split_subnet = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_id", remote_name=u"associatedApplicationID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_object_id", remote_name=u"associatedApplicationObjectID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_object_type", remote_name=u"associatedApplicationObjectType", attribute_type=str)
        self.expose_attribute(local_name=u"associated_shared_network_resource_id", remote_name=u"associatedSharedNetworkResourceID", attribute_type=str)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"gateway_mac_address", remote_name=u"gatewayMACAddress", attribute_type=str)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str)
        self.expose_attribute(local_name=u"maintenance_mode", remote_name=u"maintenanceMode", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"route_distinguisher", remote_name=u"routeDistinguisher", attribute_type=str)
        self.expose_attribute(local_name=u"route_target", remote_name=u"routeTarget", attribute_type=str)
        self.expose_attribute(local_name=u"service_id", remote_name=u"serviceID", attribute_type=str)
        self.expose_attribute(local_name=u"vn_id", remote_name=u"vnId", attribute_type=str)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str)
        self.expose_attribute(local_name=u"nsg_managed", remote_name=u"NSGManaged", attribute_type=bool)
        self.expose_attribute(local_name=u"proxy_arp", remote_name=u"proxyARP", attribute_type=bool)
        self.expose_attribute(local_name=u"split_subnet", remote_name=u"splitSubnet", attribute_type=bool)

        # Fetchers
        
        self.metadata = []
        self._metadata_fetcher = NUMetadatasFetcher.fetcher_with_entity(entity=self, local_name=u"metadata")
        
        self.addressranges = []
        self._addressranges_fetcher = NUAddressRangesFetcher.fetcher_with_entity(entity=self, local_name=u"addressranges")
        
        self.dhcpoptions = []
        self._dhcpoptions_fetcher = NUDHCPOptionsFetcher.fetcher_with_entity(entity=self, local_name=u"dhcpoptions")
        
        self.ipreservations = []
        self._ipreservations_fetcher = NUIPBindingsFetcher.fetcher_with_entity(entity=self, local_name=u"ipreservations")
        
        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        
        self.statistics = []
        self._statistics_fetcher = NUStatisticssFetcher.fetcher_with_entity(entity=self, local_name=u"statistics")
        
        self.statisticspolicies = []
        self._statisticspolicies_fetcher = NUStatisticsPoliciesFetcher.fetcher_with_entity(entity=self, local_name=u"statisticspolicies")
        
        self.tcas = []
        self._tcas_fetcher = NUTCAsFetcher.fetcher_with_entity(entity=self, local_name=u"tcas")
        
        self.vminterfaces = []
        self._vminterfaces_fetcher = NUVMInterfacesFetcher.fetcher_with_entity(entity=self, local_name=u"vminterfaces")
        
        self.resync = []
        self._resync_fetcher = NUVMResyncsFetcher.fetcher_with_entity(entity=self, local_name=u"resync")
        
        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")
        
        self.vports = []
        self._vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u"vports")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"subnet"

    # REST methods
    
    def create_metadat(self, metadat, async=False, callback=None):
        """ Create a metadat
            :param metadat: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=metadat, async=async, callback=callback)

    def delete_metadat(self, metadat, async=False, callback=None):
        """ Removes a metadat
            :param metadat: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=metadat, async=async, callback=callback)

    def fetch_metadata(self, filter=None, page=None, order_by=None):
        """ Fetch Metadatas """

        if order_by:
            self._metadata_fetcher.order_by = order_by

        return self._metadata_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_ipreservation(self, ipreservation, async=False, callback=None):
        """ Create a ipreservation
            :param ipreservation: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ipreservation, async=async, callback=callback)

    def delete_ipreservation(self, ipreservation, async=False, callback=None):
        """ Removes a ipreservation
            :param ipreservation: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ipreservation, async=async, callback=callback)

    def fetch_ipreservations(self, filter=None, page=None, order_by=None):
        """ Fetch IPBindings """

        if order_by:
            self._ipreservations_fetcher.order_by = order_by

        return self._ipreservations_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_resyn(self, resyn, async=False, callback=None):
        """ Create a resyn
            :param resyn: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=resyn, async=async, callback=callback)

    def delete_resyn(self, resyn, async=False, callback=None):
        """ Removes a resyn
            :param resyn: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=resyn, async=async, callback=callback)

    def fetch_resync(self, filter=None, page=None, order_by=None):
        """ Fetch VMResyncs """

        if order_by:
            self._resync_fetcher.order_by = order_by

        return self._resync_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    