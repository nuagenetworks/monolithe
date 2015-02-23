# -*- coding: utf-8 -*-

from .utils import Utils


class Model(object):
    """ Defines a model object

    """
    def __init__(self):
        """ Initializes a model object

            Example:
                name: Enterprise
                plural_name: Enterprises
                remote_name: enterprise
                resource_name: enterprises
                package: usermgt
        """
        self.description = None
        self.name = None  # The original name of the object
        self.plural_name = None  # the original name in plural
        self.remote_name = None  # The remote name of the object
        self.resource_name = None  # The name of the resource used in URI
        self.package = None  # The name of the package where the model is defined
        self.attributes = []  # A list of all properties of the object
        self.relations = []  # A list of children models
        self.apis = []  # A list of all apis available for this model

        self.has_time_attribute = False  # A boolean to flag if the model has a time attribute


class ModelAttribute(object):
    """ Define an attribute of a model

    """
    def __init__(self):
        """ Define an attribute

            Example:
                remote_name: associatedGatewayID
                local_name: associated_gateway_id
                remote_type: String
                local_type: str
        """
        self.description = None
        self.remote_name = None
        self.local_name = None
        self.remote_type = None
        self.local_type = None

        self.is_required = False
        self.is_unique = False


class ModelAPI(object):
    """ Describe a model API

    """
    def __init__(self):
        """ Defines an API

            Example:
                path: GET
                method: /enterprises/id/gateway
                parent_remote_name: enterprise
                parent_resource_name: enterprises
        """
        self.path = None
        self.method = None
        self.parent_remote_name = None
        self.parent_resource_name = None
        self.description = None
        self.parameters = []
        self.response_messages = []

class ModelOperation(object):
    """ Describe a model operation

    """
    def __init__(self):
        """ Defines an API

            Example:
                method: GET|POST|PUT|DELETE
                summary: a description
                parameters: List of parameters
                responseMessages:

        """
        self.method = None
        self.summary = None
        self.parameters = []
        self.responseMessages = []

class ModelOperationParameter(object):
    """ Describe a model operation

    """
    def __init__(self):
        """ Defines an API

            Example:
                name: id
                required: true
                type: string
                paramType: path|body|form

        """
        self.name = None
        self.required = None
        self.type = None
        self.paramType = None

class ModelRelation(object):
    """ Defines a model relation object

    """
    def __init__(self):
        """ Initializes a model object

            Example:
                name: Enterprise
                plural_name: Enterprises
                remote_name: enterprise
                resource_name: enterprises
                api: the model API that makes the relation
        """
        self.name = None  # The original name of the object
        self.plural_name = None  # the original name in plural
        self.remote_name = None  # The remote name of the object
        self.resource_name = None  # The name of the resource used in URI
        self.api = None  # the model api