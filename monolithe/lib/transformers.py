# -*- coding: utf-8 -*-

from copy import deepcopy

from monolithe.utils.printer import Printer
from monolithe.utils.constants import Constants
from monolithe.utils.parse import ParsingUtils
from monolithe.models.specification import Specification
from monolithe.models.objects import MonolitheObject


class SwaggerTransformer(object):
    """ Transform Swagger Structure to Specification Structure

    """

    @classmethod
    def get_specifications(cls, resources, filters=[]):
        """ Prepare all resources

            Args:
                resources: A list of all resources to manage

            Returns:
                a list of all specifications

        """
        relations = dict()
        specifications = dict()

        for entity_name, swagger_resource in resources.iteritems():

            specification = Specification(swagger_resource)

            rest_name = specification['model']['RESTName']

            if rest_name == None:
                continue

            if len(filters) > 0 and rest_name not in filters:
                continue

            specifications[rest_name] = specification

        relations = Specification.parent_relations

        for rest_name, specification in specifications.iteritems():
            # Attach children relation to its parent
            if rest_name in relations:
                specification['apis']['children'] = relations[rest_name]

        if Constants.USER_REST_NAME in specifications and Constants.RESTUSER_REST_NAME in relations:
            specifications[Constants.RESTUSER_REST_NAME] = cls._get_rest_user_specification(specifications[Constants.USER_REST_NAME], relations[Constants.RESTUSER_REST_NAME])

        Printer.success('Transformed %s objects from swagger description files' % len(specifications))

        return ParsingUtils.order(specifications)

    @classmethod
    def _get_rest_user_specification(cls, specification, relations):
        """ Process the specific case of the NURESTUser object

            Add a RESTUser object in specifications, based on User
        """
        rest_user_specification = deepcopy(specification)

        # Default information
        rest_user_specification['model']['entityName'] = Constants.RESTUSER
        rest_user_specification['model']['RESTName'] = Constants.RESTUSER_REST_NAME
        rest_user_specification['model']['resourceName'] = Constants.RESTUSER_REST_NAME

        # Apis
        rest_user_specification['apis']['children'] = relations
        rest_user_specification['apis']['parents'] = {}
        rest_user_specification['apis']['self'] = {}

        # Additional attributes
        role_attribute = Specification.get_default_attribute()
        role_attribute['description'] = "Role of the user."
        role_attribute['type'] = "string"
        rest_user_specification.add_attribute('role', role_attribute)

        entreprise_name_attribute = Specification.get_default_attribute()
        entreprise_name_attribute['description'] = "Name of the enterprise."
        entreprise_name_attribute['type'] = "string"
        rest_user_specification.add_attribute('enterpriseName', entreprise_name_attribute)

        entreprise_id_attribute = Specification.get_default_attribute()
        entreprise_id_attribute['description'] = "Identifier of the enterprise."
        entreprise_id_attribute['type'] = "string"
        rest_user_specification.add_attribute('enterpriseID', entreprise_id_attribute)

        return rest_user_specification


class SpecificationTransformer(object):
    """ Process all models information that will be send to the writer """

    @classmethod
    def get_objects(cls, specifications):
        """ Transform specifications to objects

            Args:
                specifications: A list of all specification to transform

            Returns:
                A list of python objects

        """
        models = dict()

        specifications = deepcopy(specifications)

        for rest_name, specification in specifications.iteritems():

            # Pre-calculate children entityName
            for path, api in specification['apis']['children'].iteritems():
                rest_name = ParsingUtils.get_rest_name(api['RESTName'])
                api['entityName'] = specifications[rest_name]['model']['entityName']

            model = MonolitheObject()
            model.from_specification(specification)

            models[model.remote_name] = model

        Printer.success('Processed succeed for %s objects' % len(models))

        return ParsingUtils.order(models)
