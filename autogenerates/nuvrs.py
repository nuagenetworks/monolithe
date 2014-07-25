# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUHSCsFetcher
from ..fetchers import NUPortStatussFetcher
from ..fetchers import NUVSCsFetcher
from ..fetchers import NUVirtualMachinesFetcher
from ..fetchers import NUVPortsFetcher

from restnuage import NURESTObject


class NUVRS(NURESTObject):
    """ Represents a VRS object """

    def __init__(self):
        """ Initializing object """

        super(NUVRS, self).__init__()

        # Read/Write Attributes
        
        self.parent_i_ds = None
        self.cluster_node_role = None
        self.messages = None
        self.dynamic = None
        self.hypervisor_connection_state = None
        self.hypervisor_identifier = None
        self.hypervisor_name = None
        self.hypervisor_type = None
        self.address = None
        self.jsonconnection = None
        self.last_event_name = None
        self.last_event_object = None
        self.last_event_timestamp = None
        self.management_ip = None
        self.number_of_bridge_interfaces = None
        self.number_of_host_interfaces = None
        self.number_of_virtual_machines = None
        self.peer = None
        self.personality = None
        self.role = None
        self.uptime = None
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
        
        self.expose_attribute(local_name=u"parent_i_ds", remote_name=u"parentIDs", attribute_type=str)
        self.expose_attribute(local_name=u"cluster_node_role", remote_name=u"clusterNodeRole", attribute_type=str)
        self.expose_attribute(local_name=u"messages", remote_name=u"messages", attribute_type=str)
        self.expose_attribute(local_name=u"dynamic", remote_name=u"dynamic", attribute_type=bool)
        self.expose_attribute(local_name=u"hypervisor_connection_state", remote_name=u"hypervisorConnectionState", attribute_type=str)
        self.expose_attribute(local_name=u"hypervisor_identifier", remote_name=u"hypervisorIdentifier", attribute_type=str)
        self.expose_attribute(local_name=u"hypervisor_name", remote_name=u"hypervisorName", attribute_type=str)
        self.expose_attribute(local_name=u"hypervisor_type", remote_name=u"hypervisorType", attribute_type=str)
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"jsonconnection", remote_name=u"jsonconnection", attribute_type=str)
        self.expose_attribute(local_name=u"last_event_name", remote_name=u"lastEventName", attribute_type=str)
        self.expose_attribute(local_name=u"last_event_object", remote_name=u"lastEventObject", attribute_type=str)
        self.expose_attribute(local_name=u"last_event_timestamp", remote_name=u"lastEventTimestamp", attribute_type=str)
        self.expose_attribute(local_name=u"management_ip", remote_name=u"managementIP", attribute_type=str)
        self.expose_attribute(local_name=u"number_of_bridge_interfaces", remote_name=u"numberOfBridgeInterfaces", attribute_type=int)
        self.expose_attribute(local_name=u"number_of_host_interfaces", remote_name=u"numberOfHostInterfaces", attribute_type=int)
        self.expose_attribute(local_name=u"number_of_virtual_machines", remote_name=u"numberOfVirtualMachines", attribute_type=int)
        self.expose_attribute(local_name=u"peer", remote_name=u"peer", attribute_type=str)
        self.expose_attribute(local_name=u"personality", remote_name=u"personality", attribute_type=str)
        self.expose_attribute(local_name=u"role", remote_name=u"role", attribute_type=str)
        self.expose_attribute(local_name=u"uptime", remote_name=u"uptime", attribute_type=str)
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
        
        self.jobs = []
        self._jobs_fetcher = NUJobsFetcher.fetcher_with_entity(entity=self, local_name=u"jobs")
        
        self.hscs = []
        self._hscs_fetcher = NUHSCsFetcher.fetcher_with_entity(entity=self, local_name=u"hscs")
        
        self.monitoringports = []
        self._monitoringports_fetcher = NUPortStatussFetcher.fetcher_with_entity(entity=self, local_name=u"monitoringports")
        
        self.vscs = []
        self._vscs_fetcher = NUVSCsFetcher.fetcher_with_entity(entity=self, local_name=u"vscs")
        
        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")
        
        self.vports = []
        self._vports_fetcher = NUVPortsFetcher.fetcher_with_entity(entity=self, local_name=u"vports")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vrs"

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
    
    def create_hsc(self, hsc, async=False, callback=None):
        """ Create a hsc
            :param hsc: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=hsc, async=async, callback=callback)

    def delete_hsc(self, hsc, async=False, callback=None):
        """ Removes a hsc
            :param hsc: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=hsc, async=async, callback=callback)

    def fetch_hscs(self, filter=None, page=None, order_by=None):
        """ Fetch HSCs """

        if order_by:
            self._hscs_fetcher.order_by = order_by

        return self._hscs_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_vsc(self, vsc, async=False, callback=None):
        """ Create a vsc
            :param vsc: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vsc, async=async, callback=callback)

    def delete_vsc(self, vsc, async=False, callback=None):
        """ Removes a vsc
            :param vsc: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vsc, async=async, callback=callback)

    def fetch_vscs(self, filter=None, page=None, order_by=None):
        """ Fetch VSCs """

        if order_by:
            self._vscs_fetcher.order_by = order_by

        return self._vscs_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_vm(self, vm, async=False, callback=None):
        """ Create a vm
            :param vm: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vm, async=async, callback=callback)

    def delete_vm(self, vm, async=False, callback=None):
        """ Removes a vm
            :param vm: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vm, async=async, callback=callback)

    def fetch_vms(self, filter=None, page=None, order_by=None):
        """ Fetch VirtualMachines """

        if order_by:
            self._vms_fetcher.order_by = order_by

        return self._vms_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_vport(self, vport, async=False, callback=None):
        """ Create a vport
            :param vport: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vport, async=async, callback=callback)

    def delete_vport(self, vport, async=False, callback=None):
        """ Removes a vport
            :param vport: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vport, async=async, callback=callback)

    def fetch_vports(self, filter=None, page=None, order_by=None):
        """ Fetch VPorts """

        if order_by:
            self._vports_fetcher.order_by = order_by

        return self._vports_fetcher.fetch_matching_entities(filter=filter, page=page)
    