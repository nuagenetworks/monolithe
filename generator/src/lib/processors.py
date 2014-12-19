# -*- coding: utf-8 -*-

import re

from utils import Utils
from printer import Printer

IGNORED_ATTRIBUTES = ["_fetchers"]
IGNORED_RESOURCES = ['EventLog', 'PublicNetworkMacro', 'NetworkLayout', 'InfrastructureConfig']

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
    'IngressAdvancedForwardingTemplateEntry': 'IngressAdvFwdEntryTemplate'
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
    def process(self, resources):
        """ Prepare all resources

            Args:
                resources: A list of all resources to manage

            Returns:
                a processed list of resources

        """
        relations = dict()
        models = dict()

        for resource_name, resource in resources.iteritems():

            for name, model in resource['models'].iteritems():

                if name in IGNORED_RESOURCES:
                    continue

                # No APIs, no relations, go to hell !
                if len(resource['apis']) == 0:
                    continue

                # Printer.log('Processing %s' % name)
                model['package'] = PACKAGE_MAPPING[resource['package']]
                ModelsProcessor._process_name(model=model)
                ModelsProcessor._process_apis(model=model, apis=resource['apis'], relations=relations)
                ModelsProcessor._process_attributes(model=model)

                models[model['name']] = model

        for name, model in models.iteritems():
            ModelsProcessor._process_relations(model, relations)

        Printer.success('Processed succeed for %s objects' % len(models))

        return models

    @classmethod
    def _process_name(cls, model):
        """ Compute the name and plural name of the current model

            Args:
                model: the model to process

        """
        current_name = model['id']

        if current_name in RESOURCE_MAPPING:
            model['name'] = RESOURCE_MAPPING[current_name]
        else:
            model['name'] = current_name

        model['plural_name'] = Utils.get_plural_name(model['name'])

    @classmethod
    def _process_apis(cls, model, apis, relations):
        """ Removes ignored attributes and update attribute type / name

            Args:
                model: the model to process
                apis: the list of apis availble for the resource
                relations: dict containing all relations between resources

            Returns:
                A dictionary of attribute

        """
        model['apis'] = []
        for api in apis:

            path = api['path']

            if path.startswith('/'):
                path = path[1:]

            names = filter(bool, re.split('/\{id\}?/?', path))

            model['resource_name'] = names[-1]
            model['remote_name'] = Utils.get_singular_name(names[-1])

            if model['remote_name'] not in relations:
                relations[model['remote_name']] = []

            parent_resource_name = names[0]
            parent_remote_name = Utils.get_singular_name(names[0])

            if model['resource_name'] != parent_resource_name:
                if parent_remote_name not in relations:
                    relations[parent_remote_name] = []

                relation = {
                    'name': model['name'],
                    'plural_name': model['plural_name'],
                    'resource_name': model['resource_name'],
                    'remote_name': model['remote_name'],
                    'api': api
                }

                relations[parent_remote_name].append(relation)

                api['parent'] = dict()
                api['parent']['remote_name'] = parent_remote_name
                api['parent']['resource_name'] = parent_resource_name

            model['apis'].append(api)

    @classmethod
    def _process_attributes(cls, model):
        """ Removes ignored attributes and update attribute type / name

            Args:
                model: the model to process

            Returns:
                A dictionary of attribute

        """
        attributes = model['properties']
        processed_attributes = dict()

        for name, attribute in attributes.iteritems():

            if name in IGNORED_ATTRIBUTES:
                continue

            attribute['remote_name'] = name
            attribute['local_name'] = Utils.get_python_name(name)

            if 'type' in attribute:
                attribute['local_type'] = Utils.get_python_type_name(type_name=attribute['type'], attribute_name=name, object_name=model['name'])

                # Should this model import the time or not according to its attributes
                if attribute['local_type'] == 'time':
                    model['import_time'] = True

            else:
                attribute['local_type'] = Utils.get_python_type_name(type_name=attribute['$ref'], attribute_name=name, object_name=model['name'])

            processed_attributes[name] = attribute

        model['properties'] = processed_attributes

    @classmethod
    def _process_relations(cls, model, relations):
        """ Attach relations to the current model

            Args:
                model: the model to process
                relations: all existing relations

        """

        remote_name = model['remote_name']

        if remote_name in relations:
            model['relations'] = relations[remote_name]
        else:
            model['relations'] = []
