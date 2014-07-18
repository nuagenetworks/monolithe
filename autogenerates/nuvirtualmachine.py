# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUEventLogsFetcher
from ..fetchers import NUVRSsFetcher
from ..fetchers import NUVMInterfacesFetcher
from ..fetchers import NUVMResyncsFetcher

from restnuage import NURESTObject


class NUVirtualMachine(NURESTObject):
    """ Represents a VirtualMachine object """

    def __init__(self):
        """ Initializing object """

        super(NUVirtualMachine, self).__init__()

        # Read/Write Attributes
        
        self.app_name = None
        self.domain_i_ds = None
        self.enterprise_id = None
        self.enterprise_name = None
        self.hypervisor_ip = None
        self.interfaces = None
        self.l2_domain_i_ds = None
        self.name = None
        self.resync_info = None
        self.subnet_i_ds = None
        self.user_id = None
        self.user_name = None
        self.uuid = None
        self.status = None
        self.reason_type = None
        self.vrsid = None
        self.zone_i_ds = None
        
        self.expose_attribute(local_name=u"app_name", remote_name=u"appName", attribute_type=str)
        self.expose_attribute(local_name=u"domain_i_ds", remote_name=u"domainIDs", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_name", remote_name=u"enterpriseName", attribute_type=str)
        self.expose_attribute(local_name=u"hypervisor_ip", remote_name=u"hypervisorIP", attribute_type=str)
        self.expose_attribute(local_name=u"interfaces", remote_name=u"interfaces", attribute_type=str)
        self.expose_attribute(local_name=u"l2_domain_i_ds", remote_name=u"l2DomainIDs", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"resync_info", remote_name=u"resyncInfo", attribute_type=str)
        self.expose_attribute(local_name=u"subnet_i_ds", remote_name=u"subnetIDs", attribute_type=str)
        self.expose_attribute(local_name=u"user_id", remote_name=u"userID", attribute_type=str)
        self.expose_attribute(local_name=u"user_name", remote_name=u"userName", attribute_type=str)
        self.expose_attribute(local_name=u"uuid", remote_name=u"UUID", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)
        self.expose_attribute(local_name=u"reason_type", remote_name=u"reasonType", attribute_type=str)
        self.expose_attribute(local_name=u"vrsid", remote_name=u"VRSID", attribute_type=str)
        self.expose_attribute(local_name=u"zone_i_ds", remote_name=u"zoneIDs", attribute_type=str)

        # Fetchers
        
        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")
        
        self.eventlogs = []
        self._eventlogs_fetcher = NUEventLogsFetcher.fetcher_with_entity(entity=self, local_name=u"eventlogs")
        
        self.vrss = []
        self._vrss_fetcher = NUVRSsFetcher.fetcher_with_entity(entity=self, local_name=u"vrss")
        
        self.vminterfaces = []
        self._vminterfaces_fetcher = NUVMInterfacesFetcher.fetcher_with_entity(entity=self, local_name=u"vminterfaces")
        
        self.resync = []
        self._resync_fetcher = NUVMResyncsFetcher.fetcher_with_entity(entity=self, local_name=u"resync")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vm"

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
    
    def create_vminterface(self, vminterface, async=False, callback=None):
        """ Create a vminterface
            :param vminterface: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vminterface, async=async, callback=callback)

    def delete_vminterface(self, vminterface, async=False, callback=None):
        """ Removes a vminterface
            :param vminterface: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vminterface, async=async, callback=callback)

    def fetch_vminterfaces(self, filter=None, page=None, order_by=None):
        """ Fetch VMInterfaces """

        if order_by:
            self._vminterfaces_fetcher.order_by = order_by

        return self._vminterfaces_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_resyn(self, resyn, async=False, callback=None):
        """ Create a resyn
            :param resyn: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=resyn, async=async, callback=callback)

    def delete_resyn(self, resyn, async=False, callback=None):
        """ Removes a resyn
            :param resyn: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=resyn, async=async, callback=callback)

    def fetch_resync(self, filter=None, page=None, order_by=None):
        """ Fetch VMResyncs """

        if order_by:
            self._resync_fetcher.order_by = order_by

        return self._resync_fetcher.fetch_matching_entities(filter=filter, page=page)
    