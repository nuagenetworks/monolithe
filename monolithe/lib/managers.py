# -*- coding: utf-8 -*-

import threading
import os
import json
import base64
from github import Github

from monolithe.lib.models import Specification


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

    def __init__(self, api_url, login_or_token, password, organization, repository):
        """ Initialize SpecificationsRepositoryManager

            Args:
                api_url: the API url for Github
                login_or_token: the authentication token or login for Github
                password: the authentication password for Github (only if login_or_token is a username)
                organization: the organization where specifications_repository is
                repository: the repository containing the specifications
        """
        self._repository = repository

        self._github = Github(login_or_token=login_or_token, password=password, base_url=api_url)
        self._repo = self._github.get_organization(organization).get_repo(repository)

    @property
    def repository(self):
        """
        """
        return self._repository

    def available_versions(self):
        """ Returns the list of available API spec versions (branches)

            Returns:
                list of all available specification versions (branches)
        """

        return [branch.name for branch in self._repo.get_branches()]

    def available_specifications(self, version="master"):
        """ Returns the list of available specification files

            Args:
                specification_version: the version (branch) where to find files (default: "master")

            Returns:
                list of all available specification files in the given version
        """

        ret = []

        for file in self._repo.get_dir_contents("/", ref=version):

            if os.path.splitext(file.name)[1] != ".spec":
                continue

            ret.append(file.name)

        return ret

    def get_specification_data(self, name, version="master"):
        """ Returns the content of the specification_file in the given specification_version

            Args:
                name: the name of the specification file of which you want to get the content
                version: the version (branch) where to find files (default: "master")

            Returns:
                JSON decoded structure of the specification file.
        """

        encoded_data = self._repo.get_file_contents(name, ref=version).content
        return json.loads(base64.b64decode(encoded_data))

    def get_specification(self, name, version="master"):
        """ Returns a Specification object from the given specification file name in the given specification_version

            Args:
                name: the name of the specification file of which you want to get the content
                version: the version (branch) where to find files (default: "master")

            Returns:
                Specification object.
        """

        data = self.get_specification_data(name, version)
        return Specification(data=data)

    def save_specification(self, specification, version="master", commit_message="updated using monolithe"):
        """ Saves (commit) a specification to the Github Repository

            Args:
                specification: the specification object to save
                version: the version (branch) where to commit (default: "master")
                commit_message: the commit message (default: "updated using monolithe")
        """

        pass
