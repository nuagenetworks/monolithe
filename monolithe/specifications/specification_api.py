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

from monolithe.lib import SDKUtils


class SpecificationAPI(object):
    """ Describe an object API

    """
    def __init__(self, specification, data=None):
        """ Defines an API

            Example:
                path: /enterprises/id/gateway
                resource_name : enterprisenetworks
                remote_name : enterprisenetwork
                plural_name : EnterpriseNetworks
                instance_plural_name : enterprise_networks

        """
        self.path = None
        self.resource_name = None
        self.remote_name = None
        self.plural_name = None
        self.deprecated = False
        self.relationship = "child"
        self.instance_plural_name = None
        self.specification = specification
        self._entity_name = None
        self.operations = []

        if data:
            self.from_dict(data)

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
            self.plural_name = SDKUtils.get_plural_name(value)
            self.instance_plural_name = SDKUtils.get_python_name(self.plural_name)

            if self.remote_name == "allalarm":
                self.instance_plural_name = "all_alarms"  # Differs from alarms

    def from_dict(self, data):
        """

        """
        if "path" in data:
            self.path = data["path"]

        if "resource_name" in data:
            self.resource_name = data["resource_name"]

        if "rest_name" in data:
            self.remote_name = data["rest_name"]

        if "deprecated" in data:
            self.deprecated = data["deprecated"]  if "deprecated" in data else False

        if "relationship" in data:
            self.relationship = data["relationship"] if "relationship" in data else "child"

        if "entity_name" in data:
            # Only for children to Used to create fetchers
            self.entity_name = data["entity_name"]

        for operation in data["operations"]:
            model_operation = SpecificationAPIOperation(data=operation)
            self.operations.append(model_operation)

    def to_dict(self):
        """
        """

        data = {}

        if self.resource_name:
            data["resource_name"] = self.resource_name

        if self.remote_name:
            data["rest_name"] = self.remote_name

        if self.relationship:
            data["relationship"] = self.relationship

        if self.deprecated:
            data["deprecated"] = self.deprecated

        data["operations"] = []

        for operation in self.operations:
            data["operations"].append(operation.to_dict())

        if not len(data["operations"]):
            del data["operations"]

        return data


class SpecificationAPIOperation(object):
    """ Describe an API operation

    """
    def __init__(self, data=None):
        """ Defines an API

            Example:
                method: GET

        """
        self.method = None
        self.availability = None
        self.deprecated = False

        if data:
            self.from_dict(data)

    def from_dict(self, data):
        """

        """
        self.method = data["method"]
        self.availability = data["availability"]
        self.deprecated = data["deprecated"] if "deprecated" in data else False

    def to_dict(self):
        """
        """

        data = {}

        data["method"] = self.method
        data["availability"] = self.availability
        data["deprecated"] = self.deprecated

        return data
