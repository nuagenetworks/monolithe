# -*- coding:utf-8 -*-

from .fetchers import NUSubnetTemplatesFetcher
from restnuage.nurest_object import NURESTObject


class NUZoneTemplate(NURESTObject):
    """ Defines a zone template """

    def __init__(self):
        """ Initialize a new object """

        super(NUZoneTemplate, self).__init__()

        # Read/Write Attributes
        self.address = None
        self.associated_multicast_channel_map_id = None
        self.cidr = None
        self.description = None
        self.is_multicast = bool()
        self.is_public_zone = bool()
        self.name = None
        self.netmask = None
        self.number_of_hosts_in_subnets = 0

        self.qoss = []
        self.subnet_templates = []
        self.virtual_machines = []

        self.expose_attribute(local_name=u'address', attribute_type=str)
        self.expose_attribute(local_name=u'associated_multicast_channel_map_id', remote_name=u'associatedMulticastChannelMapID', attribute_type=str)
        self.expose_attribute(local_name=u'cidr', remote_name=u'CIDR', attribute_type=str)
        self.expose_attribute(local_name=u'description', attribute_type=str)
        self.expose_attribute(local_name=u'is_multicast', remote_name=u'multicast', attribute_type=bool)
        self.expose_attribute(local_name=u'is_public_zone', remote_name=u'publicZone', attribute_type=bool)
        self.expose_attribute(local_name=u'name', attribute_type=str)
        self.expose_attribute(local_name=u'netmask', attribute_type=str)
        self.expose_attribute(local_name=u'number_of_hosts_in_subnets', remote_name=u'numberOfHostsInSubnets', attribute_type=str)

        # Read-only attributes

        # Fetchers
        # TODO: Write fetchers here
        # self.qoss_fetcher = NUQOSsFetcher.fetcher_with_entity(entity=self, local_name=u'quoss')
        self.subnet_templates_fetcher = NUSubnetTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u'subnet_templates')
        # self.virtual_machines_fetcher = NUVMsFetcher.fetcher_with_entity(entity=self, local_name=u'virtual_machines')

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"zonetemplate"

    # REST methods

    def create_subnet_template(self, subnet_template, async=False, callback=None):
        """ Create a subnet template
            :param subnet_template: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=subnet_template, async=async, callback=callback)

    def delete_subnet_template(self, subnet_template, async=False, callback=None):
        """ Removes a subnet template
            :param subnet_template: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=subnet_template, async=async, callback=callback)
