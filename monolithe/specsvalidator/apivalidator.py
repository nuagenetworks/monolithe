# -*- coding: utf-8 -*-

import os
from validationerrors import APISpecAttributeDefinitionError
from validationerrors import APISpecAttributeCapitalizationError
from validationerrors import APISpecMissingTokenError
from validationerrors import APISpecMissingAttributeDefinitionError
from validationerrors import APISpecMissingAPIError
from validationerrors import APISpecMissingAPIMethodError

IGNORED_ATTRIBUTES = ["parentType", "lastUpdatedBy", "externalID", "lastUpdatedDate", "parentID", "owner", "creationDate", "ID"]


class APIValidator:
    """ Valdidate a candidate spec file against a spec file

    """

    def __init__(self, specification, candidate):
        """ Initialize the validator

        """
        self.candidate          = candidate
        self.specification      = specification
        self.parent_api_errors  = []
        self.self_api_errors    = []
        self.attribute_errors   = []

    def run(self):
        """ Run the validation

        """
        self.validate_attributes_definition()
        self.validate_parent_apis_definition()
        self.validate_self_api_definition()

    ## Attributes Validation

    def _validate_candidate_attribute(self, specification_attribute_definition, candidate_attribute_definition, attr_name, token):
        """ Validate given token in the candidate information

        """
        if not token in candidate_attribute_definition:

            self.attribute_errors.append(APISpecMissingTokenError(attribute_name=attr_name, token=token))
            return False

        if candidate_attribute_definition[token] != specification_attribute_definition[token]:

            self.attribute_errors.append(APISpecAttributeDefinitionError(attribute_name=attr_name, token=token, expected_value=specification_attribute_definition[token], actual_value=candidate_attribute_definition[token]))
            return False

        elif token is "allowedChoices" and specification_attribute_definition["type"] == "enum":

            specification_choices      = ", ".join(sorted(specification_attribute_definition[token]))
            candidate_choices = ", ".join(sorted(candidate_attribute_definition[token]))

            if candidate_choices != specification_choices:

                self.attribute_errors.append(APISpecAttributeDefinitionError(attribute_name=attr_name, token=token, expected_value=specification_attribute_definition[token], actual_value=candidate_attribute_definition[token]))
                return False

        return True


    def validate_attributes_definition(self):
        """ Validate a attributes definition

        """
        specification_attributes_definition = self.specification["model"]["attributes"]
        candidate_attributes_definition     = self.candidate["model"]["attributes"]

        for attribute_name in specification_attributes_definition:

            if attribute_name in IGNORED_ATTRIBUTES:
                continue

            if not attribute_name in candidate_attributes_definition:
                if attribute_name.lower() in [attr.lower() for attr in candidate_attributes_definition]:
                    self.attribute_errors.append(APISpecAttributeCapitalizationError(attribute_name=attribute_name))
                else:
                    self.attribute_errors.append(APISpecMissingAttributeDefinitionError(attribute_name=attribute_name))

            else:
                specification_attribute_definition      = specification_attributes_definition[attribute_name]
                candidate_attribute_definition = candidate_attributes_definition[attribute_name]

                self._validate_candidate_attribute(specification_attribute_definition, candidate_attribute_definition, attribute_name, "required")
                self._validate_candidate_attribute(specification_attribute_definition, candidate_attribute_definition, attribute_name, "type")
                self._validate_candidate_attribute(specification_attribute_definition, candidate_attribute_definition, attribute_name, "uniqueItems")
                self._validate_candidate_attribute(specification_attribute_definition, candidate_attribute_definition, attribute_name, "allowedChoices")


    ## APIs Validation

    def _validate_candidate_api(self, api_path, specification_parent_api_definition, candidate_parent_api_definition, target_reports):
        """ Check all methods are correct

        """
        specification_methods = ", ".join([operation["method"] for operation in sorted(specification_parent_api_definition["operations"])])
        candidate_methods     = ", ".join([operation["method"] for operation in sorted(candidate_parent_api_definition["operations"])])

        if candidate_methods != specification_methods:
            target_reports.append(APISpecMissingAPIMethodError(api_path=api_path, expected_methods=specification_methods, actual_methods=candidate_methods))
            return False

        return True

    def validate_self_api_definition(self):
        """ Validate self API information

        """
        import pprint
        pprint.pprint(self.specification)
        specification_self_apis_definition = self.specification["apis"]["self"]
        candidate_self_apis_definition     = self.candidate["apis"]["self"]

        for api_path in specification_self_apis_definition:

            if not api_path in candidate_self_apis_definition:
                self.self_api_errors.append(APISpecMissingSelfAPIError(api_path))

            else:
                specification_self_api_definition = specification_self_apis_definition[api_path]
                candidate_self_api_definition     = candidate_self_apis_definition[api_path]

                self._validate_candidate_api(api_path, specification_self_api_definition, candidate_self_api_definition, self.self_api_errors)


    def validate_parent_apis_definition(self):
        """ Validate Parent API information

        """
        specification_parent_apis_definition = self.specification["apis"]["parents"]
        candidate_parent_apis_definition     = self.candidate["apis"]["parents"]

        for api_path in specification_parent_apis_definition:

            if not api_path in candidate_parent_apis_definition:
                self.parent_api_errors.append(APISpecMissingAPIError(api_path))

            else:
                specification_parent_api_definition = specification_parent_apis_definition[api_path]
                candidate_parent_api_definition     = candidate_parent_apis_definition[api_path]

                self._validate_candidate_api(api_path, specification_parent_api_definition, candidate_parent_api_definition, self.parent_api_errors)

