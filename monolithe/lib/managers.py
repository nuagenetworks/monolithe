# -*- coding: utf-8 -*-

import base64
import json
import os
import threading
import tempfile
import requests
import zipfile

from functools import partial
from github import Github
from multiprocessing.pool import ThreadPool

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

    def get_all_specifications(self, version="master"):
        """ Returns all availables specifications using zipball feature of Github
            This is extremely fast if you need to get a lot of Specifications in one
            shot.

            Args:
                version: the version (branch) where to find files (default: "master")

            Returns:
                list of Specification objects.
        """
        specifications = []
        archive_fd, archive_path = tempfile.mkstemp("archive.zip")
        url = self._repo.get_archive_link("zipball", ref=version)
        req = requests.get(url, stream=True, verify=False)

        # retrieve and write the archive content to a temporary file
        f = os.fdopen(archive_fd, "wb")
        for chunk in req.iter_content(chunk_size=1024):
            if not chunk: continue
            f.write(chunk)
            f.flush()
        os.close(archive_fd)

        # reads the content of the archive and generate Specification objects
        with zipfile.ZipFile(archive_path, "r") as archive_content:
            for file_name in archive_content.namelist():
                if os.path.splitext(file_name)[1] != ".spec": continue
                specifications.append(Specification(data=json.loads(archive_content.read(file_name))))

        # cleanup the temporary archive
        os.remove(archive_path)

        return specifications

    def get_specification_data(self, name, version="master"):
        """ Returns the content of the specification_file in the given specification_version

            Args:
                name: the name of the specification file of which you want to get the content
                version: the version (branch) where to find files (default: "master")

            Returns:
                JSON decoded structure of the specification file.
        """

        return json.loads(base64.b64decode(self._repo.get_file_contents(name, ref=version).content))

    def get_specification(self, name, version="master"):
        """ Returns a Specification object from the given specification file name in the given specification_version

            Args:
                name: the name of the specification file of which you want to get the content
                version: the version (branch) where to find files (default: "master")

            Returns:
                Specification object.
        """

        return Specification(data=self.get_specification_data(name, version))

    def get_specifications(self, names, version="master", callback=None):
        """ Returns a Specification object from the given specification file name in the given specification_version

            Args:
                name: the name of the specification file of which you want to get the content
                version: the version (branch) where to find files (default: "master")

            Returns:
                list of Specification objects.
        """
        def internal_get_specification(name, version, callback):
            """
            """
            specification = self.get_specification(name=name, version=version)

            if callback:
                callback(specification)

            return specification

        func = partial(internal_get_specification, version=version, callback=callback)

        p = ThreadPool(40)
        return p.map(func, names)

    def save_specification(self, specification, version="master", commit_message="updated using monolithe"):
        """ Saves (commit) a specification to the Github Repository

            Args:
                specification: the specification object to save
                version: the version (branch) where to commit (default: "master")
                commit_message: the commit message (default: "updated using monolithe")

        """

        pass
