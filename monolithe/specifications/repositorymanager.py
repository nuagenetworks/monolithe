# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from future import standard_library
standard_library.install_aliases()
from builtins import object

import base64
import json
import os
import tempfile
import requests
import configparser
import StringIO
import zipfile

from github import Github, InputGitTreeElement
from monolithe.lib import apply_extension

from .specification import Specification

MODE_NORMAL = 1
MODE_RAW_SPECS = 2
MODE_RAW_ABSTRACTS = 3


class RepositoryManager (object):
    """ RepositoryManager is an object that allows to manipulate the API specification repository
    """

    def __init__(self, monolithe_config, api_url, login_or_token, password, organization, repository, repository_path="/"):
        """ Initialize RepositoryManager

            Args:
                api_url: the API url for GitHub
                login_or_token: the authentication token or login for GitHub
                password: the authentication password for GitHub (only if login_or_token is a username)
                organization: the organization where specifications_repository is
                repository: the repository containing the specifications
        """
        self.monolithe_config = monolithe_config
        self._organization = organization
        self._repository = repository
        self._repository_path = repository_path

        if self._repository_path[0] == "/":
            self._repository_path = self._repository_path[1:]

        if len(self._repository_path) > 1:
            if self._repository_path[-1] == "/":
                self._repository_path = self._repository_path[:-1]

        self._github = Github(login_or_token=login_or_token, password=password, base_url=api_url)
        self._repo = self._github.get_repo("%s/%s" % (organization, repository))

    @property
    def organization(self):
        return self._organization

    @property
    def repository(self):
        return self._repository

    @property
    def repository_path(self):
        return self._repository_path

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

    def get_monolithe_config(self, branch="master"):
        """
            Returns the content of the monolithe config

            Args:
                branch: the branch where to the monolithe config (default: "master")

            Returns:
                the ConfigParserObject
        """
        path = os.path.normpath("%s/%s" % (self._repository_path, "monolithe.ini"))
        try:
            data = base64.b64decode(self._repo.get_file_contents(path, ref=branch).content)
            string_buffer = StringIO.StringIO(data)
            monolithe_config_parser = configparser.ConfigParser()
            monolithe_config_parser.readfp(string_buffer)
            return monolithe_config_parser

        except Exception as e:
            raise Exception("could not parse monolithe.ini", e)

    def get_last_commit(self, branch="master"):
        """
            Returns the last commit in the given branch

            Args:
                branch: the branch where to the commit (default: "master")
        """

        return self._repo.get_commits()[0]

    def get_repository_push_permission(self):
        """
            Returns if current user can push to the current repository
        """
        return self._repo.permissions.push

    def get_upstream_repository(self):
        """
            Returns information of the upstream repository
            if it exists, otherwise, None
        """
        return self._repo.parent

    def get_all_specifications(self, branch="master", mode=MODE_NORMAL):
        """ Returns all availables specifications using zipball feature of GitHub
            This is extremely fast if you need to get a lot of Specifications in one
            shot.

            Args:
                branch: the branch where to find files (default: "master")

            Returns:
                list of Specification objects.
        """
        specifications = {}
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

        stripped_repository_path = self.repository_path.strip("/")

        # reads the content of the archive and generate Specification objects
        with zipfile.ZipFile(archive_path, "r") as archive_content:
            for file_name in archive_content.namelist():

                spec_dir = os.path.split(file_name)[0]

                if not spec_dir.startswith(stripped_repository_path):
                    continue

                spec_name = os.path.split(file_name)[1]

                if spec_name == "api.info":
                    continue

                ext = os.path.splitext(spec_name)[1]
                is_abstract = spec_name.startswith("@")

                if ext != ".spec":
                    continue

                if mode in (MODE_NORMAL, MODE_RAW_SPECS) and is_abstract:
                    continue

                if mode == MODE_RAW_ABSTRACTS and not is_abstract:
                    continue

                specifications[spec_name.replace(".spec", "")] = Specification(filename=spec_name, data=self.get_specification_data(name=spec_name, archive=archive_content, mode=mode), monolithe_config=self.monolithe_config)

        # cleanup the temporary archive
        os.close(archive_fd)
        os.remove(archive_path)

        return specifications

    def get_specification_data(self, name, branch="master", archive=None, mode=MODE_NORMAL):
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

        if mode == MODE_NORMAL and "model" in data and "extends" in data["model"]:
            for extension in data["model"]["extends"]:
                apply_extension(self.get_specification_data(name="%s.spec" % extension, branch=branch, archive=archive, mode=MODE_NORMAL), data)

        return data

    def get_specification(self, name, branch="master", archive=None, mode=MODE_NORMAL):
        """ Returns a Specification object from the given specification file name in the given branch

            Args:
                name: the name of the specification file of which you want to get the content
                branch: the branch where to find files (default: "master")

            Returns:
                Specification object.
        """
        return Specification(filename=name, data=self.get_specification_data(name, branch, archive), monolithe_config=self.monolithe_config)

    def save_specification(self, specification, message, branch="master"):
        """
        """
        self._commit(filename=specification.filename,
                     content=json.dumps(specification.to_dict(), indent=4, sort_keys=True),
                     message=message,
                     branch=branch)

    def rename_specification(self, specification, old_name, message, branch="master"):
        """
        """
        self._delete(filename=old_name, message=message, branch=branch)
        self.save_specification(specification=specification, message=message, branch=branch)

    def delete_specification(self, specification, message, branch):
        """
        """
        self._delete(filename=specification.filename, message=message, branch=branch)

    def save_apiinfo(self, version, root_api, prefix, message, branch="master"):
        """
        """
        self._commit(filename='api.info',
                     content=json.dumps({"prefix": prefix, "root": root_api, "version": version}, indent=4, sort_keys=True),
                     message=message,
                     branch=branch)

    def save_monolithe_config(self, monolithe_config_parser, message, branch="master"):
        """
        """
        string_buffer = StringIO.StringIO()
        monolithe_config_parser.write(string_buffer)
        data = string_buffer.getvalue()

        self._commit(filename='monolithe.ini',
                     content=data,
                     message=message,
                     branch=branch)

    def merge_upstream_master(self, local_branch, upstream_branch="master", commit_message="auto merge from monolithe"):
        """
            Synchronizes current parent repo's given branch into given local branch

            Note:
                If the local repository doesn't have an upstream, this function will return False

            Args:
                local_branch: the name of the branch of the local repository you want to merge into
                upstream_repo: the name of the upstream repository branch you want to merge
                commit_message: the message for the merge commit

            Returns:
                True in case of success, or False if the local repo doesn't have an upstream
        """
        upstream_repo = self.get_upstream_repository()

        if not upstream_repo:
            return False

        upstream_last_commit = upstream_repo.get_branch(upstream_branch).commit.sha
        self._repo.merge(base=local_branch, head=upstream_last_commit, commit_message=commit_message)

        return True

    def _delete(self, filename, message, branch):
        """
        """
        # ugly manual porting of https://github.com/PyGithub/PyGithub/pull/316/files
        path = os.path.join(self._repository_path, filename)
        sha = self._repo.get_file_contents(path, branch).sha
        parameters = {"message": message, "sha": sha, "branch": branch}

        self._repo._requester.requestJsonAndCheck("DELETE", self._repo.url + "/contents/" + path, input=parameters)

    def _commit(self, filename, content, message, branch, remove_trailing_whitespaces=True):
        """
        """
        head_ref = self._repo.get_git_ref("heads/%s" % branch)
        latest_commit = self._repo.get_git_commit(head_ref.object.sha)
        base_tree = latest_commit.tree

        if remove_trailing_whitespaces:
            content = '\n'.join([line.rstrip() for line in content.split('\n')])

        new_tree = self._repo.create_git_tree(
            [InputGitTreeElement(
                path="%s" % os.path.join(self._repository_path, filename),
                mode="100644",
                type="blob",
                content=content
            )],
            base_tree)

        new_commit = self._repo.create_git_commit(
            message=message,
            parents=[latest_commit],
            tree=new_tree)

        head_ref.edit(sha=new_commit.sha, force=False)
