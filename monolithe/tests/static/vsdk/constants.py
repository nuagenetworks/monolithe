# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.


class AddressRangeDHCPPoolType(object):
    """ AddressRangeDHCPPoolType """

    BRIDGE = u"BRIDGE"
    HOST = u"HOST"
    

class AlarmSeverity(object):
    """ AlarmSeverity """

    INFO = u"INFO"
    CRITICAL = u"CRITICAL"
    MAJOR = u"MAJOR"
    WARNING = u"WARNING"
    MINOR = u"MINOR"
    

class ApplicationServiceDirection(object):
    """ ApplicationServiceDirection """

    BIDIRECTIONAL = u"BIDIRECTIONAL"
    UNIDIRECTIONAL = u"UNIDIRECTIONAL"
    REFLEXIVE = u"REFLEXIVE"
    

class AutoDiscoveredGatewayPersonality(object):
    """ AutoDiscoveredGatewayPersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class BGPPeerStatus(object):
    """ BGPPeerStatus """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class BootstrapStatus(object):
    """ BootstrapStatus """

    NOTIFICATION_APP_REQ_SENT = u"NOTIFICATION_APP_REQ_SENT"
    ACTIVE = u"ACTIVE"
    CERTIFICATE_SIGNED = u"CERTIFICATE_SIGNED"
    INACTIVE = u"INACTIVE"
    NOTIFICATION_APP_REQ_ACK = u"NOTIFICATION_APP_REQ_ACK"
    

class DSCPForwardingClassMappingForwardingClass(object):
    """ DSCPForwardingClassMappingForwardingClass """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class DomainApplicationDeploymentPolicy(object):
    """ DomainApplicationDeploymentPolicy """

    NONE = u"NONE"
    ZONE = u"ZONE"
    

class DomainDHCPBehavior(object):
    """ DomainDHCPBehavior """

    FLOOD = u"FLOOD"
    CONSUME = u"CONSUME"
    RELAY = u"RELAY"
    

class DomainPATEnabled(object):
    """ DomainPATEnabled """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class DomainTunnelType(object):
    """ DomainTunnelType """

    DC_DEFAULT = u"DC_DEFAULT"
    VXLAN = u"VXLAN"
    GRE = u"GRE"
    

class EgressACLEntryTemplateAction(object):
    """ EgressACLEntryTemplateAction """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class EgressACLEntryTemplateAssociatedApplicationObjectType(object):
    """ EgressACLEntryTemplateAssociatedApplicationObjectType """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class EgressACLEntryTemplateLocationType(object):
    """ EgressACLEntryTemplateLocationType """

    VPORTTAG = u"VPORTTAG"
    REDIRECTIONTARGET = u"REDIRECTIONTARGET"
    ZONE = u"ZONE"
    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ANY = u"ANY"
    

class EgressACLEntryTemplateNetworkType(object):
    """ EgressACLEntryTemplateNetworkType """

    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ENDPOINT_DOMAIN = u"ENDPOINT_DOMAIN"
    ZONE = u"ZONE"
    ENDPOINT_ZONE = u"ENDPOINT_ZONE"
    ENDPOINT_SUBNET = u"ENDPOINT_SUBNET"
    PUBLIC_NETWORK = u"PUBLIC_NETWORK"
    ENTERPRISE_NETWORK = u"ENTERPRISE_NETWORK"
    ANY = u"ANY"
    

class EgressQOSPolicyQueue1ForwardingClasses(object):
    """ EgressQOSPolicyQueue1ForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class EgressQOSPolicyQueue2ForwardingClasses(object):
    """ EgressQOSPolicyQueue2ForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class EgressQOSPolicyQueue3ForwardingClasses(object):
    """ EgressQOSPolicyQueue3ForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class EgressQOSPolicyQueue4ForwardingClasses(object):
    """ EgressQOSPolicyQueue4ForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class EnterpriseAllowedForwardingClasses(object):
    """ EnterpriseAllowedForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class EnterpriseAvatarType(object):
    """ EnterpriseAvatarType """

    URL = u"URL"
    COMPUTEDURL = u"COMPUTEDURL"
    BASE64 = u"BASE64"
    

class EnterpriseProfileAllowedForwardingClasses(object):
    """ EnterpriseProfileAllowedForwardingClasses """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class GatewayPersonality(object):
    """ GatewayPersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class GatewayTemplatePersonality(object):
    """ GatewayTemplatePersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class GroupRole(object):
    """ GroupRole """

    SUPER_USER_ROLES = u"SUPER_USER_ROLES"
    CSPOPERATOR = u"CSPOPERATOR"
    ORGADMIN = u"ORGADMIN"
    JMS = u"JMS"
    SYSTEM = u"SYSTEM"
    CSPROOT = u"CSPROOT"
    ORGAPPDESIGNER = u"ORGAPPDESIGNER"
    SUPER_USER_SET_VALUES = u"SUPER_USER_SET_VALUES"
    ORGNETWORKDESIGNER = u"ORGNETWORKDESIGNER"
    UNKNOWN = u"UNKNOWN"
    ORGUSER = u"ORGUSER"
    CMS = u"CMS"
    USER = u"USER"
    

class HSCStatus(object):
    """ HSCStatus """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class HSCType(object):
    """ HSCType """

    VSA = u"VSA"
    NONE = u"NONE"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    

class IPType(object):
    """ IPType """

    IPV4 = u"IPV4"
    IPV6 = u"IPV6"
    

class InfrastructureGatewayProfileDeadTimer(object):
    """ InfrastructureGatewayProfileDeadTimer """

    TEN_MINUTES = u"TEN_MINUTES"
    NONE = u"NONE"
    TWO_HOURS = u"TWO_HOURS"
    ONE_HOUR = u"ONE_HOUR"
    SIX_HOURS = u"SIX_HOURS"
    THREE_HOURS = u"THREE_HOURS"
    FOUR_HOURS = u"FOUR_HOURS"
    THIRTY_MINUTES = u"THIRTY_MINUTES"
    MAXIMUM_DURATION = u"MAXIMUM_DURATION"
    FIVE_HOURS = u"FIVE_HOURS"
    

class InfrastructureGatewayProfileRemoteLogMode(object):
    """ InfrastructureGatewayProfileRemoteLogMode """

    DISABLED = u"DISABLED"
    SCP = u"SCP"
    RSYSLOG = u"RSYSLOG"
    SFTP = u"SFTP"
    

class InfrastructureGatewayProfileSystemSyncWindow(object):
    """ InfrastructureGatewayProfileSystemSyncWindow """

    TEN_MINUTES = u"TEN_MINUTES"
    NONE = u"NONE"
    TWO_HOURS = u"TWO_HOURS"
    ONE_HOUR = u"ONE_HOUR"
    SIX_HOURS = u"SIX_HOURS"
    THREE_HOURS = u"THREE_HOURS"
    FOUR_HOURS = u"FOUR_HOURS"
    THIRTY_MINUTES = u"THIRTY_MINUTES"
    MAXIMUM_DURATION = u"MAXIMUM_DURATION"
    FIVE_HOURS = u"FIVE_HOURS"
    

class InfrastructureGatewayProfileUpgradeAction(object):
    """ InfrastructureGatewayProfileUpgradeAction """

    DOWNLOAD_ONLY = u"DOWNLOAD_ONLY"
    DOWNLOAD_AND_UPGRADE_AT_WINDOW = u"DOWNLOAD_AND_UPGRADE_AT_WINDOW"
    UPGRADE_NOW = u"UPGRADE_NOW"
    NONE = u"NONE"
    DOWNLOAD_AND_UPGRADE_NOW = u"DOWNLOAD_AND_UPGRADE_NOW"
    

class InfrastructurePortProfileDuplex(object):
    """ InfrastructurePortProfileDuplex """

    FULL = u"FULL"
    SIMPLEX = u"SIMPLEX"
    HALF = u"HALF"
    

class InfrastructurePortProfileSpeed(object):
    """ InfrastructurePortProfileSpeed """

    BASEX10G = u"BASEX10G"
    BASETX100 = u"BASETX100"
    AUTONEGOTIATE = u"AUTONEGOTIATE"
    BASET1000 = u"BASET1000"
    BASET10 = u"BASET10"
    

class IngressACLEntryTemplateAction(object):
    """ IngressACLEntryTemplateAction """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class IngressACLEntryTemplateAssociatedApplicationObjectType(object):
    """ IngressACLEntryTemplateAssociatedApplicationObjectType """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class IngressACLEntryTemplateLocationType(object):
    """ IngressACLEntryTemplateLocationType """

    VPORTTAG = u"VPORTTAG"
    REDIRECTIONTARGET = u"REDIRECTIONTARGET"
    ZONE = u"ZONE"
    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ANY = u"ANY"
    

class IngressACLEntryTemplateNetworkType(object):
    """ IngressACLEntryTemplateNetworkType """

    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ENDPOINT_DOMAIN = u"ENDPOINT_DOMAIN"
    ZONE = u"ZONE"
    ENDPOINT_ZONE = u"ENDPOINT_ZONE"
    ENDPOINT_SUBNET = u"ENDPOINT_SUBNET"
    PUBLIC_NETWORK = u"PUBLIC_NETWORK"
    ENTERPRISE_NETWORK = u"ENTERPRISE_NETWORK"
    ANY = u"ANY"
    

class IngressAdvFwdEntryTemplateAction(object):
    """ IngressAdvFwdEntryTemplateAction """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class IngressAdvFwdEntryTemplateAssociatedApplicationObjectType(object):
    """ IngressAdvFwdEntryTemplateAssociatedApplicationObjectType """

    FORWARD = u"FORWARD"
    REDIRECT = u"REDIRECT"
    DROP = u"DROP"
    

class IngressAdvFwdEntryTemplateFCOverride(object):
    """ IngressAdvFwdEntryTemplateFCOverride """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class IngressAdvFwdEntryTemplateLocationType(object):
    """ IngressAdvFwdEntryTemplateLocationType """

    VPORTTAG = u"VPORTTAG"
    REDIRECTIONTARGET = u"REDIRECTIONTARGET"
    ZONE = u"ZONE"
    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ANY = u"ANY"
    

class IngressAdvFwdEntryTemplateNetworkType(object):
    """ IngressAdvFwdEntryTemplateNetworkType """

    SUBNET = u"SUBNET"
    POLICYGROUP = u"POLICYGROUP"
    ENDPOINT_DOMAIN = u"ENDPOINT_DOMAIN"
    ZONE = u"ZONE"
    ENDPOINT_ZONE = u"ENDPOINT_ZONE"
    ENDPOINT_SUBNET = u"ENDPOINT_SUBNET"
    PUBLIC_NETWORK = u"PUBLIC_NETWORK"
    ENTERPRISE_NETWORK = u"ENTERPRISE_NETWORK"
    ANY = u"ANY"
    

class JobCommand(object):
    """ JobCommand """

    CERTIFICATE_NSG_REVOKE = u"CERTIFICATE_NSG_REVOKE"
    NOTIFY_NSG_REGISTRATION = u"NOTIFY_NSG_REGISTRATION"
    CERTIFICATE_NSG_RENEW = u"CERTIFICATE_NSG_RENEW"
    RELOAD_NSG_CONFIG = u"RELOAD_NSG_CONFIG"
    RELOAD = u"RELOAD"
    GATEWAY_AUDIT = u"GATEWAY_AUDIT"
    EXPORT = u"EXPORT"
    NOTIFY_NSG_REGISTRATION_ACK = u"NOTIFY_NSG_REGISTRATION_ACK"
    IMPORT = u"IMPORT"
    

class JobStatus(object):
    """ JobStatus """

    FAILED = u"FAILED"
    RUNNING = u"RUNNING"
    SUCCESS = u"SUCCESS"
    

class LicenseLicenseType(object):
    """ LicenseLicenseType """

    CLUSTERED = u"CLUSTERED"
    STANDARD = u"STANDARD"
    

class MaintenanceMode(object):
    """ MaintenanceMode """

    DISABLED = u"DISABLED"
    ENABLED_INHERITED = u"ENABLED_INHERITED"
    ENABLED = u"ENABLED"
    

class MonitoringPortState(object):
    """ MonitoringPortState """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class Multicast(object):
    """ Multicast """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class NSGatewayConfigurationReloadState(object):
    """ NSGatewayConfigurationReloadState """

    APPLIED = u"APPLIED"
    UNKNOWN = u"UNKNOWN"
    PENDING = u"PENDING"
    SENT = u"SENT"
    

class NSGatewayConfigurationStatus(object):
    """ NSGatewayConfigurationStatus """

    UNKNOWN = u"UNKNOWN"
    SUCCESS = u"SUCCESS"
    FAILURE = u"FAILURE"
    

class NetworkLayoutServiceType(object):
    """ NetworkLayoutServiceType """

    SUBNET_ONLY = u"SUBNET_ONLY"
    ROUTER_ONLY = u"ROUTER_ONLY"
    ROUTER_SWITCH = u"ROUTER_SWITCH"
    

class PermittedAction(object):
    """ PermittedAction """

    READ = u"READ"
    USE = u"USE"
    INSTANTIATE = u"INSTANTIATE"
    ALL = u"ALL"
    EXTEND = u"EXTEND"
    

class PermittedActionPermittedEntityID(object):
    """ PermittedActionPermittedEntityID """

    HASHING_SEED = u"HASHING_SEED"
    CASE_INSENSITIVE_ORDER = u"CASE_INSENSITIVE_ORDER"
    

class PolicyGroupTemplateType(object):
    """ PolicyGroupTemplateType """

    HARDWARE = u"HARDWARE"
    SOFTWARE = u"SOFTWARE"
    

class PolicyGroupType(object):
    """ PolicyGroupType """

    HARDWARE = u"HARDWARE"
    SOFTWARE = u"SOFTWARE"
    

class PortPortType(object):
    """ PortPortType """

    ACCESS = u"ACCESS"
    NETWORK = u"NETWORK"
    

class PortStatus(object):
    """ PortStatus """

    READY = u"READY"
    MISMATCH = u"MISMATCH"
    ORPHAN = u"ORPHAN"
    INITIALIZED = u"INITIALIZED"
    

class PortTemplatePortType(object):
    """ PortTemplatePortType """

    ACCESS = u"ACCESS"
    NETWORK = u"NETWORK"
    

class ProtocolType(object):
    """ ProtocolType """

    UDP = u"7"
    GRE = u"7"
    ESP = u"0"
    IGP = u"9"
    AH = u"1"
    ICMP = u"1"
    OSPF = u"9"
    TCP = u"6"
    IGMP = u"2"
    

class QOSServiceClass(object):
    """ QOSServiceClass """

    A = u"A"
    C = u"C"
    B = u"B"
    E = u"E"
    D = u"D"
    G = u"G"
    F = u"F"
    H = u"H"
    NONE = u"NONE"
    

class RESTUserAvatarType(object):
    """ RESTUserAvatarType """

    URL = u"URL"
    COMPUTEDURL = u"COMPUTEDURL"
    BASE64 = u"BASE64"
    

class RedirectionTargetEndPointType(object):
    """ RedirectionTargetEndPointType """

    NONE = u"NONE"
    L3 = u"L3"
    VIRTUAL_WIRE = u"VIRTUAL_WIRE"
    

class RedirectionTargetTriggerType(object):
    """ RedirectionTargetTriggerType """

    NONE = u"NONE"
    GARP = u"GARP"
    

class RedundancyGroupPersonality(object):
    """ RedundancyGroupPersonality """

    VRSG = u"VRSG"
    OTHER = u"OTHER"
    NSG = u"NSG"
    VSA = u"VSA"
    DC7X50 = u"DC7X50"
    VSG = u"VSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    

class RedundancyGroupRedundantGatewayStatus(object):
    """ RedundancyGroupRedundantGatewayStatus """

    FAILED = u"FAILED"
    SUCCESS = u"SUCCESS"
    

class SharedNetworkResourceType(object):
    """ SharedNetworkResourceType """

    FLOATING = u"FLOATING"
    REGULAR = u"REGULAR"
    UPLINK_SUBNET = u"UPLINK_SUBNET"
    L2DOMAIN = u"L2DOMAIN"
    PUBLIC = u"PUBLIC"
    

class SubnetPATEnabled(object):
    """ SubnetPATEnabled """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class SystemConfigDomainTunnelType(object):
    """ SystemConfigDomainTunnelType """

    DC_DEFAULT = u"DC_DEFAULT"
    VXLAN = u"VXLAN"
    GRE = u"GRE"
    

class TCAMetric(object):
    """ TCAMetric """

    PACKETS_OUT = u"PACKETS_OUT"
    PACKETS_OUT_DROPPED = u"PACKETS_OUT_DROPPED"
    PACKETS_OUT_ERROR = u"PACKETS_OUT_ERROR"
    BYTES_IN = u"BYTES_IN"
    PACKETS_IN_ERROR = u"PACKETS_IN_ERROR"
    PACKETS_IN_DROPPED = u"PACKETS_IN_DROPPED"
    BYTES_OUT = u"BYTES_OUT"
    PACKETS_DROPPED_BY_RATE_LIMIT = u"PACKETS_DROPPED_BY_RATE_LIMIT"
    PACKETS_IN = u"PACKETS_IN"
    

class TCAScope(object):
    """ TCAScope """

    GLOBAL = u"GLOBAL"
    LOCAL = u"LOCAL"
    

class TCAType(object):
    """ TCAType """

    ROLLING_AVERAGE = u"ROLLING_AVERAGE"
    BREACH = u"BREACH"
    

class TierType(object):
    """ TierType """

    APPLICATION_EXTENDED_NETWORK = u"APPLICATION_EXTENDED_NETWORK"
    APPLICATION = u"APPLICATION"
    NETWORK_MACRO = u"NETWORK_MACRO"
    STANDARD = u"STANDARD"
    

class UserAvatarType(object):
    """ UserAvatarType """

    URL = u"URL"
    COMPUTEDURL = u"COMPUTEDURL"
    BASE64 = u"BASE64"
    

class VLANStatus(object):
    """ VLANStatus """

    READY = u"READY"
    MISMATCH = u"MISMATCH"
    ORPHAN = u"ORPHAN"
    INITIALIZED = u"INITIALIZED"
    

class VMReasonType(object):
    """ VMReasonType """

    PAUSED_DUMP = u"PAUSED_DUMP"
    SHUTOFF_UNKNOWN = u"SHUTOFF_UNKNOWN"
    PAUSED_MIGRATION = u"PAUSED_MIGRATION"
    RUNNING_UNKNOWN = u"RUNNING_UNKNOWN"
    SHUTOFF_DESTROYED = u"SHUTOFF_DESTROYED"
    UNKNOWN = u"UNKNOWN"
    FROM_SNAPSHOT = u"FROM_SNAPSHOT"
    PAUSED_SHUTTING_DOWN = u"PAUSED_SHUTTING_DOWN"
    SHUTOFF_FROM_SNAPSHOT = u"SHUTOFF_FROM_SNAPSHOT"
    USER = u"USER"
    RUNNING_MIGRATED = u"RUNNING_MIGRATED"
    CRASHED_UNKNOWN = u"CRASHED_UNKNOWN"
    PAUSED_SAVE = u"PAUSED_SAVE"
    LAST = u"LAST"
    RUNNING_RESTORED = u"RUNNING_RESTORED"
    SHUTDOWN_USER = u"SHUTDOWN_USER"
    RUNNING_LAST = u"RUNNING_LAST"
    SHUTOFF_LAST = u"SHUTOFF_LAST"
    SHUTDOWN_UNKNOWN = u"SHUTDOWN_UNKNOWN"
    RUNNING_MIGRATION_CANCELED = u"RUNNING_MIGRATION_CANCELED"
    PAUSED_LAST = u"PAUSED_LAST"
    NOSTATE_UNKNOWN = u"NOSTATE_UNKNOWN"
    PAUSED_UNKNOWN = u"PAUSED_UNKNOWN"
    RUNNING_BOOTED = u"RUNNING_BOOTED"
    MIGRATED = u"MIGRATED"
    UNKNOWN_VAL = u"UNKNOWN_VAL"
    PAUSED_USER = u"PAUSED_USER"
    CRASHED_LAST = u"CRASHED_LAST"
    RUNNING_FROM_SNAPSHOT = u"RUNNING_FROM_SNAPSHOT"
    SHUTOFF_SHUTDOWN = u"SHUTOFF_SHUTDOWN"
    SHUTOFF_CRASHED = u"SHUTOFF_CRASHED"
    SHUTOFF_MIGRATED = u"SHUTOFF_MIGRATED"
    RUNNING_SAVE_CANCELED = u"RUNNING_SAVE_CANCELED"
    RUNNING_UNPAUSED = u"RUNNING_UNPAUSED"
    PAUSED_IOERROR = u"PAUSED_IOERROR"
    PAUSED_FROM_SNAPSHOT = u"PAUSED_FROM_SNAPSHOT"
    BLOCKED_LAST = u"BLOCKED_LAST"
    SHUTOFF_SAVED = u"SHUTOFF_SAVED"
    NOSTATE_LAST = u"NOSTATE_LAST"
    SHUTDOWN_LAST = u"SHUTDOWN_LAST"
    SHUTOFF_FAILED = u"SHUTOFF_FAILED"
    PAUSED_WATCHDOG = u"PAUSED_WATCHDOG"
    BLOCKED_UNKNOWN = u"BLOCKED_UNKNOWN"
    

class VMResyncStatus(object):
    """ VMResyncStatus """

    IN_PROGRESS = u"IN_PROGRESS"
    SUCCESS = u"SUCCESS"
    

class VMStatus(object):
    """ VMStatus """

    INIT = u"INIT"
    LAST = u"LAST"
    NOSTATE = u"NOSTATE"
    UNKNOWN = u"UNKNOWN"
    SHUTOFF = u"SHUTOFF"
    PAUSED = u"PAUSED"
    CRASHED = u"CRASHED"
    RUNNING = u"RUNNING"
    DELETE_PENDING = u"DELETE_PENDING"
    SHUTDOWN = u"SHUTDOWN"
    UNREACHABLE = u"UNREACHABLE"
    BLOCKED = u"BLOCKED"
    

class VPortAddressSpoofing(object):
    """ VPortAddressSpoofing """

    DISABLED = u"DISABLED"
    ENABLED = u"ENABLED"
    INHERITED = u"INHERITED"
    

class VPortMirrorMirrorDirection(object):
    """ VPortMirrorMirrorDirection """

    BOTH = u"BOTH"
    INGRESS = u"INGRESS"
    EGRESS = u"EGRESS"
    

class VPortOperationalState(object):
    """ VPortOperationalState """

    DOWN = u"DOWN"
    INIT = u"INIT"
    UP = u"UP"
    

class VPortSystemType(object):
    """ VPortSystemType """

    NUAGE_VRSG = u"NUAGE_VRSG"
    HARDWARE = u"HARDWARE"
    NUAGE_2 = u"NUAGE_2"
    NUAGE_1 = u"NUAGE_1"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    SOFTWARE = u"SOFTWARE"
    

class VPortType(object):
    """ VPortType """

    BRIDGE = u"BRIDGE"
    HOST = u"HOST"
    VM = u"VM"
    

class VRSClusterNodeRole(object):
    """ VRSClusterNodeRole """

    NONE = u"NONE"
    PRIMARY = u"PRIMARY"
    SECONDARY = u"SECONDARY"
    

class VRSHypervisorConnectionState(object):
    """ VRSHypervisorConnectionState """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class VRSJSONRPCConnectionState(object):
    """ VRSJSONRPCConnectionState """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class VRSPersonality(object):
    """ VRSPersonality """

    VRS = u"VRS"
    VRSG = u"VRSG"
    HARDWARE_VTEP = u"HARDWARE_VTEP"
    NONE = u"NONE"
    NSG = u"NSG"
    

class VRSRole(object):
    """ VRSRole """

    MASTER = u"MASTER"
    NONE = u"NONE"
    SLAVE = u"SLAVE"
    

class VRSStatus(object):
    """ VRSStatus """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class VSCStatus(object):
    """ VSCStatus """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class VSDComponentStatus(object):
    """ VSDComponentStatus """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class VSDComponentType(object):
    """ VSDComponentType """

    MEDIATOR = u"MEDIATOR"
    JBOSS = u"JBOSS"
    PERCONA = u"PERCONA"
    EJABBERD = u"EJABBERD"
    STATSSERVER = u"STATSSERVER"
    STATSCOLLECTOR = u"STATSCOLLECTOR"
    TCA = u"TCA"
    

class VSDMode(object):
    """ VSDMode """

    CLUSTER = u"CLUSTER"
    STANDALONE = u"STANDALONE"
    

class VSDStatus(object):
    """ VSDStatus """

    DOWN = u"DOWN"
    DEGRADED = u"DEGRADED"
    UP = u"UP"
    ADMIN_DOWN = u"ADMIN_DOWN"
    

class WANServiceConfigType(object):
    """ WANServiceConfigType """

    DYNAMIC = u"DYNAMIC"
    STATIC = u"STATIC"
    

class WANServiceServiceType(object):
    """ WANServiceServiceType """

    L2 = u"L2"
    L3 = u"L3"
    

class WANServiceTunnelType(object):
    """ WANServiceTunnelType """

    DC_DEFAULT = u"DC_DEFAULT"
    VXLAN = u"VXLAN"
    GRE = u"GRE"
    
