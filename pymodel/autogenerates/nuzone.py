# -*- coding: utf-8 -*-

from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUSubNetworksFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUStatisticssFetcher
from ..fetchers import NUStatisticsPoliciesFetcher
from ..fetchers import NUTCAsFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVirtualMachinesFetcher

from bambou import NURESTObject


class NUZone(NURESTObject):
    """ Represents a Zone object """

    def __init__(self):
        """ Initializing object """

        super(NUZone, self).__init__()

        # Read/Write Attributes

        self.address = None
        self.associated_application_id = None
        self.associated_application_object_id = None
        self.associated_application_object_type = None
        self.template_id = None
        self.description = None
        self.ip_type = None
        self.maintenance_mode = None
        self.name = None
        self.netmask = None
        self.number_of_hosts_in_subnets = None
        self.public_zone = None
        self.multicast = None
        self.associated_multicast_channel_map_id = None

        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_id", remote_name=u"associatedApplicationID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_object_id", remote_name=u"associatedApplicationObjectID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_object_type", remote_name=u"associatedApplicationObjectType", attribute_type=str)
        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str)
        self.expose_attribute(local_name=u"maintenance_mode", remote_name=u"maintenanceMode", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"number_of_hosts_in_subnets", remote_name=u"numberOfHostsInSubnets", attribute_type=int)
        self.expose_attribute(local_name=u"public_zone", remote_name=u"publicZone", attribute_type=bool)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str)

        # Fetchers

        self.dhcpoptions = []
        self._dhcpoptions_fetcher = NUDHCPOptionsFetcher.fetcher_with_entity(entity=self, local_name=u"dhcpoptions")

        self.subnets = []
        self._subnets_fetcher = NUSubNetworksFetcher.fetcher_with_entity(entity=self, local_name=u"subnets")

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


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"zone"

    # REST methods

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
