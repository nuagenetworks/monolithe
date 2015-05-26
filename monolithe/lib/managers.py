# -*- coding: utf-8 -*-

import threading
import os
import json
import base64
from github import Github


class TaskManager(object):
    """ Multi threading manager """

    def __init__(self):
        """ Initializes a TaskManager

        """
        self.threads = list()

    def wait_until_exit(self):
        """ Wait until all the threads are finished.

        """
        [t.join() for t in self.threads]

        self.threads = list()

    def start_task(self, method, *args, **kwargs):
        """ Start a task in a separate thread

            Args:
                method: the method to start in a separate thread
                args: Accept args/kwargs arguments
        """
        thread = threading.Thread(target=method, args=args, kwargs=kwargs)
        thread.is_daemon = False
        thread.start()
        self.threads.append(thread)


class SpecificationsRepositoryManager (object):
    """ SpecificationsRepositoryManager is an object that allows to manipulate the API specification repository
    """

    def __init__(self, github_api_url, github_token, specification_organization, github_specifications_repository):
        """ Initialize SpecificationsRepositoryManager

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

    def specification_contents(self, specification_file, specification_version="master"):
        """ Returns the content of the specification_file in the given specification_version

            Args:
                specification_version: the version (branch) where to find files (default: "master")
                specification_file: file name

            Returns:
                JSON encoded data of the specification file.
        """
        github_encoded_data = self._github_specification_repo.get_file_contents(specification_file, ref=specification_version).content
        return json.loads(base64.b64decode(github_encoded_data))

