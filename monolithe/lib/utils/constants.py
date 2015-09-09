# -*- coding: utf-8 -*-


class Constants(object):
    """ List all constants and mapping information

    """
    DEVELOPMENT_MODE = True

    # Constants
    INVARIANT_NAMES = ['qos', 'cms', 'statistics']
    PLURABLE_NAMES = ['vrs']  # Plurable makes no sense. Hint: neither this code.
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    HTTP_PROTOCOLS = ['http', 'https', 'ftp']

    IGNORED_ATTRIBUTES = ["_fetchers", "creationDate", "parentID", "owner", "parentType", "lastUpdatedBy", "lastUpdatedDate", "externalID", "ID"]
    IGNORED_RESOURCES = ['PublicNetworkMacro', 'NetworkLayout', 'InfrastructureConfig']

    CODEGEN_DIRECTORY = './codegen'
    DOCS_DIRECTORY = './docgen'
    SPECGEN_DIRECTORY = './specgen'

    # HTTP methods
    HTTP_METHOD_POST = 'POST'
    HTTP_METHOD_GET = 'GET'
    HTTP_METHOD_DELETE = 'DELETE'
    HTTP_METHOD_UPDATE = 'PUT'

    # Entities
    USER = u'User'
    USER_REST_NAME = u'user'
    RESTUSER = u'RESTUser'
    RESTUSER_REST_NAME = u'me'

    # Mapping
    RESOURCE_MAPPING = {
        u'AutoDiscGateway': u'AutoDiscoveredGateway',
        u'EgressACLTemplateEntry': u'EgressACLEntryTemplate',
        u'EgressQosPrimitive': u'EgressQOSPolicy',
        u'EnterpriseNetworkMacro': u'EnterpriseNetwork',
        u'IngressACLTemplateEntry': u'IngressACLEntryTemplate',
        u'IngressAdvancedForwardingTemplate': u'IngressAdvFwdTemplate',
        u'IngressAdvancedForwardingTemplateEntry': u'IngressAdvFwdEntryTemplate',
        u'IPBinding': u'IPReservation',
        u'PortStatus': u'MonitoringPort',
        u'QosPrimitive': u'QOS',  # Not working because resource name is 'qos' instead of 'quoss'
        u'RedundantGWGrp': u'RedundancyGroup',
        u'Service': u'ApplicationService',
        u'SubNetwork': u'Subnet',
        u'SubNetworkTemplate': u'SubnetTemplate',
        u'VirtualMachine': u'VM',
        u'Vlan': u'VLAN',
        u'VlanTemplate': u'VLANTemplate',
        u'VPNConnect': u'VPNConnection',
    }

    ATTRIBUTE_MAPPING = {
        u'global': u'globalMetadata',
    }

    REST_NAME_MAPPING = {
        u'allalarm': u'alarm',
    }

    PROTOCOL_TYPES = {u'TCP': u'6',
                      u'UDP': u'7',
                      u'ICMP': u'1',
                      u'IGMP': u'2',
                      u'IGP': u'9',
                      u'OSPF': u'9',
                      u'ESP': u'0',
                      u'AH': u'1',
                      u'GRE': u'7',
    }
