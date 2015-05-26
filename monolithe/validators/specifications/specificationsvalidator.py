# -*- coding: utf-8 -*-

import os
import json
import base64
from .apispecificationvalidator import APISpecificationValidator
from monolithe.generators.specifications import SpecificationsGenerator
from requests.exceptions import ConnectionError


class SpecificationsValidator (object):
    """ SpecificationsValidator is an object that will validate multiple API specifications
    """

    def __init__(self, specification_repository_manager):
        self._specification_repository_manager = specification_repository_manager

    def insert_reporting(self, reports, name, processing_error=None, contents=None):
        """ Insert a reporting in given report list

            Args:
                reports: target dictionary where the report must be inserted
                name: string representing the report name
                processing_error: string representing a processing error
                contents: list representing the content of the reporting
        """

        reports.append({"rest_name": name,  "processing_error": processing_error,  "contents": contents})

    def run_validation(self, specification_version, specification_files, vsd_server_url, vsd_api_version):
        """ Perform Validation using APISpecificationValidator

            Args:
                specification_version: the version (branch) of the specification
                specification_files: the specification files to validate
                vsd_server_url: the url of the VSD server that you want to validate
                vsd_server_url: the api version of the VSD server that you want to validate

            Returns:
                tupple containing the validation report, and all teh json specification data to generate that report.
        """
        reports                = []
        all_specification_data = {}

        for specification_file in specification_files:

            specification_data = self._specification_repository_manager.specification_contents(specification_version=specification_version, specification_file=specification_file)
            rest_name          = specification_data["model"]["RESTName"]

            ## Try to get the candidate specification from VSD
            try:
                specification_generator = SpecificationsGenerator(vsdurl=vsd_server_url, apiversion=vsd_api_version, swagger_path=None)
                candidate_data = specification_generator.get_specification(rest_name=rest_name)
            except ConnectionError as error:
                self.insert_reporting(reports, name=rest_name, processing_error=error)
                continue

            ## If we can't get any, we add a processing error
            if not candidate_data:
                err = ValueError("Could not get any specification candidate")
                self.insert_reporting(reports, name=rest_name, processing_error=err)
                continue

            ## If it's ok, we run the validation
            all_specification_data[specification_file] = specification_data
            validator = APISpecificationValidator(specification_data, candidate_data)
            validator.run()

            self_api_errors   = validator.self_api_errors
            parent_api_errors = validator.parent_api_errors
            attribute_errors  = validator.attribute_errors

            ## If there are some validation we add the reporting
            if len(attribute_errors) or len(parent_api_errors) or len(self_api_errors):
                contents = {"self_api_errors": self_api_errors, "parent_api_errors": parent_api_errors, "attribute_errors": attribute_errors}
                self.insert_reporting(reports, name=rest_name, contents=contents)

        return (reports, all_specification_data)
