# -*- coding: utf-8 -*-

import pkgutil
import json

from copy import deepcopy

from monolithe.lib import SDKUtils
from .specification_api import SpecificationAPI
from .specification_attribute import SpecificationAttribute


class Specification(object):
    """ Defines a specification object

    """

    def __init__(self, monolithe_config,  data=None):
        """ Initializes a model object

            Example:
                name: EnterpriseNetwork
                instance_name: enterprise_network
                plural_name: EnterpriseNetworks
                instance_plural_name: enterprise_networks
                remote_name: enterprisenetwork
                resource_name: enterprisenetworks
                package: network
        """
        self.__default_specification__ = None

        self.monolithe_config = monolithe_config
        self.filename = None
        self.description = None
        self.package = None
        self.name = None  # The original name of the object
        self.instance_name = None  # Name of the object as an instance
        self.plural_name = None  # the original name in plural
        self.instance_plural_name = None  # Name of the object as an instance of array or fetcher
        self.remote_name = None  # The remote name of the object
        self.resource_name = None  # The name of the resource used in URI
        self.attributes = []  # A list of all properties of the object
        self.children_apis = []
        self.parent_apis = []
        self.self_apis = []

        self.has_time_attribute = False  # A boolean to flag if the model has a time attribute

        if data:
            self.from_dict(data=data)

    def to_dict(self):
        """ Transform the current specification to a dictionary

        """

        if self.__default_specification__ is None:
            default_data = pkgutil.get_data(__package__, "/data/default_specification.json")
            self.__default_specification__ = json.loads(default_data)

        data = deepcopy(self.__default_specification__)

        data["model"]["description"] = self.description
        data["model"]["entityName"] = self.name
        data["model"]["package"] = self.package
        data["model"]["resourceName"] = self.resource_name
        data["model"]["RESTName"] = self.remote_name

        for attribute in self.attributes:
            data["model"]["attributes"][attribute.name] = attribute.to_dict()

        for api in self.children_apis:
            data["apis"]["children"] = api.to_dict()

        for api in self.parent_apis:
            data["apis"]["parent"] = api.to_dict()

        for api in self.self_apis:
            data["apis"]["self"] = api.to_dict()

        return data

    def from_dict(self, data):
        """ Fill the current object with information from the specification

        """

        ## replace all the tokens
        string_data = json.dumps(data)
        string_data.replace("[__RESSOURCE_NAME__]", data["model"]["resourceName"])
        string_data.replace("[__REST_NAME__]", data["model"]["RESTName"])
        string_data.replace("[__ENTITY_NAME__]", data["model"]["entityName"])
        data = json.loads(string_data)

        self.description = data["model"]["description"]
        self.package = data["model"]["package"]

        entity_name = data["model"]["entityName"]

        self.name = entity_name
        self.instance_name = SDKUtils.get_python_name(entity_name)
        self.plural_name = SDKUtils.get_plural_name(entity_name)
        self.instance_plural_name = SDKUtils.get_python_name(self.plural_name)
        self.remote_name = data["model"]["RESTName"]
        self.filename = "%s.spec" % self.remote_name
        self.resource_name = data["model"]["resourceName"]

        self.children_apis = self._get_apis("children", data["apis"])
        self.parent_apis = self._get_apis("parents", data["apis"])
        self.self_apis = self._get_apis("self", data["apis"])

        self.attributes = self._get_attributes(data["model"]["attributes"])

    def _get_apis(self, api_name, apis):
        """ Process apis for the given model

            Args:
                model: the model processed
                apis: the list of apis availble for the current model
                relations: dict containing all relations between resources

        """
        result_apis = []
        for path, data in apis[api_name].iteritems():

            api = SpecificationAPI(specification=self)
            data["path"] = path
            api.from_dict(data)
            result_apis.append(api)

        return result_apis

    def _get_attributes(self, attributes):
        """

        """
        model_attributes = []

        for name, data in attributes.iteritems():
            data["name"] = name
            model_attribute = SpecificationAttribute(specification=self, data=data)

            if model_attribute.has_time_attribute:
                self.has_time_attribute = True

            if not model_attribute.ignored:
                model_attributes.append(model_attribute)

        return sorted(model_attributes, key=lambda x: getattr(x, "local_name"))
