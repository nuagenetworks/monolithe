# -*- coding: utf-8 -*-

import os
from validationerrors import APISpecAttributeCharacteristicError
from validationerrors import APISpecAttributeCapitalizationError
from validationerrors import APISpecAttributeMissingCharacteristicError
from validationerrors import APISpecAttributeMissingDefinitionError
from validationerrors import APISpecAPIMissingError
from validationerrors import APISpecAPIMissingMethodError

IGNORED_ATTRIBUTES = ["parentType", "lastUpdatedBy", "externalID", "lastUpdatedDate", "parentID", "owner", "creationDate", "ID"]


class APISpecificationValidator:
    """ Valdidate a candidate spec file against a spec file

    """

    def __init__(self, specification, candidate):
        """ Initialize the validator

        """
        self.candidate          = candidate
        self.specification      = specification
        self.parent_api_errors  = {}
        self.self_api_errors    = {}
        self.attribute_errors   = {}

    def run(self):
        """ Run the validation

        """
        self.validate_attributes_definition()
        self.validate_parent_apis_definition()
        self.validate_self_api_definition()


    def _append_validation_error(self, report, key, error_type, error):

        if not key in report:
            report[key] = {}

        if not error_type in report[key]:
            report[key][error_type] = []

        report[key][error_type].append(error)


    ## Attributes Validation

    def _validate_candidate_attribute(self, specification_attribute_definition, candidate_attribute_definition, attr_name, characteristic):
        """ Validate given characteristic in the candidate information

        """

        if not characteristic in candidate_attribute_definition:
            err = APISpecAttributeMissingCharacteristicError(attribute_name=attr_name, characteristic=characteristic)
            self._append_validation_error(self.attribute_errors, attr_name, "missing_characteristics", err)
            return False

        if candidate_attribute_definition[characteristic] != specification_attribute_definition[characteristic]:
            err = APISpecAttributeCharacteristicError(attribute_name=attr_name,
                                                        characteristic=characteristic,
                                                        expected_value=specification_attribute_definition[characteristic],
                                                        actual_value=candidate_attribute_definition[characteristic])

            self._append_validation_error(self.attribute_errors, attr_name, "characteristic_errors", err)
            return False

        elif characteristic is "allowedChoices" and specification_attribute_definition["type"] == "enum":

            specification_choices      = ", ".join(sorted(specification_attribute_definition[characteristic]))
            candidate_choices = ", ".join(sorted(candidate_attribute_definition[characteristic]))

            if candidate_choices != specification_choices:
                err = APISpecAttributeCharacteristicError(attribute_name=attr_name,
                                                            characteristic=characteristic,
                                                            expected_value=specification_attribute_definition[characteristic],
                                                            actual_value=candidate_attribute_definition[characteristic])

                self._append_validation_error(self.attribute_errors, attr_name, "characteristic_errors", err)

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
                    err = APISpecAttributeCapitalizationError(attribute_name=attribute_name)
                    self._append_validation_error(self.attribute_errors, attribute_name, "capitalization_errors", err)
                else:
                    err = APISpecAttributeMissingDefinitionError(attribute_name=attribute_name)
                    self._append_validation_error(self.attribute_errors, attribute_name, "missing_attributes", err)

            else:
                specification_attribute_definition = specification_attributes_definition[attribute_name]
                candidate_attribute_definition     = candidate_attributes_definition[attribute_name]

                for characteristic in specification_attribute_definition:
                    self._validate_candidate_attribute(specification_attribute_definition, candidate_attribute_definition, attribute_name, characteristic)


    ## APIs Validation

    def _validate_candidate_api(self, api_path, specification_parent_api_definition, candidate_parent_api_definition, target_reports):
        """ Check all methods are correct

        """
        specification_methods = ", ".join([operation["method"] for operation in sorted(specification_parent_api_definition["operations"])])
        candidate_methods     = ", ".join([operation["method"] for operation in sorted(candidate_parent_api_definition["operations"])])

        if candidate_methods != specification_methods:
            err = APISpecAPIMissingMethodError(api_path=api_path, expected_methods=specification_methods, actual_methods=candidate_methods)
            self._append_validation_error(target_reports, api_path, "method_errors", err)
            return False

        return True

    def validate_self_api_definition(self):
        """ Validate self API information

        """
        specification_self_apis_definition = self.specification["apis"]["self"]
        candidate_self_apis_definition     = self.candidate["apis"]["self"]

        for api_path in specification_self_apis_definition:

            if not api_path in candidate_self_apis_definition:
                err = APISpecAPIMissingError(api_path)
                self._append_validation_error(self.self_api_errors, api_path, "missing_apis", err)

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
                err = APISpecAPIMissingError(api_path)
                self._append_validation_error(self.parent_api_errors, api_path, "missing_apis", err)

            else:
                specification_parent_api_definition = specification_parent_apis_definition[api_path]
                candidate_parent_api_definition     = candidate_parent_apis_definition[api_path]

                self._validate_candidate_api(api_path, specification_parent_api_definition, candidate_parent_api_definition, self.parent_api_errors)

