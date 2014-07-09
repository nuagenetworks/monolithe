# -*- coding:utf-8 -*-

from .fetchers import NUSubnetsFetcher
from .nuzonetemplate import NUZoneTemplate


class NUZone(NUZoneTemplate):
    """ Defines a zone """

    def __init__(self):
        """ Initialize a new object """

        super(NUZone, self).__init__()

        # Read/Write Attributes
        self.associated_application_id = None
        self.associated_application_object_id = None
        self.associated_application_object_type = None
        self.maintenance_mode = None
        self.template_id = None

        self.dhcp_options = []
        self.permissions = []
        self.statistics = []
        self.statistic_policies = []
        self.subnets = []
        self.tcas = []

        self.expose_attribute(local_name=u'associated_application_id', remote_name=u'associatedApplicationObjectID', attribute_type=str)
        self.expose_attribute(local_name=u'associated_application_object_id', remote_name=u'associatedApplicationObjectID', attribute_type=str)
        self.expose_attribute(local_name=u'associated_application_object_type', remote_name=u'associatedApplicationObjectType', attribute_type=str)
        self.expose_attribute(local_name=u'maintenance_mode', remote_name=u'maintenanceMode', attribute_type=str)
        self.expose_attribute(local_name=u'template_id', remote_name=u'templateID', attribute_type=str)

        # Read-only attributes

        # Fetchers
        # TODO: Write fetchers here
        # self.dhcp_options_fetcher = NUDHCPOptionsFetcher.fetcher_with_entity(entity=self, local_name=u'dhcp_options')
        # self.permissions_fetcher = NUPermissionsFetcher.fetcher_with_entity(entity=self, local_name=u'permissions')
        self.subnets_fetcher = NUSubnetsFetcher.fetcher_with_entity(entity=self, local_name=u'subnets')

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"zone"

    # REST methods

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
