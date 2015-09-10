# -*- coding: utf-8 -*-

import os
import pkgutil

from datetime import date
from copy import deepcopy

from monolithe.lib.utils.parse import ParsingUtils
from monolithe.lib.utils.vsdk import VSDKUtils
from monolithe.lib.utils.urls import URLUtils
from monolithe.lib.utils.constants import Constants
from monolithe.lib.utils.printer import Printer


class Specification(dict):

    __default_specification__ = None
    __default_attribute__ = None

    parent_relations = {}  # Used to compute parent - child relation

    def __init__(self, swagger):
        """ Initializes a specification

        """
        super(Specification, self).__init__()

        self.update(self.get_default_specification())
        self._from_swagger(swagger)

    @classmethod
    def get_default_specification(cls):
        """ Get a default specification structure

        """
        if cls.__default_specification__ is None:
            data = pkgutil.get_data(__package__, '/data/default_specification.json')
            cls.__default_specification__ = ParsingUtils.parseJSON(data)

        return deepcopy(cls.__default_specification__)

    @classmethod
    def get_default_attribute(cls):
        """ Get a default attribute structure

        """
        if cls.__default_attribute__ is None:
            data = pkgutil.get_data(__package__, '/data/default_attribute.json')
            cls.__default_attribute__ = ParsingUtils.parseJSON(data)

        return deepcopy(cls.__default_attribute__)

    def _from_swagger(self, swagger):
        """ Complete specification with information from
            the swagger structure

        """
        entity_name = swagger['models'].keys()[0]

        # Default values
        self['model']['package'] = swagger['package']
        self['model']['entityName'] = ParsingUtils.get_correct_name(entity_name)
        self['model']['description'] = swagger['models'][entity_name]['description']

        # if len(swagger['apis']) == 0:
        #     Printer.warn('Swagger file %s has no apis defined' % entity_name)

        self._process_apis(apis=swagger['apis'])
        self._process_attributes(swagger_properties=swagger['models'][entity_name]['properties'])

    def _process_apis(self, apis):
        """ Process apis from swagger structure

            Args:
                apis: the apis from the swagger structure

        """

        for api in apis:
            path = api['path']

            specification_api = SpecificationApi(api)

            resource_names = URLUtils.resources_from_path(path)

            self['model']['resourceName'] = resource_names[-1]
            self['model']['RESTName'] = VSDKUtils.get_singular_name(resource_names[-1])

            # Parent relation
            parent_resource_name = resource_names[0]
            parent_rest_name = VSDKUtils.get_singular_name(resource_names[0])

            specification_api['resourceName'] = parent_resource_name
            specification_api['RESTName'] = parent_rest_name

            if len(resource_names) == 2:
                self['apis']['parents'][path] = specification_api
                self._create_parent_relation(path, specification_api, parent_rest_name)
                continue

            # Only API with operation of form /xxxx or /xxxx/{id}
            methods = [operation['method'] for operation in api['operations']]

            if URLUtils.is_root_url(path=path, methods=methods):
                # specification_api['resourceName'] = Constants.RESTUSER_REST_NAME
                # specification_api['RESTName'] = Constants.RESTUSER_REST_NAME
                self['apis']['parents'][path] = specification_api
                self._create_parent_relation(path, specification_api, Constants.RESTUSER_REST_NAME)

            else:
                self['apis']['self'][path] = specification_api

    def _create_parent_relation(self, path, specification_api, parent_rest_name):
        """ Create a relation that will be bind to the parent later

        """
        # Make a copy for the parent relation
        parent_specification_api = deepcopy(specification_api)
        parent_specification_api['RESTName'] = self['model']['RESTName']
        parent_specification_api['resourceName'] = self['model']['resourceName']

        if parent_rest_name not in self.parent_relations:
            self.parent_relations[parent_rest_name] = {}

        self.parent_relations[parent_rest_name][path] = parent_specification_api

    def _process_attributes(self, swagger_properties):
        """ Removes ignored attributes and update attribute type / name

            Args:
                model: the processed model
                properties: the list of properties to process

        """

        for attribute_name, attribute_info in swagger_properties.iteritems():

            if attribute_name in Constants.IGNORED_ATTRIBUTES:
                continue

            attribute = self.get_default_attribute()

            if 'description' in attribute_info:
                attribute['description'] = attribute_info['description']

            if 'required' in attribute_info and attribute_info['required'] == 'true':
                attribute['required'] = True

            if 'uniqueItems' in attribute_info and attribute_info['uniqueItems'] == 'true':
                attribute['unique'] = True

            if '$ref' in attribute_info:
                attribute_info['type'] = attribute_info['$ref']

            if 'type' in attribute_info:
                attribute['type'] = attribute_info['type']

            if 'enum' in attribute_info:
                attribute['allowedChoices'] = attribute_info['enum']

            self.add_attribute(attribute_name, attribute)

    def add_attribute(self, attribute_name, attribute):
        """ Add a new attribute to the specification

        """
        self['model']['attributes'][attribute_name] = attribute


class SpecificationApi(dict):

    __default_api__ = None

    def __init__(self, swagger_api):
        """ Initializes a specification

        """
        super(SpecificationApi, self).__init__()
        self.update(self.get_default_api())

        for operation in swagger_api['operations']:
            self['operations'].append({u'method': operation['method'], u'availability': None})

    @classmethod
    def get_default_api(cls):
        """ Get default api structure

        """
        if cls.__default_api__ is None:
            data = pkgutil.get_data(__package__, '/data/default_api.json')
            cls.__default_api__ = ParsingUtils.parseJSON(data)

        return deepcopy(cls.__default_api__)
