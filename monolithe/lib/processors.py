# -*- coding: utf-8 -*-

import re

from .utils import Utils
from .printer import Printer
from .objects import Model, ModelAttribute, ModelAPI, ModelOperation

USER = 'User'

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
        models = dict()

        for resource_name, resource in resources.iteritems():

            model = Model()
            model.description = resource['model']['description']
            ModelsProcessor._process_package(model=model, package=resource['model']['package'])
            ModelsProcessor._process_name(model=model, name=resource['model']['entityName'], resource_name=resource['model']['resourceName'])
            ModelsProcessor._process_apis(model=model, apis=resource['apis'])
            ModelsProcessor._process_attributes(model=model, attributes=resource['model']['attributes'])

            models[model.name] = model

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
    def _process_name(cls, model, name, resource_name):
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
        model.instance_name = Utils.get_python_name(model.name)
        model.plural_name = Utils.get_plural_name(model.name)
        model.instance_plural_name = Utils.get_python_name(model.plural_name)
        model.remote_name = Utils.get_singular_name(resource_name)
        model.resource_name = resource_name

    @classmethod
    def _process_apis(cls, model, apis):
        """ Process apis for the given model

            Args:
                model: the model processed
                apis: the list of apis availble for the current swagger model
                relations: dict containing all relations between resources

        """
        for path, api in apis['children'].iteritems():

            if api['entityName'] == model.name:
                continue

            names = filter(bool, re.split('/\{id\}?/?', path))

            child_resource_name = names[-1]
            child_rest_name = Utils.get_singular_name(names[-1])

            model_api = ModelAPI()
            model_api.path = path
            model_api.resource_name = child_resource_name
            model_api.remote_name = child_rest_name
            model_api.plural_name = Utils.get_plural_name(api['entityName'])
            model_api.instance_plural_name = Utils.get_python_name(model_api.plural_name)

            for operation in api['operations']:
                model_operation = ModelOperation()
                model_operation.method = operation['method']
                model_api.operations.append(model_operation)

            model.apis['children'][path] = model_api

        for path, api in apis['parents'].iteritems():

            if api['entityName'] == model.name:
                continue

            # Check when it is necessary to use this !
            names = filter(bool, re.split('/\{id\}?/?', path))

            parent_resource_name = names[0]
            parent_rest_name = Utils.get_singular_name(names[0])

            model_api = ModelAPI()
            model_api.resource_name = parent_resource_name
            model_api.remote_name = parent_rest_name
            model_api.plural_name = Utils.get_plural_name(api['entityName'])
            model_api.instance_plural_name = Utils.get_python_name(model_api.plural_name)

            for operation in api['operations']:
                model_operation = ModelOperation()
                model_operation.method = operation['method']
                model_api.operations.append(model_operation)


            model.apis['parents'][path] = model_api

        if model.name == 'Domain':
            print model.apis['children']

    @classmethod
    def _process_attribute_local_name(cls, name):
        """ Change local name according to the remote name

            Args:
                name: the remote name

            Returns:
                A beautiful python name

        """
        if name in ATTRIBUTE_MAPPING:
            return Utils.get_python_name(ATTRIBUTE_MAPPING[name])

        return Utils.get_python_name(name)

    @classmethod
    def _process_attributes(cls, model, attributes):
        """ Removes ignored attributes and update attribute type / name

            Args:
                model: the processed model
                properties: the list of properties to process

        """

        for name, attr in attributes.iteritems():

            attribute = ModelAttribute()
            attribute.remote_name = name
            attribute.local_name = cls._process_attribute_local_name(name)

            attribute.description = attr['description']
            attribute.type = attr['type']
            attribute.required = attr['required']
            attribute.uniqueItems = attr['uniqueItems']
            attribute.filterable = attr['filterable']
            attribute.readonly = attr['readonly']
            attribute.orderable = attr['orderable']
            attribute.creationOnly = attr['creationOnly']
            attribute.autogenerated = attr['autogenerated']
            attribute.format = attr['format']
            attribute.minLength = attr['minLength']
            attribute.maxLength = attr['maxLength']
            attribute.minValue = attr['minValue']
            attribute.maxValue = attr['maxValue']
            attribute.allowedChars = attr['allowedChars']
            attribute.allowedChoices = attr['allowedChoices']
            attribute.defaultOrder = attr['defaultOrder']

            attribute.local_type = Utils.get_python_type_name(type_name=attribute.type, attribute_name=name, object_name=model.name)

            if attribute.local_type == 'time':
                model.has_time_attribute = True

            if attribute.local_type:
                model.attributes.append(attribute)
            else:
                # Simply ignore attributes otherwise...
                # CS 02/06/2015
                # Ignoring attribute enterprise of object InfrastructurePortProfile
                # Ignoring attribute gateway of object InfrastructureGatewayProfile
                # Ignoring attribute enterprise of object InfrastructureGatewayProfile
                Printer.log("Deliberately ignoring attribute %s of object %s" % (attribute.remote_name, model.name))
