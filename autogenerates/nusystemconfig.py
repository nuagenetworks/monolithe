# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUSystemConfig(NURESTObject):
    """ Represents a SystemConfig object """

    def __init__(self):
        """ Initializing object """

        super(NUSystemConfig, self).__init__()

        # Read/Write Attributes
        
        self.acl_allow_origin = None
        self.api_key_renewal_interval = None
        self.api_key_validity = None
        self.as_number = None
        self.ad_gateway_purge_time = None
        self.avatar_base_path = None
        self.avatar_base_url = None
        self.offset_customer_id = None
        self.dhcp_option_size = None
        self.domain_tunnel_type = None
        self.esi_id = None
        self.event_log_cleanup_interval = None
        self.event_log_entry_max_age = None
        self.event_processor_interval = None
        self.event_processor_max_events_count = None
        self.event_processor_timeout = None
        self.inactive_timeout = None
        self.ldap_trust_store_certifcate = None
        self.ldap_trust_store_password = None
        self.lru_cache_size_per_subnet = None
        self.alarms_max_per_object = None
        self.page_max_size = None
        self.max_response = None
        self.page_size = None
        self.post_processor_threads_count = None
        self.reflexive_acl_timeout = None
        self.offset_service_id = None
        self.stack_trace_enabled = None
        self.stats_collector_address = None
        self.stats_collector_port = None
        self.stats_max_data_points = None
        self.stats_min_duration = None
        self.stats_number_of_data_points = None
        self.subnet_resync_interval = None
        self.subnet_resync_outstanding_interval = None
        self.sysmon_cleanup_task_interval = None
        self.sysmon_node_presence_timeout = None
        self.sysmon_probe_response_timeout = None
        self.stats_tsdb_server_address = None
        self.vm_cache_size = None
        self.vm_resync_outstanding_interval = None
        self.vm_purge_time = None
        self.vm_resync_deletion_wait_time = None
        self.vm_unreachable_cleanup_time = None
        self.vm_unreachable_time = None
        self.offset_virtual_network_id = None
        self.vsc_on_same_version_as_vsd = None
        
        self.expose_attribute(local_name=u"acl_allow_origin", remote_name=u"ACLAllowOrigin", attribute_type=str)
        self.expose_attribute(local_name=u"api_key_renewal_interval", remote_name=u"APIKeyRenewalInterval", attribute_type=str)
        self.expose_attribute(local_name=u"api_key_validity", remote_name=u"APIKeyValidity", attribute_type=str)
        self.expose_attribute(local_name=u"as_number", remote_name=u"ASNumber", attribute_type=str)
        self.expose_attribute(local_name=u"ad_gateway_purge_time", remote_name=u"ADGatewayPurgeTime", attribute_type=int)
        self.expose_attribute(local_name=u"avatar_base_path", remote_name=u"avatarBasePath", attribute_type=str)
        self.expose_attribute(local_name=u"avatar_base_url", remote_name=u"avatarBaseURL", attribute_type=str)
        self.expose_attribute(local_name=u"offset_customer_id", remote_name=u"offsetCustomerID", attribute_type=int)
        self.expose_attribute(local_name=u"dhcp_option_size", remote_name=u"DHCPOptionSize", attribute_type=int)
        self.expose_attribute(local_name=u"domain_tunnel_type", remote_name=u"domainTunnelType", attribute_type=str)
        self.expose_attribute(local_name=u"esi_id", remote_name=u"esiID", attribute_type=int)
        self.expose_attribute(local_name=u"event_log_cleanup_interval", remote_name=u"eventLogCleanupInterval", attribute_type=str)
        self.expose_attribute(local_name=u"event_log_entry_max_age", remote_name=u"eventLogEntryMaxAge", attribute_type=int)
        self.expose_attribute(local_name=u"event_processor_interval", remote_name=u"eventProcessorInterval", attribute_type=str)
        self.expose_attribute(local_name=u"event_processor_max_events_count", remote_name=u"eventProcessorMaxEventsCount", attribute_type=int)
        self.expose_attribute(local_name=u"event_processor_timeout", remote_name=u"eventProcessorTimeout", attribute_type=str)
        self.expose_attribute(local_name=u"inactive_timeout", remote_name=u"inactiveTimeout", attribute_type=str)
        self.expose_attribute(local_name=u"ldap_trust_store_certifcate", remote_name=u"LDAPTrustStoreCertifcate", attribute_type=str)
        self.expose_attribute(local_name=u"ldap_trust_store_password", remote_name=u"LDAPTrustStorePassword", attribute_type=str)
        self.expose_attribute(local_name=u"lru_cache_size_per_subnet", remote_name=u"LRUCacheSizePerSubnet", attribute_type=int)
        self.expose_attribute(local_name=u"alarms_max_per_object", remote_name=u"alarmsMaxPerObject", attribute_type=int)
        self.expose_attribute(local_name=u"page_max_size", remote_name=u"pageMaxSize", attribute_type=int)
        self.expose_attribute(local_name=u"max_response", remote_name=u"maxResponse", attribute_type=int)
        self.expose_attribute(local_name=u"page_size", remote_name=u"pageSize", attribute_type=int)
        self.expose_attribute(local_name=u"post_processor_threads_count", remote_name=u"postProcessorThreadsCount", attribute_type=int)
        self.expose_attribute(local_name=u"reflexive_acl_timeout", remote_name=u"reflexiveACLTimeout", attribute_type=str)
        self.expose_attribute(local_name=u"offset_service_id", remote_name=u"offsetServiceID", attribute_type=int)
        self.expose_attribute(local_name=u"stack_trace_enabled", remote_name=u"stackTraceEnabled", attribute_type=bool)
        self.expose_attribute(local_name=u"stats_collector_address", remote_name=u"statsCollectorAddress", attribute_type=str)
        self.expose_attribute(local_name=u"stats_collector_port", remote_name=u"statsCollectorPort", attribute_type=str)
        self.expose_attribute(local_name=u"stats_max_data_points", remote_name=u"statsMaxDataPoints", attribute_type=int)
        self.expose_attribute(local_name=u"stats_min_duration", remote_name=u"statsMinDuration", attribute_type=str)
        self.expose_attribute(local_name=u"stats_number_of_data_points", remote_name=u"statsNumberOfDataPoints", attribute_type=int)
        self.expose_attribute(local_name=u"subnet_resync_interval", remote_name=u"subnetResyncInterval", attribute_type=int)
        self.expose_attribute(local_name=u"subnet_resync_outstanding_interval", remote_name=u"subnetResyncOutstandingInterval", attribute_type=int)
        self.expose_attribute(local_name=u"sysmon_cleanup_task_interval", remote_name=u"sysmonCleanupTaskInterval", attribute_type=str)
        self.expose_attribute(local_name=u"sysmon_node_presence_timeout", remote_name=u"sysmonNodePresenceTimeout", attribute_type=str)
        self.expose_attribute(local_name=u"sysmon_probe_response_timeout", remote_name=u"sysmonProbeResponseTimeout", attribute_type=str)
        self.expose_attribute(local_name=u"stats_tsdb_server_address", remote_name=u"statsTSDBServerAddress", attribute_type=str)
        self.expose_attribute(local_name=u"vm_cache_size", remote_name=u"VMCacheSize", attribute_type=int)
        self.expose_attribute(local_name=u"vm_resync_outstanding_interval", remote_name=u"VMResyncOutstandingInterval", attribute_type=int)
        self.expose_attribute(local_name=u"vm_purge_time", remote_name=u"VMPurgeTime", attribute_type=int)
        self.expose_attribute(local_name=u"vm_resync_deletion_wait_time", remote_name=u"VMResyncDeletionWaitTime", attribute_type=int)
        self.expose_attribute(local_name=u"vm_unreachable_cleanup_time", remote_name=u"VMUnreachableCleanupTime", attribute_type=int)
        self.expose_attribute(local_name=u"vm_unreachable_time", remote_name=u"VMUnreachableTime", attribute_type=int)
        self.expose_attribute(local_name=u"offset_virtual_network_id", remote_name=u"offsetVirtualNetworkID", attribute_type=int)
        self.expose_attribute(local_name=u"vsc_on_same_version_as_vsd", remote_name=u"VSCOnSameVersionAsVSD", attribute_type=bool)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"systemconfig"

    # REST methods
    