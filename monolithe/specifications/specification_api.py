# -*- coding: utf-8 -*-

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
        self.instance_plural_name = None
        self.specification = specification

        self.operations = []

        if data:
            self.from_dict(data)

    def from_dict(self, data):
        """

        """
        self.path = data["path"]
        self.resource_name = data["resourceName"]
        self.remote_name = data["RESTName"]

        if "entityName" in data:
            # Only for children
            # Used to create fetchers

            entity_name = data["entityName"]
            self.plural_name = SDKUtils.get_plural_name(entity_name)
            self.instance_plural_name = SDKUtils.get_python_name(self.plural_name)

            if self.remote_name == "allalarm":
                self.instance_plural_name = "all_alarms"  # Differs from alarms

        for operation in data["operations"]:
            model_operation = SpecificationAPIOperation(data=operation)
            self.operations.append(model_operation)

    def to_dict(self):
        """
        """

        data = {}

        data["path"] = self.path
        data["resourceName"] = self.resource_name
        data["RESTName"] = self.remote_name
        data["operations"] = []

        for operation in self.operations:
            data["operations"].append(operation.to_dict())

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

        if data:
            self.from_dict(data)

    def from_dict(self, data):
        """

        """
        self.method = data["method"]
        self.availability = data["availability"]

    def to_dict(self):
        """
        """

        data = {}

        data["method"] = self.method
        data["availability"] = self.availability

        return data
