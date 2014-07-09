# -*- coding:utf-8 -*-

from .fetchers import NUVPortsFetcher
from .nusubnettemplate import NUSubnetTemplate


class NUSubnet(NUSubnetTemplate):
    """ Defines a subnet """

    def __init__(self):
        """ Initialize a new object """

        super(NUSubnet, self).__init__()

        # Read/Write Attributes
        self.associated_application_id = None
        self.associated_application_object_id = None
        self.associated_application_object_type = None
        self.associated_shared_network_resource_id = None
        self.maintenance_mode = None
        self.template_id = None

        self.dhcp_options = []
        self.permissions = []
        self.statistics = []
        self.statistic_policies = []
        self.vpn_connections = []
        self.vports = []
        self.tcas = []

        self.expose_attribute(local_name=u'associated_application_id', remote_name=u'associatedApplicationObjectID', attribute_type=str)
        self.expose_attribute(local_name=u'associated_application_object_id', remote_name=u'associatedApplicationObjectID', attribute_type=str)
        self.expose_attribute(local_name=u'associated_application_object_type', remote_name=u'associatedApplicationObjectType', attribute_type=str)
        self.expose_attribute(local_name=u'associated_shared_network_resource_id', remote_name=u'associatedSharedNetworkResourceID', attribute_type=str)
        self.expose_attribute(local_name=u'maintenance_mode', remote_name=u'maintenanceMode', attribute_type=str)
        self.expose_attribute(local_name=u'template_id', remote_name=u'templateID', attribute_type=str)

        # Read-only attributes

        # Fetchers
        # TODO: Write fetchers here
        self.vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u'vports')

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"subnet"

    # REST methods

    def create_vport(self, vport, async=False, callback=None):
        """ Create a vport
            :param vport: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vport, async=async, callback=callback)

    def delete_vport(self, vport, async=False, callback=None):
        """ Removes a subnet
            :param vport: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vport, async=async, callback=callback)
