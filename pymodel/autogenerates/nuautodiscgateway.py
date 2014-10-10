# -*- coding: utf-8 -*-

from ..fetchers import NUPortsFetcher
from ..fetchers import NUWANServicesFetcher

from restnuage import NURESTObject


class NUAutoDiscGateway(NURESTObject):
    """ Represents a AutoDiscGateway object """

    def __init__(self):
        """ Initializing object """

        super(NUAutoDiscGateway, self).__init__()

        # Read/Write Attributes
        
        self.controllers = None
        self.gateway_id = None
        self.related_ports = None
        self.system_id = None
        self.description = None
        self.infrastructure_profile_id = None
        self.name = None
        self.personality = None
        
        self.expose_attribute(local_name=u"controllers", remote_name=u"controllers", attribute_type=str)
        self.expose_attribute(local_name=u"gateway_id", remote_name=u"gatewayID", attribute_type=str)
        self.expose_attribute(local_name=u"related_ports", remote_name=u"relatedPorts", attribute_type=str)
        self.expose_attribute(local_name=u"system_id", remote_name=u"systemID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"infrastructure_profile_id", remote_name=u"infrastructureProfileID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"personality", remote_name=u"personality", attribute_type=str)

        # Fetchers
        
        self.ports = []
        self._ports_fetcher = NUPortsFetcher.fetcher_with_entity(entity=self, local_name=u"ports")
        
        self.services = []
        self._services_fetcher = NUWANServicesFetcher.fetcher_with_entity(entity=self, local_name=u"services")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"autodiscoveredgateway"

    # REST methods
    
    def create_port(self, port, async=False, callback=None):
        """ Create a port
            :param port: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=port, async=async, callback=callback)

    def delete_port(self, port, async=False, callback=None):
        """ Removes a port
            :param port: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=port, async=async, callback=callback)

    def fetch_ports(self, filter=None, page=None, order_by=None):
        """ Fetch Ports """

        if order_by:
            self._ports_fetcher.order_by = order_by

        return self._ports_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_service(self, service, async=False, callback=None):
        """ Create a service
            :param service: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=service, async=async, callback=callback)

    def delete_service(self, service, async=False, callback=None):
        """ Removes a service
            :param service: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=service, async=async, callback=callback)

    def fetch_services(self, filter=None, page=None, order_by=None):
        """ Fetch WANServices """

        if order_by:
            self._services_fetcher.order_by = order_by

        return self._services_fetcher.fetch_matching_entities(filter=filter, page=page)
    