# -*- coding:utf-8 -*-

from restnuage.nurest_object import NURESTObject

NUVPORT_TYPEVM = u"VM"
NUVPORT_TYPEHOST = u"HOST"
NUVPORT_TYPEBRIDGE = u"BRIDGE"
NUVPORT_ADDRESSSPOOFINGINHERITED = u"INHERITED"
NUVPORT_ADDRESSSPOOFINGENABLED = u"ENABLED"
NUVPORT_ADDRESSSPOOFINGDISABLED = u"DISABLED"
NUVPORT_OPERATIONALSTATEINIT = u"INIT"
NUVPORT_OPERATIONALSTATEUNRESOLVED = u"DOWN"
NUVPORT_OPERATIONALSTATERESOLVED = u"UP"


class NUVPort(NURESTObject):
    """ Defines a vport """

    def __init__(self):
        """ Initialize a new object """

        super(NUVPort, self).__init__()

        # Read/Write Attributes
        self.address_spoofing = NUVPORT_ADDRESSSPOOFINGINHERITED
        self.associated_application_id = None
        self.associated_application_object_id = None
        self.associated_application_object_type = None
        self.associated_floating_ip_id = None
        self.associated_multicast_channel_map_id = None
        self.description = None
        self.domain_id = None
        self.gateway_ip = None
        self.gateway_port_name = None
        self.has_attached_interfaces = bool()
        self.is_active = bool()
        self.is_multicast = u"INHERITED"  # TODO: NUMulticastChannelMapINHERITED
        self.name = None
        self.operational_state = NUVPORT_OPERATIONALSTATEINIT
        self.type = NUVPORT_TYPEVM
        self.vlan = None
        self.vlan_id = None
        self.vrs_id = None
        self.zone_id = None

        self.alarms = []
        self.birdge_interfaces = []
        self.host_interfaces = []
        self.policy_groups = []
        self.quoss = []
        self.redirection_targets = []
        self.statistics = []
        self.statistics_policies = []
        self.tcas = []
        self.virtual_machines = []
        self.vm_interfaces = []
        self.vport_mirrors = []

        self.expose_attribute(local_name=u'address_spoofing', remote_name=u"addressSpoofing", attribute_type=str)
        self.expose_attribute(local_name=u'associated_application_id', remote_name=u'associatedApplicationObjectID', attribute_type=str)
        self.expose_attribute(local_name=u'associated_application_id', remote_name=u'associatedApplicationObjectID', attribute_type=str)
        self.expose_attribute(local_name=u'associated_application_object_id', remote_name=u'associatedApplicationObjectID', attribute_type=str)
        self.expose_attribute(local_name=u'associated_application_object_type', remote_name=u'associatedApplicationObjectType', attribute_type=str)
        self.expose_attribute(local_name=u'associated_floating_ip_id', remote_name=u"associatedFloatingIPID", attribute_type=str)
        self.expose_attribute(local_name=u'associated_multicast_channel_map_id', remote_name=u"associatedMulticastChannelMapID", attribute_type=str)
        self.expose_attribute(local_name=u'description', attribute_type=str)
        self.expose_attribute(local_name=u'has_attached_interfaces', remote_name=u"hasAttachedInterfaces", attribute_type=str)
        self.expose_attribute(local_name=u'is_multicast', remote_name=u"multicast", attribute_type=str)
        self.expose_attribute(local_name=u'maintenance_mode', remote_name=u'maintenanceMode', attribute_type=str)
        self.expose_attribute(local_name=u'name', attribute_type=str)
        self.expose_attribute(local_name=u'operational_state', remote_name=u"operationalState", attribute_type=str)
        self.expose_attribute(local_name=u'template_id', remote_name=u'templateID', attribute_type=str)
        self.expose_attribute(local_name=u'type', attribute_type=str)
        self.expose_attribute(local_name=u'vlan_id', remote_name=u"VLANID", attribute_type=str)
        self.expose_attribute(local_name=u'vrs_id', remote_name=u"VRSID", attribute_type=str)

        # Read-only attributes

        # Fetchers
        # TODO: Write fetchers here

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"vport"

    # REST methods
