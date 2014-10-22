# -*- coding: utf-8 -*-

from ..fetchers import NUSubNetworkTemplatesFetcher
from ..fetchers import NUQosPrimitivesFetcher

from bambou import NURESTObject


class NUZoneTemplate(NURESTObject):
    """ Represents a ZoneTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUZoneTemplate, self).__init__()

        # Read/Write Attributes

        self.address = None
        self.description = None
        self.ip_type = None
        self.name = None
        self.netmask = None
        self.number_of_hosts_in_subnets = None
        self.public_zone = None
        self.multicast = None
        self.associated_multicast_channel_map_id = None

        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"number_of_hosts_in_subnets", remote_name=u"numberOfHostsInSubnets", attribute_type=int)
        self.expose_attribute(local_name=u"public_zone", remote_name=u"publicZone", attribute_type=bool)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str)

        # Fetchers

        self.subnettemplates = []
        self._subnettemplates_fetcher = NUSubNetworkTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"subnettemplates")

        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"zonetemplate"

    # REST methods

    def create_subnettemplate(self, subnettemplate, async=False, callback=None):
        """ Create a subnettemplate
            :param subnettemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=subnettemplate, async=async, callback=callback)

    def delete_subnettemplate(self, subnettemplate, async=False, callback=None):
        """ Removes a subnettemplate
            :param subnettemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=subnettemplate, async=async, callback=callback)

    def fetch_subnettemplates(self, filter=None, page=None, order_by=None):
        """ Fetch SubNetworkTemplates """

        if order_by:
            self._subnettemplates_fetcher.order_by = order_by

        return self._subnettemplates_fetcher.fetch_matching_entities(filter=filter, page=page)

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
