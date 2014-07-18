# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUVSDComponentsFetcher

from restnuage import NURESTObject


class NUVSD(NURESTObject):
    """ Represents a VSD object """

    def __init__(self):
        """ Initializing object """

        super(NUVSD, self).__init__()

        # Read/Write Attributes
        
        self.already_marked_for_unavailable = None
        self.address = None
        self.management_ip = None
        self.mode = None
        self.peer_addresses = None
        self.unavailable_timestamp = None
        self.url = None
        self.messages = None
        self.average_cpu_usage = None
        self.average_memory_usage = None
        self.current_cpu_usage = None
        self.current_memory_usage = None
        self.description = None
        self.disks = None
        self.last_state_change = None
        self.location = None
        self.name = None
        self.peak_cpu_usage = None
        self.peak_memory_usage = None
        self.product_version = None
        self.status = None
        
        self.expose_attribute(local_name=u"already_marked_for_unavailable", remote_name=u"alreadyMarkedForUnavailable", attribute_type=bool)
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"management_ip", remote_name=u"managementIP", attribute_type=str)
        self.expose_attribute(local_name=u"mode", remote_name=u"mode", attribute_type=str)
        self.expose_attribute(local_name=u"peer_addresses", remote_name=u"peerAddresses", attribute_type=str)
        self.expose_attribute(local_name=u"unavailable_timestamp", remote_name=u"unavailableTimestamp", attribute_type=str)
        self.expose_attribute(local_name=u"url", remote_name=u"URL", attribute_type=str)
        self.expose_attribute(local_name=u"messages", remote_name=u"messages", attribute_type=str)
        self.expose_attribute(local_name=u"average_cpu_usage", remote_name=u"averageCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"average_memory_usage", remote_name=u"averageMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"current_cpu_usage", remote_name=u"currentCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"current_memory_usage", remote_name=u"currentMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"disks", remote_name=u"disks", attribute_type=str)
        self.expose_attribute(local_name=u"last_state_change", remote_name=u"lastStateChange", attribute_type=str)
        self.expose_attribute(local_name=u"location", remote_name=u"location", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"peak_cpu_usage", remote_name=u"peakCPUUsage", attribute_type=float)
        self.expose_attribute(local_name=u"peak_memory_usage", remote_name=u"peakMemoryUsage", attribute_type=float)
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)

        # Fetchers
        
        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")
        
        self.eventlogs = []
        self._eventlogs_fetcher = NUEventLogsFetcher.fetcher_with_entity(entity=self, local_name=u"eventlogs")
        
        self.jobs = []
        self._jobs_fetcher = NUJobsFetcher.fetcher_with_entity(entity=self, local_name=u"jobs")
        
        self.components = []
        self._components_fetcher = NUVSDComponentsFetcher.fetcher_with_entity(entity=self, local_name=u"components")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vsd"

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
    
    def create_component(self, component, async=False, callback=None):
        """ Create a component
            :param component: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=component, async=async, callback=callback)

    def delete_component(self, component, async=False, callback=None):
        """ Removes a component
            :param component: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=component, async=async, callback=callback)

    def fetch_components(self, filter=None, page=None, order_by=None):
        """ Fetch VSDComponents """

        if order_by:
            self._components_fetcher.order_by = order_by

        return self._components_fetcher.fetch_matching_entities(filter=filter, page=page)
    