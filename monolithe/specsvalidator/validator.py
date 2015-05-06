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
            print "Specification Validation Report for entity '%s'" % entity
            print ""

            if not validation:
                print " - missing candidate file."
                missing_candidate_count = missing_candidate_count + 1
                continue

            if not len(validation.attribute_errors):
                print " - attributes specification:  \033[92mCONFORM\033[0m"
            else:
                print " - attributes specification:  \033[91mNOT CONFORM\033[0m"
                for error in validation.attribute_errors:
                    attribute_validation_count = attribute_validation_count + 1
                    print "     %s" % error
                print ""

            if not len(validation.parent_api_errors):
                print " - parent apis specification: \033[92mCONFORM\033[0m"
            else:
                print " - parent apis specification: \033[91mNOT CONFORM\033[0m"
                for error in validation.parent_api_errors:
                    parent_apis_validation_count = parent_apis_validation_count + 1
                    print "     %s" % error
                print ""

            print ""
            print ""

        print "\nmissing apis: %d, api validation errors: %d, attribute validation errors: %d" % (missing_candidate_count, parent_apis_validation_count, attribute_validation_count)

