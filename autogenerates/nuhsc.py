# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUBGPPeersFetcher
from ..fetchers import NUPortStatussFetcher
from ..fetchers import NUVRSsFetcher

from restnuage import NURESTObject


class NUHSC(NURESTObject):
    """ Represents a HSC object """

    def __init__(self):
        """ Initializing object """

        super(NUHSC, self).__init__()

        # Read/Write Attributes
        
        self.model = None
        self.type = None
        self.already_marked_for_unavailable = None
        self.address = None
        self.management_ip = None
        self.unavailable_timestamp = None
        self.vsds = None
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
        
        self.expose_attribute(local_name=u"model", remote_name=u"model", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)
        self.expose_attribute(local_name=u"already_marked_for_unavailable", remote_name=u"alreadyMarkedForUnavailable", attribute_type=bool)
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"management_ip", remote_name=u"managementIP", attribute_type=str)
        self.expose_attribute(local_name=u"unavailable_timestamp", remote_name=u"unavailableTimestamp", attribute_type=str)
        self.expose_attribute(local_name=u"vsds", remote_name=u"vsds", attribute_type=str)
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
        
        self.bgppeers = []
        self._bgppeers_fetcher = NUBGPPeersFetcher.fetcher_with_entity(entity=self, local_name=u"bgppeers")
        
        self.monitoringports = []
        self._monitoringports_fetcher = NUPortStatussFetcher.fetcher_with_entity(entity=self, local_name=u"monitoringports")
        
        self.vrss = []
        self._vrss_fetcher = NUVRSsFetcher.fetcher_with_entity(entity=self, local_name=u"vrss")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"hsc"

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
    
    def create_bgppeer(self, bgppeer, async=False, callback=None):
        """ Create a bgppeer
            :param bgppeer: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=bgppeer, async=async, callback=callback)

    def delete_bgppeer(self, bgppeer, async=False, callback=None):
        """ Removes a bgppeer
            :param bgppeer: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=bgppeer, async=async, callback=callback)

    def fetch_bgppeers(self, filter=None, page=None, order_by=None):
        """ Fetch BGPPeers """

        if order_by:
            self._bgppeers_fetcher.order_by = order_by

        return self._bgppeers_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_monitoringport(self, monitoringport, async=False, callback=None):
        """ Create a monitoringport
            :param monitoringport: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=monitoringport, async=async, callback=callback)

    def delete_monitoringport(self, monitoringport, async=False, callback=None):
        """ Removes a monitoringport
            :param monitoringport: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=monitoringport, async=async, callback=callback)

    def fetch_monitoringports(self, filter=None, page=None, order_by=None):
        """ Fetch PortStatuss """

        if order_by:
            self._monitoringports_fetcher.order_by = order_by

        return self._monitoringports_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_vrs(self, vrs, async=False, callback=None):
        """ Create a vrs
            :param vrs: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vrs, async=async, callback=callback)

    def delete_vrs(self, vrs, async=False, callback=None):
        """ Removes a vrs
            :param vrs: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vrs, async=async, callback=callback)

    def fetch_vrss(self, filter=None, page=None, order_by=None):
        """ Fetch VRSs """

        if order_by:
            self._vrss_fetcher.order_by = order_by

        return self._vrss_fetcher.fetch_matching_entities(filter=filter, page=page)
    