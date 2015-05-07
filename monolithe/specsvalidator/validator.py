# -*- coding: utf-8 -*-

import os
from apivalidator import APIValidator

class Validator:
    """ Validates an entire spec candidate folder against an entire spec folder

    """

    def __init__(self, specification_path, candidate_path):
        """ Initialize the validator

        """
        self._report       = {};
        self.specification_path = specification_path
        self.candidate_path     = candidate_path

    def run(self):
        """ Run the validator

        """
        if os.path.isdir(self.specification_path) and os.path.isdir(self.candidate_path):

            for file in os.listdir(self.specification_path):

                file_name = os.path.splitext(file)[0]
                file_ext  = os.path.splitext(file)[1]

                if file_ext != ".spec":
                    continue

                if not os.path.exists("%s/%s" % (self.candidate_path, file)):
                    self.final_report[file_name] = None
                    continue

                specification_file_path = "%s/%s" % (self.specification_path, file)
                candidate_file_path     = "%s/%s" % (self.candidate_path, file)

                spec_validator = APIValidator(specification_file_path, candidate_file_path)
                spec_validator.run()
                self._report[file_name] = spec_validator

    def print_console_report(self):
        """ Print the report as text

        """
        missing_candidate_count      = 0
        parent_apis_validation_count = 0
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
                    out = "%s\033[91mapi conformity errors\033[0m" % out
                    for error in validation.parent_api_errors:
                        parent_apis_validation_count = parent_apis_validation_count + 1
                        out = "%s\n     %s" % (out, error)
                    out = "%s\n\n" % out

            if errored:
                print out

        missing_candidates = "\033[92m0\033[0m"  if not missing_candidate_count else "\033[91m%d\033[0m" % missing_candidate_count
        validation_errors = "\033[92m0\033[0m"  if not parent_apis_validation_count else "\033[91m%d\033[0m" % parent_apis_validation_count
        api_errors = "\033[92m0\033[0m"  if not attribute_validation_count else "\033[91m%d\033[0m" % attribute_validation_count

        print "missing apis: %s, api validation errors: %s, attribute validation errors: %s\n" % (missing_candidates, validation_errors, api_errors)

