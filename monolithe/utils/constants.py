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

    DEFAULT_SPECIFICATION_PATH = u'/templates/specifications/default_specification.json'
    DEFAULT_ATTRIBUTE_PATH = u'/templates/specifications/default_attribute.json'
    DEFAULT_API_PATH = u'/templates/specifications/default_api.json'

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
        u'VlanTemplate': u'VLANTemplate'
    }

    ATTRIBUTE_MAPPING = {
        u'global': u'globalMetadata'
    }

    REST_NAME_MAPPING = {
        u'allalarm': u'alarm'
    }    