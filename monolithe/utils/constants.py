# -*- coding: utf-8 -*-


class Constants(object):
    """ List all constants and mapping information

    """
    # Constants
    INVARIANT_NAMES = ['qos', 'vrs', 'cms', 'statistics']
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    HTTP_PROTOCOLS = ['http', 'https', 'ftp']

    IGNORED_ATTRIBUTES = ["_fetchers", "creationDate", "parentID", "owner", "parentType", "lastUpdatedBy", "lastUpdatedDate", "externalID", "ID" ]
    IGNORED_RESOURCES = ['PublicNetworkMacro', 'NetworkLayout', 'InfrastructureConfig']

    # Entities
    USER = 'User'
    RESTUSER = 'RESTUser'

    # Mapping
    RESOURCE_MAPPING = {
        'SubNetwork': 'Subnet',
        'SubNetworkTemplate': 'SubnetTemplate',
        'PortStatus': 'MonitoringPort',
        'EnterpriseNetworkMacro': 'EnterpriseNetwork',
        'RedundantGWGrp': 'RedundancyGroup',
        'Service': 'ApplicationService',
        'IPBinding': 'IPReservation',
        'VPNConnect': 'VPNConnection',
        'QosPrimitive': 'QOS',  # Not working because resource name is 'qos' instead of 'quoss'
        'EgressQosPrimitive': 'EgressQOSPolicy',
        'EgressACLTemplateEntry': 'EgressACLEntryTemplate',
        'IngressACLTemplateEntry': 'IngressACLEntryTemplate',
        'IngressAdvancedForwardingTemplate': 'IngressAdvFwdTemplate',
        'IngressAdvancedForwardingTemplateEntry': 'IngressAdvFwdEntryTemplate',
        'AutoDiscGateway': 'AutoDiscoveredGateway',
        'VirtualMachine': 'VM',
        'Vlan': 'VLAN',
        'VlanTemplate': 'VLANTemplate'
    }

    PACKAGE_MAPPING = {
        '/alarm': 'Alarms',
        '/appd': 'Application Designer',
        '/common': 'Metadata',
        '/eventlog': 'Event Logs',
        '/gateway': 'Gateway Management',
        '/infrastructure': 'Infrastructure Profiles',
        '/job': 'Jobs',
        '/licensemgmt': 'Licensing',
        '/network': 'Core Networking',
        '/nsg': 'Gateway Management',
        '/policy': 'Policies',
        '/policy/acl': 'Security Policies',
        '/policy/qos': 'Policies',
        '/stats': 'Statistics',
        '/sysmon': 'System Monitoring',
        '/systemconfig': 'System Configuration',
        '/usermgmt': 'User Management',
        '/vm': 'Virtual Machines',
        '/vport': 'Core Networking',
        '/certificate': 'Certificate',
        '/cms': 'Cloud Management System',
        '/ipsec': 'IP Sec',
        '/keyserver': 'Key Server',
        '/vmware': 'VMware',
    }

    ATTRIBUTE_MAPPING = {
        'global': 'globalMetadata'
    }
    