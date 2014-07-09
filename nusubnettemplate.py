# -*- coding:utf-8 -*-

from restnuage.nurest_object import NURESTObject


class NUSubnetTemplate(NURESTObject):
    """ Defines a subnet template """

    def __init__(self):
        """ Initialize a new object """

        super(NUSubnetTemplate, self).__init__()

        # Read/Write Attributes

        self.address = None
        self.associated_multicast_channel_map_id = None
        self.cidr = None
        self.description = None
        self.gateway = None
        self.ip_type = None
        self.is_multicast = bool()
        self.is_proxy_arp = bool()
        self.is_split_subnet = bool()
        self.max_address = None
        self.min_address = None
        self.name = None
        self.netmask = None

        self.qoss = []
        self.address_ranges = []
        self.virtual_machines = []

        self.expose_attribute(local_name=u'address', attribute_type=str)
        self.expose_attribute(local_name=u'associated_multicast_channel_map_id', remote_name=u'associatedMulticastChannelMapID', attribute_type=str)
        self.expose_attribute(local_name=u'cidr', remote_name=u'CIDR', attribute_type=str)
        self.expose_attribute(local_name=u'description', attribute_type=str)
        self.expose_attribute(local_name=u'gateway', attribute_type=str)
        self.expose_attribute(local_name=u'ip_type', remote_name=u'IPType', attribute_type=str)
        self.expose_attribute(local_name=u'is_multicast', remote_name=u'multicast', attribute_type=bool)
        self.expose_attribute(local_name=u'is_proxy_arp', remote_name=u'proxyARP', attribute_type=bool)
        self.expose_attribute(local_name=u'is_split_subnet', remote_name=u'splitSubnet', attribute_type=bool)
        self.expose_attribute(local_name=u'name', attribute_type=str)
        self.expose_attribute(local_name=u'netmask', attribute_type=str)

        # Read-only attributes

        # Fetchers
        # TODO: Write fetchers here

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"subnettemplate"

    # REST methods
