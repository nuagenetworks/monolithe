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
        u'SubNetwork': u'Subnet',
        u'SubNetworkTemplate': u'SubnetTemplate',
        u'PortStatus': u'MonitoringPort',
        u'EnterpriseNetworkMacro': u'EnterpriseNetwork',
        u'RedundantGWGrp': u'RedundancyGroup',
        u'Service': u'ApplicationService',
        u'IPBinding': u'IPReservation',
        u'VPNConnect': u'VPNConnection',
        u'QosPrimitive': u'QOS',  # Not working because resource name is 'qos' instead of 'quoss'
        u'EgressQosPrimitive': u'EgressQOSPolicy',
        u'EgressACLTemplateEntry': u'EgressACLEntryTemplate',
        u'IngressACLTemplateEntry': u'IngressACLEntryTemplate',
        u'IngressAdvancedForwardingTemplate': u'IngressAdvFwdTemplate',
        u'IngressAdvancedForwardingTemplateEntry': u'IngressAdvFwdEntryTemplate',
        u'AutoDiscGateway': u'AutoDiscoveredGateway',
        u'VirtualMachine': u'VM',
        u'Vlan': u'VLAN',
        u'VlanTemplate': u'VLANTemplate'
    }

    PACKAGE_MAPPING = {
        u'/alarm': u'Alarms',
        u'/appd': u'Application Designer',
        u'/common': u'Metadata',
        u'/eventlog': u'Event Logs',
        u'/gateway': u'Gateway Management',
        u'/infrastructure': u'Infrastructure Profiles',
        u'/job': u'Jobs',
        u'/licensemgmt': u'Licensing',
        u'/network': u'Core Networking',
        u'/nsg': u'Gateway Management',
        u'/policy': u'Policies',
        u'/policy/acl': u'Security Policies',
        u'/policy/qos': u'Policies',
        u'/stats': u'Statistics',
        u'/sysmon': u'System Monitoring',
        u'/systemconfig': u'System Configuration',
        u'/usermgmt': u'User Management',
        u'/vm': u'Virtual Machines',
        u'/vport': u'Core Networking',
        u'/certificate': u'Certificate',
        u'/cms': u'Cloud Management System',
        u'/ipsec': u'IP Sec',
        u'/keyserver': u'Key Server',
        u'/vmware': u'VMware',
    }

    ATTRIBUTE_MAPPING = {
        u'global': u'globalMetadata'
    }    