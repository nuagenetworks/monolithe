# -*- coding: utf-8 -*-

import re

from .utils import Utils
from monolithe.utils.printer import Printer
from .objects import Model, ModelAttribute, ModelAPI, ModelOperation

from monolithe.utils.parse import ParsingUtils
from monolithe.utils.constants import Constants


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
            ModelsProcessor._process_name(model=model, name=resource['model']['entityName'], resource_name=resource['model']['resourceName'], remote_name=resource['model']['RESTName'])
            ModelsProcessor._process_apis(model=model, apis=resource['apis'], resources=resources)
            ModelsProcessor._process_attributes(model=model, attributes=resource['model']['attributes'])

            models[model.remote_name] = model

        Printer.success('Processed succeed for %s objects' % len(models))

        return models

    @classmethod
    def _process_package(cls, model, package):
        """ Process package name

        """
        model.package = ParsingUtils.get_package_name(package)

    @classmethod
    def _process_name(cls, model, name, resource_name, remote_name):
        """ Compute the name and plural name of from the swagger
            model

            Args:
                model: the model processed
                name: the name from swagger

        """
        model.name = ParsingUtils.get_correct_name(name)

        model.instance_name = Utils.get_python_name(model.name)
        model.plural_name = Utils.get_plural_name(model.name)
        model.instance_plural_name = Utils.get_python_name(model.plural_name)
        model.remote_name = remote_name.lower()
        model.resource_name = resource_name

    @classmethod
    def _process_apis(cls, model, apis, resources):
        """ Process apis for the given model

            Args:
                model: the model processed
                apis: the list of apis availble for the current swagger model
                relations: dict containing all relations between resources

        """

        for path, api in apis['children'].iteritems():

            if api['resourceName'] == model.resource_name:
                continue

            names = filter(bool, re.split('/\{id\}?/?', path[1:] if path.startswith('/') else path))

            child_resource_name = names[-1]
            child_rest_name = Utils.get_singular_name(names[-1])

            model_api = ModelAPI()
            model_api.path = path
            model_api.resource_name = child_resource_name
            model_api.remote_name = child_rest_name

            if child_rest_name.startswith('all'):
                child_rest_name = child_rest_name[3:]

            if child_rest_name in resources:
                entity_name = resources[child_rest_name]['model']['entityName']
                model_api.plural_name = Utils.get_plural_name(entity_name)
                model_api.instance_plural_name = Utils.get_python_name(model_api.plural_name)

            for operation in api['operations']:
                model_operation = ModelOperation()
                model_operation.method = operation['method']
                model_api.operations.append(model_operation)

            model.apis['children'][path] = model_api

        for path, api in apis['parents'].iteritems():

            model_api = ModelAPI()
            model_api.path = path
            model_api.resource_name = api['resourceName']
            model_api.remote_name = api['RESTName']

            for operation in api['operations']:
                model_operation = ModelOperation()
                model_operation.method = operation['method']
                model_api.operations.append(model_operation)

            model.apis['parents'][path] = model_api

        for path, api in apis['self'].iteritems():

            model_api = ModelAPI()
            model_api.path = path

            for operation in api['operations']:
                model_operation = ModelOperation()
                model_operation.method = operation['method']
                model_api.operations.append(model_operation)

            model.apis['self'][path] = model_api

    @classmethod
    def _process_attribute_local_name(cls, name):
        """ Change local name according to the remote name

            Args:
                name: the remote name

            Returns:
                A beautiful python name

        """
        if name in Constants.ATTRIBUTE_MAPPING:
            return Utils.get_python_name(Constants.ATTRIBUTE_MAPPING[name])

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
            attribute.unique = attr['unique']
            attribute.filterable = attr['filterable']
            attribute.read_only = attr['readOnly']
            attribute.orderable = attr['orderable']
            attribute.creation_only = attr['creationOnly']
            attribute.autogenerated = attr['autogenerated']
            attribute.format = attr['format']
            attribute.min_length = attr['minLength']
            attribute.max_length = attr['maxLength']
            attribute.min_value = attr['minValue']
            attribute.max_value = attr['maxValue']
            attribute.allowed_chars = attr['allowedChars']
            attribute.allowed_choices = attr['allowedChoices']
            attribute.default_order = attr['defaultOrder']

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
