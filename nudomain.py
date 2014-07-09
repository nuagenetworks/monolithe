# -*- coding:utf-8 -*-

from .nudomainbase import NUDomainBase

NUDOMAINTUNNEL_TYPEDEFAULT = u"DC_DEFAULT"
NUDOMAINTUNNEL_TYPEVXLAN = u"VXLAN"
NUDOMAINTUNNEL_TYPEGRE = u"GRE"


class NUDomain(NUDomainBase):
    """ Defines a domain """

    def __init__(self):
        """ Initialize a new object """

        super(NUDomain, self).__init__()

        # Read/Write Attributes
        self.application_deployment_policy = None
        self.customer_id = None
        self.domaine_of_selected_template = bool()
        self.maintenance_mode = None  # TODO: NUMaintenanceModeDisabled
        self.route_distinguisher = None
        self.route_target = None
        self.service_id = None
        self.template_id = None
        self.tunnel_type = NUDOMAINTUNNEL_TYPEDEFAULT

        self.bridge_interfaces = []
        self.dhcp_options = []
        self.floating_ips = []
        self.hosting_interfaces = []
        self.policy_groups = []
        self.redirection_targets = []
        self.static_routes = []
        self.statistics = []
        self.statistics_policies = []
        self.subnets = []
        self.tcas = []
        self.virtual_machines = []
        self.vpn_connections = []
        self.vports = []
        self.vport_tags = []
        self.zones = []

        self.expose_attribute(local_name=u'application_deployment_policy', remote_name=u'applicationDeploymentPolicy', attribute_type=str)
        self.expose_attribute(local_name=u'customer_id', remote_name=u'customerID', attribute_type=str)
        self.expose_attribute(local_name=u'domaine_of_selected_template', remote_name=u'domainOfSelectedTemplate', attribute_type=str)
        self.expose_attribute(local_name=u'maintenance_mode', remote_name=u'maintenanceMode', attribute_type=str)
        self.expose_attribute(local_name=u'route_distinguisher', remote_name=u'routeDistinguisher', attribute_type=str)
        self.expose_attribute(local_name=u'route_target', remote_name=u'routeTarget', attribute_type=str)
        self.expose_attribute(local_name=u'service_id', remote_name=u'serviceID', attribute_type=str)
        self.expose_attribute(local_name=u'template_id', remote_name=u'templateID', attribute_type=str)
        self.expose_attribute(local_name=u'tunnel_type', remote_name=u'tunnelType', attribute_type=str)

        # Fetchers
        # TODO : Write fetchers here

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"domain"

    # REST methods

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
