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

from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import object

import json
import os
import configparser
import git

from .specification import Specification
from monolithe.lib import apply_extension
from monolithe import MonolitheConfig


class FolderManager (object):

    def __init__(self, folder, config_path=None):
        self.folder = folder
        self.monolithe_config = self.get_monolithe_config(config_path)

    def get_available_specifications(self):
        ret = []
        for filename in os.listdir(self.folder):
            if os.path.splitext(filename)[1] != ".spec" or filename.startswith("@"):
                continue
            ret.append(filename)
        return ret

    def get_api_info(self):
        with open("%s/api.info" % self.folder, "r") as f:
            try:
                return json.loads(f.read())
            except Exception as e:
                raise Exception("could not parse api.info", e)

    def get_monolithe_config(self, config_path):
        if config_path is None:
            config_path = "%s/monolithe.ini" % self.folder
        return MonolitheConfig(config_path)

    def get_all_specifications(self):
        specifications = {}
        for name in self.get_available_specifications():
            specifications[name.replace(".spec", "")] = self.get_specification(name)
        return specifications

    def get_specification_data(self, name):
        data = {}
        with open("%s/%s" % (self.folder, name), "r") as f:
            try:
                data = json.loads(f.read())
                if "model" in data and "extends" in data["model"]:
                    for extension in data["model"]["extends"]:
                        apply_extension(self.get_specification_data(name="%s.spec" % extension), data)
            except Exception as e:
                raise Exception("Could not parse %s" % name, e)
        return data

    def get_specification(self, name):
        return Specification(filename=name, data=self.get_specification_data(name), monolithe_config=self.monolithe_config)

    def get_specifications(self, names, callback=None):
        specifications = []
        for name in names:
            specifications.append(Specification(filename=name, data=self.get_specification_data(name=name)))
        return specifications


class RepositoryManager(FolderManager):

    def __init__(self, folder, config_path=None):
        try:
            self.repo = git.repo.Repo(folder)
        except git.InvalidGitRepositoryError:
            raise Exception(
                "%s is not a git repository. Cannot handle branches" % folder)
        super(RepositoryManager, self).__init__(folder, config_path=config_path)

    def switch_branch(self, name):
        for branch in self.repo.branches:
            if branch.name == name:
                branch.checkout()
                return
        # At this point, no branch was found. We assume the ref is actually a
        # tag or a commit. This is an undocumented feature, we expect users to
        # use actual branches.
        try:
            self.repo.head.reference = self.repo.commit(name)
            self.repo.head.reset(index=True, working_tree=True)
        except:
            raise Exception('No branch or reference %s found' % name)
