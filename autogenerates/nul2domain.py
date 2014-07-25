# -*- coding: utf-8 -*-

from ..fetchers import NUMetadatasFetcher
from ..fetchers import NUAddressRangesFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUStaticRoutesFetcher
from ..fetchers import NUVPNConnectsFetcher
from ..fetchers import NUEgressACLTemplatesFetcher
from ..fetchers import NUIngressACLTemplatesFetcher
from ..fetchers import NUIngressAdvancedForwardingTemplatesFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUVirtualMachinesFetcher
from ..fetchers import NUBridgeInterfacesFetcher
from ..fetchers import NUHostInterfacesFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUVPortsFetcher
from ..fetchers import NUVPortTagsFetcher

from restnuage import NURESTObject


class NUL2Domain(NURESTObject):
    """ Represents a L2Domain object """

    def __init__(self):
        """ Initializing object """

        super(NUL2Domain, self).__init__()

        # Read/Write Attributes
        
        self.address = None
        self.associated_shared_network_resource_id = None
        self.template_id = None
        self.description = None
        self.dhcp_managed = None
        self.gateway = None
        self.ip_type = None
        self.maintenance_mode = None
        self.name = None
        self.netmask = None
        self.route_distinguisher = None
        self.route_target = None
        self.service_id = None
        self.vn_id = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"associated_shared_network_resource_id", remote_name=u"associatedSharedNetworkResourceID", attribute_type=str)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"dhcp_managed", remote_name=u"DHCPManaged", attribute_type=bool)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str)
        self.expose_attribute(local_name=u"maintenance_mode", remote_name=u"maintenanceMode", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"route_distinguisher", remote_name=u"routeDistinguisher", attribute_type=str)
        self.expose_attribute(local_name=u"route_target", remote_name=u"routeTarget", attribute_type=str)
        self.expose_attribute(local_name=u"service_id", remote_name=u"serviceID", attribute_type=str)
        self.expose_attribute(local_name=u"vn_id", remote_name=u"vnId", attribute_type=str)

        # Fetchers
        
        self.metadata = []
        self._metadata_fetcher = NUMetadatasFetcher.fetcher_with_entity(entity=self, local_name=u"metadata")
        
        self.addressranges = []
        self._addressranges_fetcher = NUAddressRangesFetcher.fetcher_with_entity(entity=self, local_name=u"addressranges")
        
        self.dhcpoptions = []
        self._dhcpoptions_fetcher = NUDHCPOptionsFetcher.fetcher_with_entity(entity=self, local_name=u"dhcpoptions")
        
        self.staticroutes = []
        self._staticroutes_fetcher = NUStaticRoutesFetcher.fetcher_with_entity(entity=self, local_name=u"staticroutes")
        
        self.vpnconnections = []
        self._vpnconnections_fetcher = NUVPNConnectsFetcher.fetcher_with_entity(entity=self, local_name=u"vpnconnections")
        
        self.egressacltemplates = []
        self._egressacltemplates_fetcher = NUEgressACLTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"egressacltemplates")
        
        self.ingressacltemplates = []
        self._ingressacltemplates_fetcher = NUIngressACLTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"ingressacltemplates")
        
        self.ingressadvfwdtemplates = []
        self._ingressadvfwdtemplates_fetcher = NUIngressAdvancedForwardingTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"ingressadvfwdtemplates")
        
        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        
        self.statistics = []
        self._statistics_fetcher = NUStatisticssFetcher.fetcher_with_entity(entity=self, local_name=u"statistics")
        
        self.statisticspolicies = []
        self._statisticspolicies_fetcher = NUStatisticsPoliciesFetcher.fetcher_with_entity(entity=self, local_name=u"statisticspolicies")
        
        self.tcas = []
        self._tcas_fetcher = NUTCAsFetcher.fetcher_with_entity(entity=self, local_name=u"tcas")
        
        self.groups = []
        self._groups_fetcher = NUGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"groups")
        
        self.permissions = []
        self._permissions_fetcher = NUPermittedActionsFetcher.fetcher_with_entity(entity=self, local_name=u"permissions")
        
        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")
        
        self.bridgeinterfaces = []
        self._bridgeinterfaces_fetcher = NUBridgeInterfacesFetcher.fetcher_with_entity(entity=self, local_name=u"bridgeinterfaces")
        
        self.hostinterfaces = []
        self._hostinterfaces_fetcher = NUHostInterfacesFetcher.fetcher_with_entity(entity=self, local_name=u"hostinterfaces")
        
        self.policygroups = []
        self._policygroups_fetcher = NUPolicyGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"policygroups")
        
        self.vports = []
        self._vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u"vports")
        
        self.redirectiontargets = []
        self._redirectiontargets_fetcher = NUVPortTagsFetcher.fetcher_with_entity(entity=self, local_name=u"redirectiontargets")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"l2domain"

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
    
    def create_vpnconnection(self, vpnconnection, async=False, callback=None):
        """ Create a vpnconnection
            :param vpnconnection: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vpnconnection, async=async, callback=callback)

    def delete_vpnconnection(self, vpnconnection, async=False, callback=None):
        """ Removes a vpnconnection
            :param vpnconnection: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vpnconnection, async=async, callback=callback)

    def fetch_vpnconnections(self, filter=None, page=None, order_by=None):
        """ Fetch VPNConnects """

        if order_by:
            self._vpnconnections_fetcher.order_by = order_by

        return self._vpnconnections_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_egressacltemplate(self, egressacltemplate, async=False, callback=None):
        """ Create a egressacltemplate
            :param egressacltemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=egressacltemplate, async=async, callback=callback)

    def delete_egressacltemplate(self, egressacltemplate, async=False, callback=None):
        """ Removes a egressacltemplate
            :param egressacltemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=egressacltemplate, async=async, callback=callback)

    def fetch_egressacltemplates(self, filter=None, page=None, order_by=None):
        """ Fetch EgressACLTemplates """

        if order_by:
            self._egressacltemplates_fetcher.order_by = order_by

        return self._egressacltemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_ingressacltemplate(self, ingressacltemplate, async=False, callback=None):
        """ Create a ingressacltemplate
            :param ingressacltemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ingressacltemplate, async=async, callback=callback)

    def delete_ingressacltemplate(self, ingressacltemplate, async=False, callback=None):
        """ Removes a ingressacltemplate
            :param ingressacltemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ingressacltemplate, async=async, callback=callback)

    def fetch_ingressacltemplates(self, filter=None, page=None, order_by=None):
        """ Fetch IngressACLTemplates """

        if order_by:
            self._ingressacltemplates_fetcher.order_by = order_by

        return self._ingressacltemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_ingressadvfwdtemplate(self, ingressadvfwdtemplate, async=False, callback=None):
        """ Create a ingressadvfwdtemplate
            :param ingressadvfwdtemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ingressadvfwdtemplate, async=async, callback=callback)

    def delete_ingressadvfwdtemplate(self, ingressadvfwdtemplate, async=False, callback=None):
        """ Removes a ingressadvfwdtemplate
            :param ingressadvfwdtemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ingressadvfwdtemplate, async=async, callback=callback)

    def fetch_ingressadvfwdtemplates(self, filter=None, page=None, order_by=None):
        """ Fetch IngressAdvancedForwardingTemplates """

        if order_by:
            self._ingressadvfwdtemplates_fetcher.order_by = order_by

        return self._ingressadvfwdtemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_group(self, group, async=False, callback=None):
        """ Create a group
            :param group: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=group, async=async, callback=callback)

    def delete_group(self, group, async=False, callback=None):
        """ Removes a group
            :param group: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=group, async=async, callback=callback)

    def fetch_groups(self, filter=None, page=None, order_by=None):
        """ Fetch Groups """

        if order_by:
            self._groups_fetcher.order_by = order_by

        return self._groups_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_permission(self, permission, async=False, callback=None):
        """ Create a permission
            :param permission: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=permission, async=async, callback=callback)

    def delete_permission(self, permission, async=False, callback=None):
        """ Removes a permission
            :param permission: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=permission, async=async, callback=callback)

    def fetch_permissions(self, filter=None, page=None, order_by=None):
        """ Fetch PermittedActions """

        if order_by:
            self._permissions_fetcher.order_by = order_by

        return self._permissions_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    