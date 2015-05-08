# -*- coding: utf-8 -*-


class Model(object):
    """ Defines a model object

    """
    def __init__(self):
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
        self.description = None
        self.name = None  # The original name of the object
        self.instance_name = None # Name of the object as an instance
        self.plural_name = None  # the original name in plural
        self.instance_plural_name = None # Name of the object as an instance of array or fetcher
        self.remote_name = None  # The remote name of the object
        self.resource_name = None  # The name of the resource used in URI
        self.package = None  # The name of the package where the model is defined
        self.attributes = []  # A list of all properties of the object
        self.apis = {'children': {}, 'parents': {}}  # A list of all apis available for this model

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
                path: /enterprises/id/gateway
                resource_name : enterprisenetworks
                remote_name : enterprisenetwork
                name : EnterpriseNetwork
                plural_name : EnterpriseNetworks
                instance_plural_name : enterprise_networks

        """
        self.name = None
        self.path = None
        self.resource_name = None
        self.remote_name = None
        self.plural_name = None
        self.instance_plural_name = None

        self.operations = []


class ModelOperation(object):
    """ Describe a model operation

    """
    def __init__(self):
        """ Defines an API

            Example:
                method: GET

        """
        self.method = None


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
