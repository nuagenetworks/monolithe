# -*- coding: utf-8 -*-

from ..fetchers import NUAddressRangesFetcher
from ..fetchers import NUDHCPOptionsFetcher
from ..fetchers import NUStaticRoutesFetcher
from ..fetchers import NUVPNConnectsFetcher

from bambou import NURESTObject


class NUSharedNetworkResource(NURESTObject):
    """ Represents a SharedNetworkResource object """

    def __init__(self):
        """ Initializing object """

        super(NUSharedNetworkResource, self).__init__()

        # Read/Write Attributes

        self.address = None
        self.description = None
        self.dhcp_managed = None
        self.shared_resource_parent_id = None
        self.gateway = None
        self.name = None
        self.netmask = None
        self.domain_route_distinguisher = None
        self.domain_route_target = None
        self.type = None
        self.uplink_interface_ip = None
        self.uplink_interface_mac = None
        self.uplink_v_port_name = None
        self.uplink_gw_vlan_attachment_id = None

        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"dhcp_managed", remote_name=u"DHCPManaged", attribute_type=bool)
        self.expose_attribute(local_name=u"shared_resource_parent_id", remote_name=u"sharedResourceParentID", attribute_type=str)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"domain_route_distinguisher", remote_name=u"domainRouteDistinguisher", attribute_type=str)
        self.expose_attribute(local_name=u"domain_route_target", remote_name=u"domainRouteTarget", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)
        self.expose_attribute(local_name=u"uplink_interface_ip", remote_name=u"uplinkInterfaceIP", attribute_type=str)
        self.expose_attribute(local_name=u"uplink_interface_mac", remote_name=u"uplinkInterfaceMAC", attribute_type=str)
        self.expose_attribute(local_name=u"uplink_v_port_name", remote_name=u"uplinkVPortName", attribute_type=str)
        self.expose_attribute(local_name=u"uplink_gw_vlan_attachment_id", remote_name=u"uplinkGWVlanAttachmentID", attribute_type=str)

        # Fetchers

        self.addressranges = []
        self._addressranges_fetcher = NUAddressRangesFetcher.fetcher_with_entity(entity=self, local_name=u"addressranges")

        self.dhcpoptions = []
        self._dhcpoptions_fetcher = NUDHCPOptionsFetcher.fetcher_with_entity(entity=self, local_name=u"dhcpoptions")

        self.staticroutes = []
        self._staticroutes_fetcher = NUStaticRoutesFetcher.fetcher_with_entity(entity=self, local_name=u"staticroutes")

        self.vpnconnections = []
        self._vpnconnections_fetcher = NUVPNConnectsFetcher.fetcher_with_entity(entity=self, local_name=u"vpnconnections")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"sharednetworkresource"

    # REST methods

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
