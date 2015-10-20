# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pkgutil
import json

from copy import deepcopy

from monolithe.lib import SDKUtils
from .specification_api import SpecificationAPI
from .specification_attribute import SpecificationAttribute


class Specification(object):
    """ Defines a specification object

    """

    def __init__(self, monolithe_config, filename, data=None):
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
        self.filename = filename
        self.description = None
        self.package = None
        self._name = None  # The original name of the object
        self.instance_name = None  # Name of the object as an instance
        self.plural_name = None  # the original name in plural
        self.instance_plural_name = None  # Name of the object as an instance of array or fetcher
        self.remote_name = None  # The remote name of the object
        self.resource_name = None  # The name of the resource used in URI
        self.attributes = []  # A list of all properties of the object
        self.child_apis = []
        self.extends = []
        self.allows_get = True
        self.allows_create = False
        self.allows_update = True
        self.allows_delete = False
        self.has_time_attribute = False  # A boolean to flag if the model has a time attribute

        if data:
            self.from_dict(data=data)

    @property
    def name(self):
        """
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        """
        self._name = value

        if value:
            self.instance_name = SDKUtils.get_python_name(value)
            self.plural_name = SDKUtils.get_plural_name(value)
            self.instance_plural_name = SDKUtils.get_python_name(self.plural_name)


    def to_dict(self):
        """ Transform the current specification to a dictionary

        """

        if self.__default_specification__ is None:
            default_data = pkgutil.get_data(__package__, "/data/default_specification.json")
            self.__default_specification__ = json.loads(default_data)

        data = deepcopy(self.__default_specification__)

        if self.description:
            data["description"] = self.description

        if self.name:
            data["entity_name"] = self.name

        if self.package:
            data["package"] = self.package

        if self.resource_name:
            data["resource_name"] = self.resource_name

        if self.remote_name:
            data["rest_name"] = self.remote_name

        if self.extends:
            data["extends"] = self.extends

        if self.get:
            data["get"] = self.get

        if self.update:
            data["update"] = self.update

        if self.create:
            data["create"] = self.create

        if self.delete:
            data["delete"] = self.delete

        for attribute in self.attributes:
            data["attributes"][attribute.remote_name] = attribute.to_dict()

        if not len(data["attributes"]):
            del data["attributes"]

        if len(self.child_apis):
            data["children"] = []
            for api in self.child_apis:
                data["children"] = api.to_dict()

        return data

    def from_dict(self, data):
        """ Fill the current object with information from the specification

        """

        ## replace all the tokens
        string_data = json.dumps(data)
        tokens_replaced = False

        if "children" in data:
            self.child_apis = self._get_apis(data["children"])

        if "resource_name" in data:
            string_data = string_data.replace("[[resource_name]]", data["resource_name"])
            tokens_replaced = True

        if "rest_name" in data:
            string_data = string_data.replace("[[rest_name]]", data["rest_name"])
            tokens_replaced = True

        if "entity_name" in data:
            string_data = string_data.replace("[[entity_name]]", data["entity_name"])
            tokens_replaced = True

        if tokens_replaced:
            data = json.loads(string_data)

        self.description   = data["description"] if "description" in data else None
        self.package       = data["package"] if "package" in data else None
        self.extends       = data["extends"] if "extends" in data else []
        self.name          = data["entity_name"] if "entity_name" in data else None
        self.remote_name   = data["rest_name"] if "rest_name" in data else None
        self.resource_name = data["resource_name"] if "resource_name" in data else None
        self.allows_get    = data["get"] if "get" in data else True
        self.allows_create = data["create"] if "create" in data else False
        self.allows_update = data["update"] if "update" in data else True
        self.allows_delete = data["delete"] if "delete" in data else True

        if "attributes" in data:
            self.attributes = self._get_attributes(data["attributes"])


    def _get_apis(self, apis):
        """ Process apis for the given model

            Args:
                model: the model processed
                apis: the list of apis availble for the current model
                relations: dict containing all relations between resources

        """
        ret = []

        for data in apis:
            api = SpecificationAPI(specification=self)
            api.from_dict(data)
            ret.append(api)

        return ret

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
