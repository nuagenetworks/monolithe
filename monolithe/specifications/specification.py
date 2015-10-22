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

    def __init__(self, filename, monolithe_config=None, data=None):
        """ Initializes a model object

            Example:
                name: EnterpriseNetwork
                instance_name: enterprise_network
                entity_name_plural: EnterpriseNetworks
                instance_name_plural: enterprise_networks
                rest_name: enterprisenetwork
                resource_name: enterprisenetworks
                package: network
        """
        self.monolithe_config = monolithe_config
        self.filename = filename

        self.allows_create = False
        self.allows_delete = False
        self.allows_get = False
        self.allows_update = False
        self.description = None
        self.entity_name_plural = None  # the original name in plural
        self.extends = []
        self.instance_name = None  # Name of the object as an instance
        self.instance_name_plural = None  # Name of the object as an instance of array or fetcher
        self.is_root = False
        self.package = None
        self.resource_name = None  # The name of the resource used in URI
        self.rest_name = None  # The remote name of the object
        self._entity_name = None  # The original name of the object

        self.attributes = []  # A list of all properties of the object
        self.child_apis = []
        self.parent_apis = []

        if data:
            self.from_dict(data=data)

    @property
    def entity_name(self):
        """
        """
        return self._entity_name

    @entity_name.setter
    def entity_name(self, value):
        """
        """
        self._entity_name = value

        if value:
            self.instance_name = SDKUtils.get_python_name(value)
            self.entity_name_plural = SDKUtils.get_entity_name_plural(value)
            self.instance_name_plural = SDKUtils.get_python_name(self.entity_name_plural)


    def to_dict(self):
        """ Transform the current specification to a dictionary

        """

        data = {"model": {}}

        if self.description:
            data["model"]["description"] = self.description

        if self.entity_name:
            data["model"]["entity_name"] = self.entity_name

        if self.package:
            data["model"]["package"] = self.package

        if self.resource_name:
            data["model"]["resource_name"] = self.resource_name

        if self.rest_name:
            data["model"]["rest_name"] = self.rest_name

        if self.extends:
            data["model"]["extends"] = self.extends

        if self.allows_get:
            data["model"]["get"] = self.allows_get

        if self.allows_update:
            data["model"]["update"] = self.allows_update

        if self.allows_create:
            data["model"]["create"] = self.allows_create

        if self.allows_delete:
            data["model"]["delete"] = self.allows_delete

        if self.is_root:
            data["model"]["root"] = self.is_root

        if not len(data["model"]):
            del data["model"]

        if len(self.attributes):
            data["attributes"] = {}

            for attribute in self.attributes:
                data["attributes"][attribute.rest_name] = attribute.to_dict()

        if len(self.child_apis):
            data["children"] = {}

            for api in self.child_apis:
                data["children"][api.remote_specification_name] = api.to_dict()

        return data

    def from_dict(self, data):
        """ Fill the current object with information from the specification

        """

        ## replace all the tokens
        string_data = json.dumps(data)
        tokens_replaced = False

        if "children" in data:
            self.child_apis = self._get_apis(data["children"])

        if "model" in data and "resource_name" in data["model"]:
            string_data = string_data.replace("[[resource_name]]", data["model"]["resource_name"])
            tokens_replaced = True

        if "model" in data and "rest_name" in data["model"]:
            string_data = string_data.replace("[[rest_name]]", data["model"]["rest_name"])
            tokens_replaced = True

        if "model" in data and "entity_name" in data["model"]:
            string_data = string_data.replace("[[entity_name]]", data["model"]["entity_name"])
            tokens_replaced = True

        if tokens_replaced:
            data = json.loads(string_data)

        if "model" in data:
            model = data["model"]
            self.description   = model["description"] if "description" in model else None
            self.package       = model["package"] if "package" in model else None
            self.extends       = model["extends"] if "extends" in model else []
            self.entity_name   = model["entity_name"] if "entity_name" in model else None
            self.rest_name     = model["rest_name"] if "rest_name" in model else None
            self.resource_name = model["resource_name"] if "resource_name" in model else None
            self.allows_get    = model["get"] if "get" in model else False
            self.allows_create = model["create"] if "create" in model else False
            self.allows_update = model["update"] if "update" in model else False
            self.allows_delete = model["delete"] if "delete" in model else False
            self.is_root       = model["root"] if "root" in model else False

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

        for name, data in apis.iteritems():
            api = SpecificationAPI(remote_specification_name=name, specification=self)
            api.from_dict(data)
            ret.append(api)

        return sorted(ret, key=lambda x: getattr(x, "specification"))

    def _get_attributes(self, attributes):
        """

        """
        ret = []

        for name, data in attributes.iteritems():
            model_attribute = SpecificationAttribute(rest_name=name, specification=self, data=data)
            ret.append(model_attribute)

        return sorted(ret, key=lambda x: getattr(x, "rest_name"))
