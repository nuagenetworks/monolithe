# -*- coding: utf-8 -*-

import os
import difflib
from exceptions import *


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
            err = APISpecAttributeMissingCharacteristicException(attribute_name=attr_name, characteristic=characteristic)
            self._append_validation_error(self.attribute_errors, attr_name, "missing_characteristics", err)
            return False

        if candidate_attribute_definition[characteristic] != specification_attribute_definition[characteristic]:
            err = APISpecAttributeCharacteristicException(attribute_name=attr_name,
                                                        characteristic=characteristic,
                                                        expected_value=specification_attribute_definition[characteristic],
                                                        actual_value=candidate_attribute_definition[characteristic])

            self._append_validation_error(self.attribute_errors, attr_name, "characteristic_errors", err)
            return False

        elif characteristic is "allowedChoices" and specification_attribute_definition["type"] == "enum":

            specification_choices      = ", ".join(sorted(specification_attribute_definition[characteristic]))
            candidate_choices = ", ".join(sorted(candidate_attribute_definition[characteristic]))

            if candidate_choices != specification_choices:
                err = APISpecAttributeCharacteristicException(attribute_name=attr_name,
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

        ## check for missing attributes or wrong characteristic
        for attribute_name in specification_attributes_definition:

            if attribute_name in IGNORED_ATTRIBUTES:
                continue

            if not attribute_name in candidate_attributes_definition:

                search_list = {}
                for key in candidate_attributes_definition.keys():
                    search_list[key.lower()] = key

                potential_matches = difflib.get_close_matches(attribute_name, search_list.keys())
                final_matches = [search_list[key] for key in potential_matches]
                if len(potential_matches):
                    err = APISpecAttributeMispelledDeclarationException(attribute_name=attribute_name, potential_attributes=final_matches)
                    self._append_validation_error(self.attribute_errors, attribute_name, "mispelling_errors", err)
                else:
                    err = APISpecAttributeMissingDeclarationException(attribute_name=attribute_name)
                    self._append_validation_error(self.attribute_errors, attribute_name, "missing_attributes", err)

            else:
                specification_attribute_definition = specification_attributes_definition[attribute_name]
                candidate_attribute_definition     = candidate_attributes_definition[attribute_name]

                for characteristic in specification_attribute_definition:
                    self._validate_candidate_attribute(specification_attribute_definition, candidate_attribute_definition, attribute_name, characteristic)

        ## Check for extra attribiutes in candidate spec
        for attribute_name in candidate_attributes_definition:

            if attribute_name in IGNORED_ATTRIBUTES:
                continue

            if not attribute_name in specification_attributes_definition:
                err = APISpecAttributeExtraDeclarationException(attribute_name=attribute_name)
                self._append_validation_error(self.attribute_errors, attribute_name, "extra_attributes_errors", err)


    ## APIs Validation

    def _validate_candidate_api(self, api_path, specification_parent_api_definition, candidate_parent_api_definition, target_reports):
        """ Check all methods are correct

        """
        specification_methods = ", ".join([operation["method"] for operation in sorted(specification_parent_api_definition["operations"])])
        candidate_methods     = ", ".join([operation["method"] for operation in sorted(candidate_parent_api_definition["operations"])])

        if candidate_methods != specification_methods:
            err = APISpecAPIMissingMethodException(api_path=api_path, expected_methods=specification_methods, actual_methods=candidate_methods)
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
                err = APISpecAPIMissingException(api_path)
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
                err = APISpecAPIMissingException(api_path)
                self._append_validation_error(self.parent_api_errors, api_path, "missing_apis", err)

            else:
                specification_parent_api_definition = specification_parent_apis_definition[api_path]
                candidate_parent_api_definition     = candidate_parent_apis_definition[api_path]

                self._validate_candidate_api(api_path, specification_parent_api_definition, candidate_parent_api_definition, self.parent_api_errors)

