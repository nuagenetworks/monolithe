# -*- coding: utf-8 -*-

from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUFloatingIpsFetcher
from ..fetchers import NUStaticRoutesFetcher
from ..fetchers import NUSubNetworksFetcher
from ..fetchers import NUVPNConnectsFetcher
from ..fetchers import NUZonesFetcher
from ..fetchers import NUEgressACLTemplatesFetcher
from ..fetchers import NUIngressACLTemplatesFetcher
from ..fetchers import NUIngressAdvancedForwardingTemplatesFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVirtualMachinesFetcher
from ..fetchers import NUBridgeInterfacesFetcher
from ..fetchers import NUHostInterfacesFetcher
from ..fetchers import NUPolicyGroupsFetcher
from ..fetchers import NUVPortsFetcher
from ..fetchers import NUVPortTagsFetcher

from restnuage import NURESTObject


class NUDomain(NURESTObject):
    """ Represents a Domain object """

    def __init__(self):
        """ Initializing object """

        super(NUDomain, self).__init__()

        # Read/Write Attributes
        
        self.application_deployment_policy = None
        self.template_id = None
        self.customer_id = None
        self.description = None
        self.tunnel_type = None
        self.multicast = None
        self.label_id = None
        self.maintenance_mode = None
        self.associated_multicast_channel_map_id = None
        self.name = None
        self.route_distinguisher = None
        self.route_target = None
        self.service_id = None
        
        self.expose_attribute(local_name=u"application_deployment_policy", remote_name=u"applicationDeploymentPolicy", attribute_type=str)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str)
        self.expose_attribute(local_name=u"customer_id", remote_name=u"customerID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"tunnel_type", remote_name=u"tunnelType", attribute_type=str)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str)
        self.expose_attribute(local_name=u"label_id", remote_name=u"labelID", attribute_type=str)
        self.expose_attribute(local_name=u"maintenance_mode", remote_name=u"maintenanceMode", attribute_type=str)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"route_distinguisher", remote_name=u"routeDistinguisher", attribute_type=str)
        self.expose_attribute(local_name=u"route_target", remote_name=u"routeTarget", attribute_type=str)
        self.expose_attribute(local_name=u"service_id", remote_name=u"serviceID", attribute_type=str)

        # Fetchers
        
        self.eventlogs = []
        self._eventlogs_fetcher = NUEventLogsFetcher.fetcher_with_entity(entity=self, local_name=u"eventlogs")
        
        self.dhcpoptions = []
        self._dhcpoptions_fetcher = NUDHCPOptionsFetcher.fetcher_with_entity(entity=self, local_name=u"dhcpoptions")
        
        self.floatingips = []
        self._floatingips_fetcher = NUFloatingIpsFetcher.fetcher_with_entity(entity=self, local_name=u"floatingips")
        
        self.staticroutes = []
        self._staticroutes_fetcher = NUStaticRoutesFetcher.fetcher_with_entity(entity=self, local_name=u"staticroutes")
        
        self.subnets = []
        self._subnets_fetcher = NUSubNetworksFetcher.fetcher_with_entity(entity=self, local_name=u"subnets")
        
        self.vpnconnections = []
        self._vpnconnections_fetcher = NUVPNConnectsFetcher.fetcher_with_entity(entity=self, local_name=u"vpnconnections")
        
        self.zones = []
        self._zones_fetcher = NUZonesFetcher.fetcher_with_entity(entity=self, local_name=u"zones")
        
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
        
        self.vports = []
        self._vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u"vports")
        
        self.redirectiontargets = []
        self._redirectiontargets_fetcher = NUVPortTagsFetcher.fetcher_with_entity(entity=self, local_name=u"redirectiontargets")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"domain"

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
    
    def create_floatingip(self, floatingip, async=False, callback=None):
        """ Create a floatingip
            :param floatingip: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=floatingip, async=async, callback=callback)

    def delete_floatingip(self, floatingip, async=False, callback=None):
        """ Removes a floatingip
            :param floatingip: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=floatingip, async=async, callback=callback)

    def fetch_floatingips(self, filter=None, page=None, order_by=None):
        """ Fetch FloatingIps """

        if order_by:
            self._floatingips_fetcher.order_by = order_by

        return self._floatingips_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_zone(self, zone, async=False, callback=None):
        """ Create a zone
            :param zone: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=zone, async=async, callback=callback)

    def delete_zone(self, zone, async=False, callback=None):
        """ Removes a zone
            :param zone: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=zone, async=async, callback=callback)

    def fetch_zones(self, filter=None, page=None, order_by=None):
        """ Fetch Zones """

        if order_by:
            self._zones_fetcher.order_by = order_by

        return self._zones_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    