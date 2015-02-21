# -*- coding: utf-8 -*-

import re

from .utils import Utils
from .printer import Printer
from .objects import Model, ModelAttribute, ModelAPI, ModelRelation

USER = 'User'
RESTUSER = 'RESTUser'

IGNORED_ATTRIBUTES = ["_fetchers"]
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
    '/vport': 'Core Networking'
}


class ModelsProcessor(object):
    """ Process all models information that will be send to the writer """

    @classmethod
    def process(cls, resources):
        """ Prepare all resources

            Args:
                resources: A list of all resources to manage

            Returns:
                a processed list of resources

        """
        relations = dict()
        models = dict()

        for resource_name, resource in resources.iteritems():

            for name, swagger_model in resource['models'].iteritems():

                if name in IGNORED_RESOURCES:
                    continue

                # No APIs, no relations, go to hell !
                if len(resource['apis']) == 0:
                    continue

                model = Model()
                model.description = swagger_model['description']
                ModelsProcessor._process_package(model=model, package=resource['package'])
                ModelsProcessor._process_name(model=model, name=swagger_model['id'])
                ModelsProcessor._process_apis(model=model, apis=resource['apis'], relations=relations)
                ModelsProcessor._process_attributes(model=model, properties=swagger_model['properties'])

                models[model.name] = model

        for name, model in models.iteritems():
            ModelsProcessor._process_relations(model, relations)

        # Specific case of the REST User
        ModelsProcessor._process_rest_user(models, relations)

        Printer.success('Processed succeed for %s objects' % len(models))

        return models

    @classmethod
    def _process_package(cls, model, package):
        """ Process package name

        """
        if package in PACKAGE_MAPPING:
            model.package = PACKAGE_MAPPING[package]
        else:
            model.package = package

    @classmethod
    def _process_name(cls, model, name):
        """ Compute the name and plural name of from the swagger
            model

            Args:
                model: the model processed
                name: the name from swagger

        """
        if name in RESOURCE_MAPPING:
            model.name = RESOURCE_MAPPING[name]
        else:
            model.name = name

        model.instance_name = Utils.get_python_name(model.name)
        model.plural_name = Utils.get_plural_name(model.name)
        model.instance_plural_name = Utils.get_python_name(model.plural_name)

    @classmethod
    def _process_apis(cls, model, apis, relations):
        """ Process apis for the given model

            Args:
                model: the model processed
                apis: the list of apis availble for the current swagger model
                relations: dict containing all relations between resources

        """
        for api in apis:

            path = api['path']

            if path.startswith('/'):
                path = path[1:]

            model_api = ModelAPI()
            model_api.path = '/%s' % path
            model_api.operations = api['operations']  # TOIMPROVE

            names = filter(bool, re.split('/\{id\}?/?', path))

            model.resource_name = names[-1]
            model.remote_name = Utils.get_singular_name(names[-1])

            if model.remote_name not in relations:
                relations[model.remote_name] = []

            parent_resource_name = names[0]
            parent_remote_name = Utils.get_singular_name(names[0])

            should_create_relation = False

            if model.resource_name != parent_resource_name:
                should_create_relation = True

            elif model_api.operations[0]['method'] in ['GET', 'POST']:
                should_create_relation = True
                parent_resource_name = 'me'
                parent_remote_name = RESTUSER

            if should_create_relation:
                if parent_remote_name not in relations:
                    relations[parent_remote_name] = []

                model_api.parent_remote_name = parent_remote_name
                model_api.parent_resource_name = parent_resource_name

                relation = ModelRelation()
                relation.name = model.name
                relation.plural_name = model.plural_name
                relation.remote_name = model.remote_name
                relation.resource_name = model.resource_name
                relation.instance_plural_name = model.instance_plural_name
                relation.api = model_api

                relations[parent_remote_name].append(relation)

            model.apis.append(model_api)

    @classmethod
    def _process_attributes(cls, model, properties):
        """ Removes ignored attributes and update attribute type / name

            Args:
                model: the processed model
                properties: the list of properties to process

        """

        for name, prop in properties.iteritems():

            if name in IGNORED_ATTRIBUTES:
                continue

            attribute = ModelAttribute()
            attribute.remote_name = name
            attribute.local_name = Utils.get_python_name(name)
            attribute.description = prop['description']

            if 'required' in prop and prop['required'] == 'true':
                attribute.is_required = True

            if 'uniqueItems' in prop and prop['uniqueItems'] == 'true':
                attribute.is_unique = True

            if 'type' in prop:
                attribute.remote_type = prop['type']
                attribute.local_type = Utils.get_python_type_name(type_name=prop['type'], attribute_name=name, object_name=model.name)

                # Should this model import the time or not according to its attributes
                if attribute.local_type == 'time':
                    model.has_time_attribute = True

                if attribute.remote_type == 'enum':
                    attribute.choices = prop['enum']

            else:
                attribute.local_type = Utils.get_python_type_name(type_name=prop['$ref'], attribute_name=name, object_name=model.name)

            if attribute.local_type:
                model.attributes.append(attribute)
            else:
                # Simply ignore attributes otherwise...
                # 02/06/2015
                # Ignoring attribute enterprise of object InfrastructurePortProfile
                # Ignoring attribute gateway of object InfrastructureGatewayProfile
                # Ignoring attribute enterprise of object InfrastructureGatewayProfile
                Printer.log("Deliberately ignoring attribute %s of object %s" % (attribute.remote_name, model.name))

    @classmethod
    def _process_relations(cls, model, relations):
        """ Attach relations to the current model

            Args:
                model: the processed model
                relations: all existing relations

        """
        if model.remote_name in relations:
            model.relations = relations[model.remote_name]
        else:
            model.relations = []

    @classmethod
    def _process_rest_user(cls, models, relations):
        """ Process the specific case of the NURESTUser object

            Add a RESTUser object in models, based on User
        """
        from copy import deepcopy
        rest_user_model = Model()
        rest_user_model.name = RESTUSER
        rest_user_model.remote_name = 'me'
        rest_user_model.relations = relations[RESTUSER]
        rest_user_model.attributes = deepcopy(models[USER].attributes)

        role = ModelAttribute()
        role.description = u'Role of the user'
        role.remote_name = u'role'
        role.local_name = u'role'
        role.remote_type = u'String'
        role.local_type = u'str'
        rest_user_model.attributes.append(role)

        enterprise_id = ModelAttribute()
        enterprise_id.description = u'Identifier of the enterprise'
        enterprise_id.remote_name = u'enterpriseID'
        enterprise_id.local_name = u'enterprise_id'
        enterprise_id.remote_type = u'String'
        enterprise_id.local_type = u'str'
        rest_user_model.attributes.append(enterprise_id)

        enterprise_name = ModelAttribute()
        enterprise_name.description = u'Name of the enterprise'
        enterprise_name.remote_name = u'enterpriseName'
        enterprise_name.local_name = u'enterprise_name'
        enterprise_name.remote_type = u'String'
        enterprise_name.local_type = u'str'
        rest_user_model.attributes.append(enterprise_name)

        models[RESTUSER] = rest_user_model
