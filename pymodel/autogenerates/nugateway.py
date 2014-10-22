# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUBootstrapsFetcher
from ..fetchers import NUBootstrapActivationsFetcher
from ..fetchers import NUEnterprisePermissionsFetcher
from ..fetchers import NUInfrastructureConfigsFetcher
from ..fetchers import NULocationsFetcher
from ..fetchers import NUPortsFetcher
from ..fetchers import NUWANServicesFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUPermittedActionsFetcher

from bambou import NURESTObject


class NUGateway(NURESTObject):
    """ Represents a Gateway object """

    def __init__(self):
        """ Initializing object """

        super(NUGateway, self).__init__()

        # Read/Write Attributes

        self.template_id = None
        self.auto_disc_gateway_id = None
        self.bootstrap_id = None
        self.enterprise_id = None
        self.location_id = None
        self.pending = None
        self.permitted_action = None
        self.redundancy_group_id = None
        self.system_id = None
        self.description = None
        self.infrastructure_profile_id = None
        self.name = None
        self.personality = None

        self.expose_attribute(local_name=u"template_id", remote_name=u"templateID", attribute_type=str)
        self.expose_attribute(local_name=u"auto_disc_gateway_id", remote_name=u"autoDiscGatewayID", attribute_type=str)
        self.expose_attribute(local_name=u"bootstrap_id", remote_name=u"bootstrapID", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str)
        self.expose_attribute(local_name=u"location_id", remote_name=u"locationID", attribute_type=str)
        self.expose_attribute(local_name=u"pending", remote_name=u"pending", attribute_type=bool)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str)
        self.expose_attribute(local_name=u"redundancy_group_id", remote_name=u"redundancyGroupID", attribute_type=str)
        self.expose_attribute(local_name=u"system_id", remote_name=u"systemID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"infrastructure_profile_id", remote_name=u"infrastructureProfileID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"personality", remote_name=u"personality", attribute_type=str)

        # Fetchers

        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")

        self.bootstraps = []
        self._bootstraps_fetcher = NUBootstrapsFetcher.fetcher_with_entity(entity=self, local_name=u"bootstraps")

        self.bootstrapactivations = []
        self._bootstrapactivations_fetcher = NUBootstrapActivationsFetcher.fetcher_with_entity(entity=self, local_name=u"bootstrapactivations")

        self.enterprisepermissions = []
        self._enterprisepermissions_fetcher = NUEnterprisePermissionsFetcher.fetcher_with_entity(entity=self, local_name=u"enterprisepermissions")

        self.infraconfig = []
        self._infraconfig_fetcher = NUInfrastructureConfigsFetcher.fetcher_with_entity(entity=self, local_name=u"infraconfig")

        self.locations = []
        self._locations_fetcher = NULocationsFetcher.fetcher_with_entity(entity=self, local_name=u"locations")

        self.ports = []
        self._ports_fetcher = NUPortsFetcher.fetcher_with_entity(entity=self, local_name=u"ports")

        self.services = []
        self._services_fetcher = NUWANServicesFetcher.fetcher_with_entity(entity=self, local_name=u"services")

        self.jobs = []
        self._jobs_fetcher = NUJobsFetcher.fetcher_with_entity(entity=self, local_name=u"jobs")

        self.permissions = []
        self._permissions_fetcher = NUPermittedActionsFetcher.fetcher_with_entity(entity=self, local_name=u"permissions")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"gateway"

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

    def create_bootstrap(self, bootstrap, async=False, callback=None):
        """ Create a bootstrap
            :param bootstrap: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=bootstrap, async=async, callback=callback)

    def delete_bootstrap(self, bootstrap, async=False, callback=None):
        """ Removes a bootstrap
            :param bootstrap: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=bootstrap, async=async, callback=callback)

    def fetch_bootstraps(self, filter=None, page=None, order_by=None):
        """ Fetch Bootstraps """

        if order_by:
            self._bootstraps_fetcher.order_by = order_by

        return self._bootstraps_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_bootstrapactivation(self, bootstrapactivation, async=False, callback=None):
        """ Create a bootstrapactivation
            :param bootstrapactivation: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=bootstrapactivation, async=async, callback=callback)

    def delete_bootstrapactivation(self, bootstrapactivation, async=False, callback=None):
        """ Removes a bootstrapactivation
            :param bootstrapactivation: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=bootstrapactivation, async=async, callback=callback)

    def fetch_bootstrapactivations(self, filter=None, page=None, order_by=None):
        """ Fetch BootstrapActivations """

        if order_by:
            self._bootstrapactivations_fetcher.order_by = order_by

        return self._bootstrapactivations_fetcher.fetch_matching_entities(filter=filter, page=page)

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

    def create_infraconfi(self, infraconfi, async=False, callback=None):
        """ Create a infraconfi
            :param infraconfi: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=infraconfi, async=async, callback=callback)

    def delete_infraconfi(self, infraconfi, async=False, callback=None):
        """ Removes a infraconfi
            :param infraconfi: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=infraconfi, async=async, callback=callback)

    def fetch_infraconfig(self, filter=None, page=None, order_by=None):
        """ Fetch InfrastructureConfigs """

        if order_by:
            self._infraconfig_fetcher.order_by = order_by

        return self._infraconfig_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_location(self, location, async=False, callback=None):
        """ Create a location
            :param location: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=location, async=async, callback=callback)

    def delete_location(self, location, async=False, callback=None):
        """ Removes a location
            :param location: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=location, async=async, callback=callback)

    def fetch_locations(self, filter=None, page=None, order_by=None):
        """ Fetch Locations """

        if order_by:
            self._locations_fetcher.order_by = order_by

        return self._locations_fetcher.fetch_matching_entities(filter=filter, page=page)

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

    def create_job(self, job, async=False, callback=None):
        """ Create a job
            :param job: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=job, async=async, callback=callback)

    def delete_job(self, job, async=False, callback=None):
        """ Removes a job
            :param job: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=job, async=async, callback=callback)

    def fetch_jobs(self, filter=None, page=None, order_by=None):
        """ Fetch Jobs """

        if order_by:
            self._jobs_fetcher.order_by = order_by

        return self._jobs_fetcher.fetch_matching_entities(filter=filter, page=page)

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
