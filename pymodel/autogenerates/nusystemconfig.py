# -*- coding: utf-8 -*-


from bambou import NURESTObject


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
        self.customer_id_upper_limit = None
        self.customer_key = None
        self.dhcp_option_size = None
        self.domain_tunnel_type = None
        self.ejbca_client_key_store = None
        self.ejbca_client_key_store_password = None
        self.ejbca_client_namespace_uri = None
        self.ejbca_client_trust_store = None
        self.ejbca_client_trust_store_password = None
        self.ejbca_client_ws_local_part = None
        self.ejbca_client_ws_url = None
        self.ejbca_ncpe_certificate_profile = None
        self.ejbca_ncpe_end_entity_profile = None
        self.ejbca_server_hostname = None
        self.ejbca_server_port = None
        self.ejbca_vsp_root_ca = None
        self.esi_id = None
        self.event_log_cleanup_interval = None
        self.event_log_entry_max_age = None
        self.event_processor_interval = None
        self.event_processor_max_events_count = None
        self.event_processor_timeout = None
        self.evpnbgp_community_tag_as_number = None
        self.evpnbgp_community_tag_lower_limit = None
        self.evpnbgp_community_tag_upper_limit = None
        self.inactive_timeout = None
        self.ldap_trust_store_certifcate = None
        self.ldap_trust_store_password = None
        self.lru_cache_size_per_subnet = None
        self.alarms_max_per_object = None
        self.page_max_size = None
        self.max_response = None
        self.ncpe_bootstrap_endpoint = None
        self.ncpe_config_endpoint = None
        self.ncpe_local_ui_url = None
        self.page_size = None
        self.post_processor_threads_count = None
        self.reflexive_acl_timeout = None
        self.rd_lower_limit = None
        self.rd_public_network_lower_limit = None
        self.rd_public_network_upper_limit = None
        self.rd_upper_limit = None
        self.rt_lower_limit = None
        self.rt_public_network_lower_limit = None
        self.rt_public_network_upper_limit = None
        self.rt_upper_limit = None
        self.offset_service_id = None
        self.service_id_upper_limit = None
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
        self.two_factor_code_expiry = None
        self.two_factor_code_length = None
        self.two_factor_code_seed_length = None
        self.vm_cache_size = None
        self.vm_resync_outstanding_interval = None
        self.vm_purge_time = None
        self.vm_resync_deletion_wait_time = None
        self.vm_unreachable_cleanup_time = None
        self.vm_unreachable_time = None
        self.vnid_lower_limit = None
        self.vnid_public_network_lower_limit = None
        self.vnid_public_network_upper_limit = None
        self.vnid_upper_limit = None
        self.vsc_on_same_version_as_vsd = None
        self.vsd_read_only_mode = None
        self.static_wan_service_purge_time = None

        self.expose_attribute(local_name=u"acl_allow_origin", remote_name=u"ACLAllowOrigin", attribute_type=str)
        self.expose_attribute(local_name=u"api_key_renewal_interval", remote_name=u"APIKeyRenewalInterval", attribute_type=str)
        self.expose_attribute(local_name=u"api_key_validity", remote_name=u"APIKeyValidity", attribute_type=str)
        self.expose_attribute(local_name=u"as_number", remote_name=u"ASNumber", attribute_type=str)
        self.expose_attribute(local_name=u"ad_gateway_purge_time", remote_name=u"ADGatewayPurgeTime", attribute_type=int)
        self.expose_attribute(local_name=u"avatar_base_path", remote_name=u"avatarBasePath", attribute_type=str)
        self.expose_attribute(local_name=u"avatar_base_url", remote_name=u"avatarBaseURL", attribute_type=str)
        self.expose_attribute(local_name=u"offset_customer_id", remote_name=u"offsetCustomerID", attribute_type=str)
        self.expose_attribute(local_name=u"customer_id_upper_limit", remote_name=u"customerIDUpperLimit", attribute_type=str)
        self.expose_attribute(local_name=u"customer_key", remote_name=u"customerKey", attribute_type=str)
        self.expose_attribute(local_name=u"dhcp_option_size", remote_name=u"DHCPOptionSize", attribute_type=int)
        self.expose_attribute(local_name=u"domain_tunnel_type", remote_name=u"domainTunnelType", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_client_key_store", remote_name=u"ejbcaClientKeyStore", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_client_key_store_password", remote_name=u"ejbcaClientKeyStorePassword", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_client_namespace_uri", remote_name=u"ejbcaClientNamespaceUri", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_client_trust_store", remote_name=u"ejbcaClientTrustStore", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_client_trust_store_password", remote_name=u"ejbcaClientTrustStorePassword", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_client_ws_local_part", remote_name=u"ejbcaClientWsLocalPart", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_client_ws_url", remote_name=u"ejbcaClientWsUrl", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_ncpe_certificate_profile", remote_name=u"ejbcaNcpeCertificateProfile", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_ncpe_end_entity_profile", remote_name=u"ejbcaNcpeEndEntityProfile", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_server_hostname", remote_name=u"ejbcaServerHostname", attribute_type=str)
        self.expose_attribute(local_name=u"ejbca_server_port", remote_name=u"ejbcaServerPort", attribute_type=int)
        self.expose_attribute(local_name=u"ejbca_vsp_root_ca", remote_name=u"ejbcaVspRootCa", attribute_type=str)
        self.expose_attribute(local_name=u"esi_id", remote_name=u"esiID", attribute_type=int)
        self.expose_attribute(local_name=u"event_log_cleanup_interval", remote_name=u"eventLogCleanupInterval", attribute_type=str)
        self.expose_attribute(local_name=u"event_log_entry_max_age", remote_name=u"eventLogEntryMaxAge", attribute_type=int)
        self.expose_attribute(local_name=u"event_processor_interval", remote_name=u"eventProcessorInterval", attribute_type=str)
        self.expose_attribute(local_name=u"event_processor_max_events_count", remote_name=u"eventProcessorMaxEventsCount", attribute_type=int)
        self.expose_attribute(local_name=u"event_processor_timeout", remote_name=u"eventProcessorTimeout", attribute_type=str)
        self.expose_attribute(local_name=u"evpnbgp_community_tag_as_number", remote_name=u"EVPNBGPCommunityTagASNumber", attribute_type=str)
        self.expose_attribute(local_name=u"evpnbgp_community_tag_lower_limit", remote_name=u"EVPNBGPCommunityTagLowerLimit", attribute_type=str)
        self.expose_attribute(local_name=u"evpnbgp_community_tag_upper_limit", remote_name=u"EVPNBGPCommunityTagUpperLimit", attribute_type=str)
        self.expose_attribute(local_name=u"inactive_timeout", remote_name=u"inactiveTimeout", attribute_type=str)
        self.expose_attribute(local_name=u"ldap_trust_store_certifcate", remote_name=u"LDAPTrustStoreCertifcate", attribute_type=str)
        self.expose_attribute(local_name=u"ldap_trust_store_password", remote_name=u"LDAPTrustStorePassword", attribute_type=str)
        self.expose_attribute(local_name=u"lru_cache_size_per_subnet", remote_name=u"LRUCacheSizePerSubnet", attribute_type=int)
        self.expose_attribute(local_name=u"alarms_max_per_object", remote_name=u"alarmsMaxPerObject", attribute_type=int)
        self.expose_attribute(local_name=u"page_max_size", remote_name=u"pageMaxSize", attribute_type=int)
        self.expose_attribute(local_name=u"max_response", remote_name=u"maxResponse", attribute_type=int)
        self.expose_attribute(local_name=u"ncpe_bootstrap_endpoint", remote_name=u"ncpeBootstrapEndpoint", attribute_type=str)
        self.expose_attribute(local_name=u"ncpe_config_endpoint", remote_name=u"ncpeConfigEndpoint", attribute_type=str)
        self.expose_attribute(local_name=u"ncpe_local_ui_url", remote_name=u"ncpeLocalUiUrl", attribute_type=str)
        self.expose_attribute(local_name=u"page_size", remote_name=u"pageSize", attribute_type=int)
        self.expose_attribute(local_name=u"post_processor_threads_count", remote_name=u"postProcessorThreadsCount", attribute_type=int)
        self.expose_attribute(local_name=u"reflexive_acl_timeout", remote_name=u"reflexiveACLTimeout", attribute_type=str)
        self.expose_attribute(local_name=u"rd_lower_limit", remote_name=u"RDLowerLimit", attribute_type=str)
        self.expose_attribute(local_name=u"rd_public_network_lower_limit", remote_name=u"RDPublicNetworkLowerLimit", attribute_type=str)
        self.expose_attribute(local_name=u"rd_public_network_upper_limit", remote_name=u"RDPublicNetworkUpperLimit", attribute_type=str)
        self.expose_attribute(local_name=u"rd_upper_limit", remote_name=u"RDUpperLimit", attribute_type=str)
        self.expose_attribute(local_name=u"rt_lower_limit", remote_name=u"RTLowerLimit", attribute_type=str)
        self.expose_attribute(local_name=u"rt_public_network_lower_limit", remote_name=u"RTPublicNetworkLowerLimit", attribute_type=str)
        self.expose_attribute(local_name=u"rt_public_network_upper_limit", remote_name=u"RTPublicNetworkUpperLimit", attribute_type=str)
        self.expose_attribute(local_name=u"rt_upper_limit", remote_name=u"RTUpperLimit", attribute_type=str)
        self.expose_attribute(local_name=u"offset_service_id", remote_name=u"offsetServiceID", attribute_type=str)
        self.expose_attribute(local_name=u"service_id_upper_limit", remote_name=u"serviceIDUpperLimit", attribute_type=str)
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
        self.expose_attribute(local_name=u"two_factor_code_expiry", remote_name=u"twoFactorCodeExpiry", attribute_type=int)
        self.expose_attribute(local_name=u"two_factor_code_length", remote_name=u"twoFactorCodeLength", attribute_type=int)
        self.expose_attribute(local_name=u"two_factor_code_seed_length", remote_name=u"twoFactorCodeSeedLength", attribute_type=int)
        self.expose_attribute(local_name=u"vm_cache_size", remote_name=u"VMCacheSize", attribute_type=int)
        self.expose_attribute(local_name=u"vm_resync_outstanding_interval", remote_name=u"VMResyncOutstandingInterval", attribute_type=int)
        self.expose_attribute(local_name=u"vm_purge_time", remote_name=u"VMPurgeTime", attribute_type=int)
        self.expose_attribute(local_name=u"vm_resync_deletion_wait_time", remote_name=u"VMResyncDeletionWaitTime", attribute_type=int)
        self.expose_attribute(local_name=u"vm_unreachable_cleanup_time", remote_name=u"VMUnreachableCleanupTime", attribute_type=int)
        self.expose_attribute(local_name=u"vm_unreachable_time", remote_name=u"VMUnreachableTime", attribute_type=int)
        self.expose_attribute(local_name=u"vnid_lower_limit", remote_name=u"VNIDLowerLimit", attribute_type=int)
        self.expose_attribute(local_name=u"vnid_public_network_lower_limit", remote_name=u"VNIDPublicNetworkLowerLimit", attribute_type=int)
        self.expose_attribute(local_name=u"vnid_public_network_upper_limit", remote_name=u"VNIDPublicNetworkUpperLimit", attribute_type=int)
        self.expose_attribute(local_name=u"vnid_upper_limit", remote_name=u"VNIDUpperLimit", attribute_type=int)
        self.expose_attribute(local_name=u"vsc_on_same_version_as_vsd", remote_name=u"VSCOnSameVersionAsVSD", attribute_type=bool)
        self.expose_attribute(local_name=u"vsd_read_only_mode", remote_name=u"VSDReadOnlyMode", attribute_type=bool)
        self.expose_attribute(local_name=u"static_wan_service_purge_time", remote_name=u"staticWANServicePurgeTime", attribute_type=int)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"systemconfig"

    # REST methods
