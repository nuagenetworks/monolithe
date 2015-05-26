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
        self.validate_attributes_declarations()
        self.validate_parent_apis_declarations()
        self.validate_self_api_declarations()


    def _append_validation_error(self, report, key, error_type, error):
        """ Append a new reporting in the given report
        """
        if not key in report: report[key] = {}
        if not error_type in report[key]: report[key][error_type] = []
        report[key][error_type].append(error)


    def _check_similarities(self, word, corpus):
        """ Find similarity of a given word from an array or words
        """
        search_list = {}
        for key in corpus: search_list[key.lower()] = key
        potential_matches = difflib.get_close_matches(word.lower(), search_list.keys())
        return [search_list[key] for key in potential_matches] if len(potential_matches) else None


    ## Attributes Validation

    def validate_attributes_declarations(self):
        """ Validate a attributes definition
        """
        specification_attributes_definition = self.specification["model"]["attributes"]
        candidate_attributes_definition     = self.candidate["model"]["attributes"]
        mispellings                         = []

        ## check for missing attributes or wrong characteristic
        for attribute_name in specification_attributes_definition:

            if attribute_name in IGNORED_ATTRIBUTES:
                continue

            if not attribute_name in candidate_attributes_definition:

                similarities = self._check_similarities(attribute_name, candidate_attributes_definition.keys())

                if similarities:
                    err = MispelledDeclarationException(declaration_name=attribute_name, potential_declarations=similarities)
                    self._append_validation_error(self.attribute_errors, attribute_name, "mispelled_declarations", err)
                    mispellings.extend(similarities)
                else:
                    err = MissingDeclarationException(declaration_name=attribute_name)
                    self._append_validation_error(self.attribute_errors, attribute_name, "missing_declarations", err)

            else:

                specification_attribute_definition = specification_attributes_definition[attribute_name]
                candidate_attribute_definition     = candidate_attributes_definition[attribute_name]

                for characteristic in specification_attribute_definition:

                    if not characteristic in candidate_attribute_definition:
                        err = CharacteristicMissingException(characteristic_name=characteristic)
                        self._append_validation_error(self.attribute_errors, attribute_name, "missing_characteristics", err)

                    elif candidate_attribute_definition[characteristic] != specification_attribute_definition[characteristic]:
                        err = CharacteristicMismatchException(characteristic_name=characteristic, expected_value=specification_attribute_definition[characteristic], actual_value=candidate_attribute_definition[characteristic])
                        self._append_validation_error(self.attribute_errors, attribute_name, "characteristic_mismatches", err)

                    elif characteristic is "allowedChoices" and specification_attribute_definition["type"] == "enum":
                        specification_choices = ", ".join(sorted(specification_attribute_definition[characteristic]))
                        candidate_choices     = ", ".join(sorted(candidate_attribute_definition[characteristic]))

                        if candidate_choices != specification_choices:
                            err = CharacteristicMismatchException(characteristic_name=characteristic, expected_value=specification_attribute_definition[characteristic], actual_value=candidate_attribute_definition[characteristic])
                            self._append_validation_error(self.attribute_errors, attribute_name, "characteristic_mismatches", err)

        ## Check for extra attribiutes in candidate spec
        for attribute_name in candidate_attributes_definition:

            if attribute_name in IGNORED_ATTRIBUTES:
                continue

            if attribute_name in mispellings:
                continue

            if not attribute_name in specification_attributes_definition:

                err = ExtraDeclarationException(declaration_name=attribute_name)
                self._append_validation_error(self.attribute_errors, attribute_name, "extra_declarations", err)


    ## APIs Validation

    def _validate_api_declarations(self, specification_api_declarations, candidate_api_declarations, target_report):
        """ Perform validations on api declarations
        """
        mispellings = []

        ## check for missing apis or wrong operations
        for api_path in specification_api_declarations:

            if not api_path in candidate_api_declarations:

                similarities = self._check_similarities(api_path, candidate_api_declarations.keys())

                if similarities:
                    err = MispelledDeclarationException(declaration_name=api_path, potential_declarations=similarities)
                    self._append_validation_error(target_report, api_path, "mispelled_declarations", err)
                    mispellings.extend(similarities)
                else:
                    err = MissingDeclarationException(declaration_name=api_path)
                    self._append_validation_error(target_report, api_path, "missing_declarations", err)

            else:

                specification_methods = ", ".join([operation["method"] for operation in sorted(specification_api_declarations[api_path]["operations"])])
                candidate_methods     = ", ".join([operation["method"] for operation in sorted(candidate_api_declarations[api_path]["operations"])])

                if candidate_methods != specification_methods:
                    err = CharacteristicMismatchException(characteristic_name="methods", expected_value=specification_methods, actual_value=candidate_methods)
                    self._append_validation_error(target_report, api_path, "characteristic_mismatches", err)

        ## check for extra apis
        for api_path in candidate_api_declarations:

            if api_path in mispellings:
                continue

            if not api_path in specification_api_declarations:
                err = ExtraDeclarationException(declaration_name=api_path)
                self._append_validation_error(target_report, api_path, "extra_declarations", err)

    def validate_self_api_declarations(self):
        """ Validate self API information
        """
        self._validate_api_declarations(self.specification["apis"]["self"], self.candidate["apis"]["self"], self.self_api_errors)


    def validate_parent_apis_declarations(self):
        """ Validate Parent API information
        """
        self._validate_api_declarations(self.specification["apis"]["parents"], self.candidate["apis"]["parents"], self.parent_api_errors)

