# -*- coding: utf-8 -*-

import base64
import json
import os
import tempfile
import requests
import zipfile

from functools import partial
from github import Github
from multiprocessing.pool import ThreadPool
from monolithe.lib import merge_dict

from .specification import Specification


class RepositoryManager (object):
    """ RepositoryManager is an object that allows to manipulate the API specification repository
    """

    def __init__(self, monolithe_config, api_url, login_or_token, password, organization, repository, repository_path="/"):
        """ Initialize RepositoryManager

            Args:
                api_url: the API url for Github
                login_or_token: the authentication token or login for Github
                password: the authentication password for Github (only if login_or_token is a username)
                organization: the organization where specifications_repository is
                repository: the repository containing the specifications
        """
        self._monolithe_config = monolithe_config;
        self._repository = repository
        self._repository_path = repository_path

        if len(self._repository_path) > 1:
            if self._repository_path[0] == "/":
                self._repository_path = self._repository_path[1:]

            if self._repository_path[-1] == "/":
                self._repository_path = self._repository_path[:-1]

        self._github = Github(login_or_token=login_or_token, password=password, base_url=api_url)
        self._repo = self._github.get_organization(organization).get_repo(repository)


    @property
    def repository(self):
        return self._repository

    def get_available_branches(self):
        """ Returns the list of available API spec branches

            Returns:
                list of all available specification branches
        """

        return [branch.name for branch in self._repo.get_branches()]

    def get_available_specifications(self, branch="master"):
        """ Returns the list of available specification files

            Args:
                branch: the branch where to find files (default: "master")

            Returns:
                list of all available specification files in the given branch
        """

        ret = []

        for file in self._repo.get_dir_contents(self._repository_path, ref=branch):

            if os.path.splitext(file.name)[1] != ".spec" or file.name.startswith("@"):
                continue

            ret.append(file.name)

        return ret

    def get_api_info(self, branch="master"):
        """
            Returns the content of the api.info in the specification

            Args:
                branch: the branch where to the api info (default: "master")

            Returns:
                the server api version as dict containing the keys "version", "prefix" and "root"
        """
        path = os.path.normpath("%s/%s" % (self._repository_path, "api.info"))
        try:
            return json.loads(base64.b64decode(self._repo.get_file_contents(path, ref=branch).content))
        except Exception as e:
            raise Exception("could not parse api.info", e)

    def get_last_commit(self, branch="master"):
        """
            Returns the last commit in the given branch

            Args:
                branch: the branch where to the commit (default: "master")
        """

        return self._repo.get_commits()[0]


    def get_all_specifications(self, branch="master"):
        """ Returns all availables specifications using zipball feature of Github
            This is extremely fast if you need to get a lot of Specifications in one
            shot.

            Args:
                branch: the branch where to find files (default: "master")

            Returns:
                list of Specification objects.
        """
        specifications = []
        archive_fd, archive_path = tempfile.mkstemp("archive.zip")
        url = self._repo.get_archive_link("zipball", ref=branch)
        req = requests.get(url, stream=True, verify=False)

        # retrieve and write the archive content to a temporary file
        with open(archive_path, "wb") as f:
            for chunk in req.iter_content(chunk_size=1024):
                if not chunk:
                    continue
                f.write(chunk)
                f.flush()

        # reads the content of the archive and generate Specification objects
        with zipfile.ZipFile(archive_path, "r") as archive_content:
            for file_name in archive_content.namelist():

                spec_name = os.path.split(file_name)[1]

                if spec_name == "api.info":
                    continue

                if os.path.splitext(spec_name)[1] != ".spec" or spec_name.startswith("@"):
                    continue

                specifications.append(Specification(data=self.get_specification_data(name=spec_name, archive=archive_content), monolithe_config=self._monolithe_config))

        # cleanup the temporary archive
        os.close(archive_fd)
        os.remove(archive_path)

        return specifications

    def get_specification_data(self, name, branch="master", archive=None):
        """ Returns the content of the specification_file in the given branch

            Args:
                name: the name of the specification file of which you want to get the content
                branch: the branch where to find files (default: "master")

            Returns:
                JSON decoded structure of the specification file.
        """
        data = {}
        full_path = None

        if archive:
            full_path = os.path.normpath("%s%s/%s" % (archive.namelist()[0], self._repository_path, name))
            try:
                data = json.loads(archive.read(full_path))
            except Exception as e:
                raise Exception("could not parse %s" % name, e)
        else:
            full_path = os.path.normpath("%s/%s" % (self._repository_path, name))
            try:
                data = json.loads(base64.b64decode(self._repo.get_file_contents(full_path, ref=branch).content))
            except Exception as e:
                raise Exception("could not parse %s" % name, e)

        if "model" in data and "extends" in data["model"]:
            for extension in data["model"]["extends"]:
                data = merge_dict(data, self.get_specification_data(name="%s.spec" % extension, branch=branch, archive=archive))

        return data


    def get_specification(self, name, branch="master", archive=None):
        """ Returns a Specification object from the given specification file name in the given branch

            Args:
                name: the name of the specification file of which you want to get the content
                branch: the branch where to find files (default: "master")

            Returns:
                Specification object.
        """
        return Specification(data=self.get_specification_data(name, branch, archive), monolithe_config=self._monolithe_config)

    def get_specifications(self, names, branch="master", callback=None):
        """ Returns a Specification object from the given specification file name in the given branch

            Args:
                name: the name of the specification file of which you want to get the content
                branch: the branch where to find files (default: "master")

            Returns:
                list of Specification objects.
        """
        def internal_get_specification(name, branch, callback):
            """
            """
            specification = self.get_specification(name=name, branch=branch)

            if callback:
                callback(specification)

            return specification

        func = partial(internal_get_specification, branch=branch, callback=callback)

        return ThreadPool(40).map(func, names)

    def save_specification(self, specification, branch="master", commit_message="updated using monolithe"):
        """ Saves (commit) a specification to the Github Repository

            Args:
                specification: the specification object to save
                branch: the branch where to commit (default: "master")
                commit_message: the commit message (default: "updated using monolithe")

        """

        pass
