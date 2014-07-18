# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUEnterprisePermissionsFetcher
from ..fetchers import NUGatewaysFetcher
from ..fetchers import NUPortsFetcher
from ..fetchers import NUWANServicesFetcher
from ..fetchers import NUPermittedActionsFetcher

from restnuage import NURESTObject


class NURedundantGWGrp(NURESTObject):
    """ Represents a RedundantGWGrp object """

    def __init__(self):
        """ Initializing object """

        super(NURedundantGWGrp, self).__init__()

        # Read/Write Attributes
        
        self.gateway_peer1_autodiscovered_gateway_id = None
        self.gateway_peer2_autodiscovered_gateway_id = None
        self.description = None
        self.enterprise_id = None
        self.redundant_gateway_status = None
        self.gateway_peer1_id = None
        self.gateway_peer1_name = None
        self.gateway_peer2_id = None
        self.gateway_peer2_name = None
        self.name = None
        self.permitted_action = None
        self.personality = None
        
        self.expose_attribute(local_name=u"gateway_peer1_autodiscovered_gateway_id", remote_name=u"gatewayPeer1AutodiscoveredGatewayID", attribute_type=str)
        self.expose_attribute(local_name=u"gateway_peer2_autodiscovered_gateway_id", remote_name=u"gatewayPeer2AutodiscoveredGatewayID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str)
        self.expose_attribute(local_name=u"redundant_gateway_status", remote_name=u"redundantGatewayStatus", attribute_type=str)
        self.expose_attribute(local_name=u"gateway_peer1_id", remote_name=u"gatewayPeer1ID", attribute_type=str)
        self.expose_attribute(local_name=u"gateway_peer1_name", remote_name=u"gatewayPeer1Name", attribute_type=str)
        self.expose_attribute(local_name=u"gateway_peer2_id", remote_name=u"gatewayPeer2ID", attribute_type=str)
        self.expose_attribute(local_name=u"gateway_peer2_name", remote_name=u"gatewayPeer2Name", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str)
        self.expose_attribute(local_name=u"personality", remote_name=u"personality", attribute_type=str)

        # Fetchers
        
        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")
        
        self.eventlogs = []
        self._eventlogs_fetcher = NUEventLogsFetcher.fetcher_with_entity(entity=self, local_name=u"eventlogs")
        
        self.enterprisepermissions = []
        self._enterprisepermissions_fetcher = NUEnterprisePermissionsFetcher.fetcher_with_entity(entity=self, local_name=u"enterprisepermissions")
        
        self.gateways = []
        self._gateways_fetcher = NUGatewaysFetcher.fetcher_with_entity(entity=self, local_name=u"gateways")
        
        self.ports = []
        self._ports_fetcher = NUPortsFetcher.fetcher_with_entity(entity=self, local_name=u"ports")
        
        self.services = []
        self._services_fetcher = NUWANServicesFetcher.fetcher_with_entity(entity=self, local_name=u"services")
        
        self.permissions = []
        self._permissions_fetcher = NUPermittedActionsFetcher.fetcher_with_entity(entity=self, local_name=u"permissions")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"redundancygroup"

    # REST methods
    
    def create_alarm(self, alarm, async=False, callback=None):
        """ Create a alarm
            :param alarm: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=alarm, async=async, callback=callback)

    def delete_alarm(self, alarm, async=False, callback=None):
        """ Removes a alarm
            :param alarm: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=alarm, async=async, callback=callback)

    def fetch_alarms(self, filter=None, page=None, order_by=None):
        """ Fetch Alarms """

        if order_by:
            self._alarms_fetcher.order_by = order_by

        return self._alarms_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_eventlog(self, eventlog, async=False, callback=None):
        """ Create a eventlog
            :param eventlog: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=eventlog, async=async, callback=callback)

    def delete_eventlog(self, eventlog, async=False, callback=None):
        """ Removes a eventlog
            :param eventlog: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=eventlog, async=async, callback=callback)

    def fetch_eventlogs(self, filter=None, page=None, order_by=None):
        """ Fetch EventLogs """

        if order_by:
            self._eventlogs_fetcher.order_by = order_by

        return self._eventlogs_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_enterprisepermission(self, enterprisepermission, async=False, callback=None):
        """ Create a enterprisepermission
            :param enterprisepermission: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=enterprisepermission, async=async, callback=callback)

    def delete_enterprisepermission(self, enterprisepermission, async=False, callback=None):
        """ Removes a enterprisepermission
            :param enterprisepermission: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=enterprisepermission, async=async, callback=callback)

    def fetch_enterprisepermissions(self, filter=None, page=None, order_by=None):
        """ Fetch EnterprisePermissions """

        if order_by:
            self._enterprisepermissions_fetcher.order_by = order_by

        return self._enterprisepermissions_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_gateway(self, gateway, async=False, callback=None):
        """ Create a gateway
            :param gateway: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=gateway, async=async, callback=callback)

    def delete_gateway(self, gateway, async=False, callback=None):
        """ Removes a gateway
            :param gateway: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=gateway, async=async, callback=callback)

    def fetch_gateways(self, filter=None, page=None, order_by=None):
        """ Fetch Gateways """

        if order_by:
            self._gateways_fetcher.order_by = order_by

        return self._gateways_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    