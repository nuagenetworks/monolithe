# -*- coding: utf-8 -*-

import os
import json
import base64
from .apispecificationvalidator import APISpecificationValidator
from monolithe.generators.specifications import SpecificationsGenerator
from github import Github
from requests.exceptions import ConnectionError


class SpecificationsValidator (object):
    """ SpecificationsValidator is an object that allows to use monolithe.APISpecificationValidator
        using a github repository for specifications and a running VSD for candidate specifications
    """

    def __init__(self, github_api_url, github_token, specification_organization, github_specifications_repository):
        """ Initialize FindACoolName

            Args:
                github_api_url: the API url for Github
                github_token: the authentication token for Github
                specification_organization: the organization where github_specifications_repository is
                github_specifications_repository: the repository containing the specifications
        """

        self._github                    = Github(login_or_token=github_token, base_url=github_api_url)
        self._github_specification_repo = self._github.get_organization(specification_organization).get_repo(github_specifications_repository)

    def available_specification_versions(self):
        """ Returns the list of available API spec versions

            Returns:
                list of all available specification branches
        """

        return [branch.name for branch in self._github_specification_repo.get_branches()]

    def available_specification_files(self, specification_version="master"):
        """ Returns the list of available specification files

            Args:
                specification_version: the version (branch) where to find files (default: "master")

            Returns:
                list of all available specification files in the given version
        """

        ret = []

        for file in self._github_specification_repo.get_dir_contents("/", ref=specification_version):

            if os.path.splitext(file.name)[1] != ".spec":
                continue

            ret.append(file.name)

        return ret

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

            github_encoded_data = self._github_specification_repo.get_file_contents(specification_file, ref=specification_version).content
            specification_data  = json.loads(base64.b64decode(github_encoded_data))
            rest_name           = specification_data["model"]["RESTName"]

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
