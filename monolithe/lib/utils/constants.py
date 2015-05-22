# -*- coding: utf-8 -*-


class Constants(object):
    """ List all constants and mapping information

    """
    DEVELOPMENT_MODE = True

    # Constants
    INVARIANT_NAMES = ['qos', 'vrs', 'cms', 'statistics']
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    HTTP_PROTOCOLS = ['http', 'https', 'ftp']

    IGNORED_ATTRIBUTES = ["_fetchers", "creationDate", "parentID", "owner", "parentType", "lastUpdatedBy", "lastUpdatedDate", "externalID", "ID"]
    IGNORED_RESOURCES = ['PublicNetworkMacro', 'NetworkLayout', 'InfrastructureConfig']

    DEFAULT_SPECIFICATION_PATH = u'/templates/specifications/default_specification.json'
    DEFAULT_ATTRIBUTE_PATH = u'/templates/specifications/default_attribute.json'
    DEFAULT_API_PATH = u'/templates/specifications/default_api.json'

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
        u'VlanTemplate': u'VLANTemplate',
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
