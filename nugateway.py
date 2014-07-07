# -*- coding:utf-8 -*-

from .nugatewaybase import NUGatewayBase

NUGATEWAY_CHILDRENSTATUSINITIALIZED = u"INITIALIZED"
NUGATEWAY_CHILDRENSTATUSREADY = u"READY"
NUGATEWAY_CHILDRENSTATUSORPHAN = u"ORPHAN"
NUGATEWAY_CHILDRENSTATUSMISMATCH = u"MISMATCH"


class NUGateway(NUGatewayBase):
    """ Defines a Gateway """

    def __init__(self):
        """ Initialize a new object """

        super(NUGateway, self).__init__()

        # Read/Write Attributes
        self.auto_discovered_gateway_id = None
        self.pending = bool()
        self.permitted_action = None
        self.redundancy_group_id = None  # NUMaintenanceModeDisabled
        self.system_id = None
        self.template_id = None

        self.alarms = []
        self.auto_discovered_gateways = []
        self.enterprise_permissions = []
        self.permissions = []
        self.ports = []
        self.wan_services = []

        self.expose_attribute(local_name=u'system_id', remote_name=u'systemID')
        self.expose_attribute(local_name=u'template_id', remote_name=u'templateID')
        self.expose_attribute(local_name=u'pending', remote_name=u'pending')
        self.expose_attribute(local_name=u'redundancy_group_id', remote_name=u'redundancyGroupID')
        self.expose_attribute(local_name=u'permitted_action', remote_name=u'permittedAction')
        self.expose_attribute(local_name=u'auto_discovered_gateway_id', remote_name=u'autoDiscGatewayID')

        # Fetchers
        # TODO : Write fetchers here
        # self.alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u'alarms')
        # self.auto_discovered_gateways_fetcher = NUAutodiscoveredGatewaysFetcher.fetcher_with_entity(entity=self, local_name=u'auto_discovered_gateways')
        # self.enterprise_permissions_fetcher = NUEnterprisePermissionsFetcher.fetcher_with_entity(entity=self, local_name=u'enterprise_permissions')
        # self.permissions_fetcher = NUPermissionsFetcher.fetcher_with_entity(entity=self, local_name=u'permissions')
        # self.ports_fetcher = NUPortsFetcher.fetcher_with_entity(entity=self, local_name=u'ports')
        # self.wan_services_fetcher = NUWANServicesFetcher.fetcher_with_entity(entity=self, local_name=u'wan_services')

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"gateway"

    # REST methods
    # TODO: Write methods here
