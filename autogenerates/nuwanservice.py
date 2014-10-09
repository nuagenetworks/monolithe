# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUEnterprisePermissionsFetcher
from ..fetchers import NUPermittedActionsFetcher

from restnuage import NURESTObject


class NUWANService(NURESTObject):
    """ Represents a WANService object """

    def __init__(self):
        """ Initializing object """

        super(NUWANService, self).__init__()

        # Read/Write Attributes
        
        self.associated_domain_id = None
        self.domain_name = None
        self.enterprise_name = None
        self.associated_vpn_connect_id = None
        self.config_type = None
        self.description = None
        self.external_route_target = None
        self.irb_enabled = None
        self.name = None
        self.orphan = None
        self.permitted_action = None
        self.service_policy = None
        self.service_type = None
        self.tunnel_type = None
        self.user_mnemonic = None
        self.use_user_mnemonic = None
        self.vn_id = None
        self.wan_service_identifier = None
        
        self.expose_attribute(local_name=u"associated_domain_id", remote_name=u"associatedDomainID", attribute_type=str)
        self.expose_attribute(local_name=u"domain_name", remote_name=u"domainName", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_name", remote_name=u"enterpriseName", attribute_type=str)
        self.expose_attribute(local_name=u"associated_vpn_connect_id", remote_name=u"associatedVPNConnectID", attribute_type=str)
        self.expose_attribute(local_name=u"config_type", remote_name=u"configType", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"external_route_target", remote_name=u"externalRouteTarget", attribute_type=str)
        self.expose_attribute(local_name=u"irb_enabled", remote_name=u"IRBEnabled", attribute_type=bool)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"orphan", remote_name=u"orphan", attribute_type=bool)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str)
        self.expose_attribute(local_name=u"service_policy", remote_name=u"servicePolicy", attribute_type=str)
        self.expose_attribute(local_name=u"service_type", remote_name=u"serviceType", attribute_type=str)
        self.expose_attribute(local_name=u"tunnel_type", remote_name=u"tunnelType", attribute_type=str)
        self.expose_attribute(local_name=u"user_mnemonic", remote_name=u"userMnemonic", attribute_type=str)
        self.expose_attribute(local_name=u"use_user_mnemonic", remote_name=u"useUserMnemonic", attribute_type=bool)
        self.expose_attribute(local_name=u"vn_id", remote_name=u"vnId", attribute_type=str)
        self.expose_attribute(local_name=u"wan_service_identifier", remote_name=u"WANServiceIdentifier", attribute_type=str)

        # Fetchers
        
        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")
        
        self.enterprisepermissions = []
        self._enterprisepermissions_fetcher = NUEnterprisePermissionsFetcher.fetcher_with_entity(entity=self, local_name=u"enterprisepermissions")
        
        self.permissions = []
        self._permissions_fetcher = NUPermittedActionsFetcher.fetcher_with_entity(entity=self, local_name=u"permissions")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"service"

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
    