# -*- coding: utf-8 -*-

import os
import json
from apispecificationvalidator import APISpecificationValidator

class SpecificationsValidator:
    """ Validates an entire spec candidate folder against an entire spec folder

    """

    def __init__(self, specification_path, candidate_path):
        """ Initialize the validator

        """
        self._candidate_files     = []
        self._candidate_path      = candidate_path
        self._specification_files = []
        self._specification_path  = specification_path
        self._report              = {};
        self._mode                = None

        if os.path.isdir(self._specification_path) and os.path.isdir(self._candidate_path):
            self._specification_files = [file for file in os.listdir(self._specification_path)]
            self._candidate_files     = [file for file in os.listdir(self._candidate_path)]
            self._mode                = "folder"

        elif not os.path.isdir(self._specification_path) and not os.path.isdir(self._candidate_path):
            self._specification_files = [self._specification_path]
            self._candidate_files     = [self._candidate_path]
            self._mode                = "file"

        else:
            raise Exception("You must either pass two folers or two files.")


    def run(self):
        """ Run the validator

        """

        if self._mode == "file":
            self._run_file_mode()
        else:
            self._run_folder_mode()



    def _run_file_mode(self):
        """ Run validation against two files

        """
        self._validate_files(self._specification_files[0], self._candidate_files[0]);

    def _run_folder_mode(self):
        """ Run validation against two folders

        """
        for file in self._specification_files:

            specification_file = os.path.join(self._specification_path, file)
            candidate_file     = os.path.join(self._candidate_path, file)

            if os.path.splitext(specification_file)[1] != ".spec":
                continue

            if not os.path.exists(candidate_file):
                self._report[os.path.basename(specification_file)] = None
                continue

            self._validate_files(specification_file, candidate_file);

    def _validate_files(self, specification_file_path, candidate_file_path):
        """ Actually performs validation against to files

        """
        with open(specification_file_path, 'r') as specification_file, open(candidate_file_path, 'r') as candidate_file:
            specification_data = json.loads(specification_file.read())
            candidate_data     = json.loads(candidate_file.read())

        spec_validator = APISpecificationValidator(specification_data, candidate_data)
        spec_validator.run()
        self._report[os.path.basename(specification_file_path)] = spec_validator


    def print_console_report(self):
        """ Print the report as text

        """
        missing_candidate_count      = 0
        parent_apis_validation_count = 0
        self_apis_validation_count   = 0
        attribute_validation_count   = 0

        for entity, validation in sorted(self._report.items()):
            errored = False

            out = "\n\033[95mSpecification Validation Report for entity '%s'\033[0m\n\n" % entity

            if not validation:
                errored = True
                out = "%s\n - missing candidate file." % out
                missing_candidate_count = missing_candidate_count + 1

            else:

                if len(validation.attribute_errors):
                    errored = True
                    out = "%s\033[91mattribute conformity errors\033[0m" % out
                    for error in validation.attribute_errors:
                        attribute_validation_count = attribute_validation_count + 1
                        out = "%s\n     %s" % (out, error)
                    out = "%s\n\n" % out

                if len(validation.parent_api_errors):
                    errored = True
                    out = "%s\033[91mparent api conformity errors\033[0m" % out
                    for error in validation.parent_api_errors:
                        parent_apis_validation_count = parent_apis_validation_count + 1
                        out = "%s\n     %s" % (out, error)
                    out = "%s\n\n" % out

                if len(validation.self_api_errors):
                    errored = True
                    out = "%s\033[91mself api conformity errors\033[0m" % out
                    for error in validation.self_api_errors:
                        self_apis_validation_count = self_apis_validation_count + 1
                        out = "%s\n     %s" % (out, error)
                    out = "%s\n\n" % out

            if errored:
                print out

        missing_candidates = "\033[92m0\033[0m"  if not missing_candidate_count else "\033[91m%d\033[0m" % missing_candidate_count
        validation_errors = "\033[92m0\033[0m"  if not attribute_validation_count else "\033[91m%d\033[0m" % attribute_validation_count
        parent_apis_errors = "\033[92m0\033[0m"  if not parent_apis_validation_count else "\033[91m%d\033[0m" % parent_apis_validation_count
        self_apis_errors = "\033[92m0\033[0m"  if not self_apis_validation_count else "\033[91m%d\033[0m" % self_apis_validation_count

        print "missing apis: %s, self api validation errors: %s, parent api validation errors: %s, attribute validation errors: %s\n" % (missing_candidates, self_apis_errors, parent_apis_errors, validation_errors)

