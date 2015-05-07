# -*- coding: utf-8 -*-

import re
from copy import deepcopy

from .utils import Utils
from .printer import Printer

USER = 'User'
RESTUSER = 'RESTUser'

IGNORED_ATTRIBUTES = ["_fetchers"]

ATTRIBUTE_MAPPING = {
    'global': 'globalMetadata'
}

IGNORED_RESOURCES = ['PublicNetworkMacro', 'NetworkLayout', 'InfrastructureConfig']

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


class SwaggerToSpecConverter(object):
    """ Convert Swagger structure to a Specification structure """

    @classmethod
    def convert(cls, resources):
        """ Prepare all resources

            Args:
                resources: A list of all resources to manage

            Returns:
                a list of all specifications

        """
        relations = dict()

        specifications = dict()

        for name, resource in resources.iteritems():

            if name in IGNORED_RESOURCES:
                Printer.warn('Ignored resource %s' % name)
                continue

            # No APIs, no relations, go to hell !
            if len(resource['apis']) == 0:
                Printer.warn('No APIs for resource %s' % name)
                continue

            specifications[name] = cls._reorganize_structure(name, resource)

            model = specifications[name]['model']
            parents_apis = specifications[name]['apis']['parents']

            SwaggerToSpecConverter._process_name(model=model)
            SwaggerToSpecConverter._process_apis(model=model, apis=parents_apis, relations=relations)
            SwaggerToSpecConverter._process_attributes(model=model)

        for name, specification in specifications.iteritems():
            model = specification['model']
            SwaggerToSpecConverter._process_children_apis(model=model, apis=specification['apis'], relations=relations)

        # Specific case of the REST User
        SwaggerToSpecConverter._process_rest_user(specifications, relations)

        Printer.success('Converted %s objects from swagger description files' % len(specifications))

        return specifications

    @classmethod
    def _reorganize_structure(self, resource_name, swagger_infos):
        """ Switch from swagger information to something more processable

        """
        model_name = swagger_infos['models'].keys()[0] # Still Metadata trick here...

        for api in swagger_infos['apis']:
            for operation in api['operations']:
                operation.pop('parameters', None)
                operation.pop('responseMessages', None)
                operation.pop('summary', None)
                operation.pop('nickname', None)
                operation.pop('type', None)

        resource = {
            'metadata': {},
            'apis': {
                'parents': {api['path']: api for api in swagger_infos['apis']},
                'children': None
            },
            'model': {
                "package": swagger_infos['package'],
                "entityName": resource_name,
                "RESTName": None,
                "resourceName": None,
                "description": swagger_infos['models'][model_name]['description'],
                "attributes": swagger_infos['models'][model_name]['properties']
            }
        }

        return resource

    @classmethod
    def _process_name(cls, model):
        """ Compute the name and plural name of from the swagger
            model

            Args:
                model: the model processed
                name: the name from swagger

        """
        name = model['entityName']

        if name in RESOURCE_MAPPING:
            model['entityName'] = RESOURCE_MAPPING[name]

    @classmethod
    def _process_apis(cls, model, apis, relations):
        """ Process apis for the given model

            Args:
                model: the model processed
                apis: the list of apis availble for the current swagger model
                relations: dict containing all relations between resources

        """
        for path, api in apis.iteritems():

            api.pop('path')

            if path.startswith('/'):
                path = path[1:]

            names = filter(bool, re.split('/\{id\}?/?', path))

            model['resourceName'] = names[-1]
            model['RESTName'] = Utils.get_singular_name(names[-1])
            api['entityName'] = model['entityName']

            if model['RESTName'] not in relations:
                relations[model['RESTName']] = {}

            # Parent relation
            parent_resource_name = names[0]
            parent_rest_name = Utils.get_singular_name(names[0])

            should_create_relation = False

            if model['resourceName'] != parent_resource_name:
                should_create_relation = True

            elif api['operations'][0]['method'] in ['GET', 'POST']:
                should_create_relation = True
                parent_resource_name = 'me'
                parent_rest_name = RESTUSER

            if should_create_relation:
                if parent_rest_name not in relations:
                    relations[parent_rest_name] = {}

                # Why ?
                # model_api.parent_rest_name = parent_rest_name
                # model_api.parent_resource_name = parent_resource_name

                relations[parent_rest_name][path] = {
                    'entityName': model['entityName'],
                    'operations': api['operations']
                }


    @classmethod
    def _process_attributes(cls, model):
        """ Removes ignored attributes and update attribute type / name

            Args:
                model: the processed model
                properties: the list of properties to process

        """
        attributes = model['attributes']

        for name in IGNORED_ATTRIBUTES:
            if name in attributes:
                attributes.pop(name)

        for name, attribute in attributes.iteritems():

            if 'required' in attribute and attribute['required'] == 'true':
                attribute['required'] = True
            else:
                attribute['required'] = False

            if 'uniqueItems' in attribute and attribute['uniqueItems'] == 'true':
                attribute['uniqueItems'] = True
            else:
                attribute['uniqueItems'] = False

            if '$ref' in attribute:
                attribute['type'] = attribute['$ref']
                attribute.pop('$ref')

            if attribute['type'] == 'enum' and 'enum' in attribute:
                attribute['allowedChoices'] = attribute['enum']
                attribute.pop('enum')

            if 'type' in attribute:
                clean_type = attribute['type'].lower().strip()
                if clean_type.startswith('array') or clean_type.startswith('collection'):
                    attribute['type'] = 'array'

            # Remove attributes
            if 'items' in attribute:
                attribute.pop('items')

            # Default values
            if 'filterable' not in attribute:
                attribute['filterable'] = False

            if 'readonly' not in attribute:
                attribute['readonly'] = False

            if 'orderable' not in attribute:
                attribute['orderable'] = False

            if 'creationOnly' not in attribute:
                attribute['creationOnly'] = False

            if 'autogenerated' not in attribute:
                attribute['autogenerated'] = False

            if 'format' not in attribute:
                attribute['format'] = None

            if 'minLength' not in attribute:
                attribute['minLength'] = None

            if 'maxLength' not in attribute:
                attribute['maxLength'] = None

            if 'minValue' not in attribute:
                attribute['minValue'] = None

            if 'maxValue' not in attribute:
                attribute['maxValue'] = None

            if 'allowedChars' not in attribute:
                attribute['allowedChars'] = None

            if 'defaultOrder' not in attribute:
                attribute['defaultOrder'] = False

            if 'allowedChoices' not in attribute:
                attribute['allowedChoices'] = None

    @classmethod
    def _process_children_apis(cls, model, apis, relations):
        """ Attach relations to the current model

            Args:
                model: the processed model
                relations: all existing relations

        """
        if model['RESTName'] in relations:
            apis['children'] = relations[model['RESTName']]

    @classmethod
    def _process_rest_user(cls, models, relations):
        """ Process the specific case of the NURESTUser object

            Add a RESTUser object in models, based on User
        """
        if USER not in models:
            return

        models[RESTUSER] = deepcopy(models[USER])
        models[RESTUSER]['model']['entityName'] = RESTUSER
        models[RESTUSER]['model']['RESTName'] = 'me'
        models[RESTUSER]['apis']['children'] = relations[RESTUSER]

        # Still needed ??
        # ignored_attributes = ['restrictionDate']
        #
        # for attribute_name, attribute_infos in models[RESTUSER]['model']['attributes'].iteritems():
        #     if attribute_name in ignored_attributes:
        #         rest_user_model.attributes.remove(attribute)

        # Additional attributes
        role_attribute = {
                u"description": "Role of the user.",
                u"type": "string",
                u"required": False,
                u"uniqueItems": False,
                u"filterable": False,
                u"readonly": False,
                u"orderable": False,
                u"creationOnly": False,
                u"autogenerated": False,
                u"format": None,
                u"minLength": None,
                u"maxLength": None,
                u"minValue": None,
                u"maxValue": None,
                u"allowedChars": None,
                u"allowedChoices": None,
                u"defaultOrder": False,
            }

        models[RESTUSER]['model']['attributes']['role'] = role_attribute

        entreprise_name_attribute = {
                u"description": "Name of the enterprise.",
                u"type": "string",
                u"required": False,
                u"uniqueItems": False,
                u"filterable": False,
                u"readonly": False,
                u"orderable": False,
                u"creationOnly": False,
                u"autogenerated": False,
                u"format": None,
                u"minLength": None,
                u"maxLength": None,
                u"minValue": None,
                u"maxValue": None,
                u"allowedChars": None,
                u"allowedChoices": None,
                u"defaultOrder": False,
            }

        models[RESTUSER]['model']['attributes']['enterpriseName'] = entreprise_name_attribute

        entreprise_id_attribute = {
                u"description": "Identifier of the enterprise.",
                u"type": "string",
                u"required": False,
                u"uniqueItems": False,
                u"filterable": False,
                u"readonly": False,
                u"orderable": False,
                u"creationOnly": False,
                u"autogenerated": False,
                u"format": None,
                u"minLength": None,
                u"maxLength": None,
                u"minValue": None,
                u"maxValue": None,
                u"allowedChars": None,
                u"allowedChoices": None,
                u"defaultOrder": False,
            }

        models[RESTUSER]['model']['attributes']['enterpriseID'] = entreprise_id_attribute
