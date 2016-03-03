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

from builtins import object

import os
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import Printer
from monolithe.specifications import RepositoryManager, FolderManager, SpecificationAPI


class Generator(object):

    def __init__(self, monolithe_config):
        """
        """
        self.monolithe_config = monolithe_config

    def initialize_folder_manager(self, folder):
        """
        """
        self.folder_manager = FolderManager(folder=folder, monolithe_config=self.monolithe_config)

    def retrieve_monolithe_config_from_folder(self, language="python"):
        """
        """
        parser = self.folder_manager.get_monolithe_config()
        self.monolithe_config = MonolitheConfig()
        self.monolithe_config.set_config(parser)
        self.monolithe_config.language = language
        self.folder_manager.monolithe_config = self.monolithe_config
        return self.monolithe_config

    def generate_from_folder(self):
        """
        """
        specification_info = []

        Printer.log("retrieving specifications from folder \"%s\"" % (self.folder_manager.folder))
        api_info = self.folder_manager.get_api_info()
        specifications = self.folder_manager.get_all_specifications()
        self._resolve_parent_apis(specifications)
        specification_info.append({"specifications": specifications, "api": api_info})
        Printer.log("%d specifications retrieved from folder \"%s\" (api version: %s)" % (len(specifications), self.folder_manager.folder, api_info["version"]))

        self.generate(specification_info=specification_info)

    def initialize_repository_manager(self, api_url, login_or_token, password, organization, repository, repository_path):
        """
        """
        self.repository_manager = RepositoryManager(monolithe_config=self.monolithe_config,
                                                    api_url=api_url,
                                                    login_or_token=login_or_token,
                                                    password=password,
                                                    organization=organization,
                                                    repository=repository,
                                                    repository_path=repository_path)

    def retrieve_monolithe_config_from_repo(self, branch, language):
        """
        """
        parser = self.repository_manager.get_monolithe_config(branch=branch)
        self.monolithe_config = MonolitheConfig()
        self.monolithe_config.set_config(parser)
        self.monolithe_config.language = language
        self.repository_manager.monolithe_config = self.monolithe_config
        return self.monolithe_config

    def generate_from_repo(self, branches):
        """
        """
        specification_info = []

        for branch in branches:
            Printer.log("retrieving specifications from github \"%s/%s%s@%s\"" % (self.repository_manager.organization.lower(), self.repository_manager.repository.lower(), self.repository_manager.repository_path, branch))
            api_info = self.repository_manager.get_api_info(branch=branch)
            specifications = self.repository_manager.get_all_specifications(branch=branch)
            self._resolve_parent_apis(specifications)
            specification_info.append({"specifications": specifications, "api": api_info})
            Printer.log("%d specifications retrieved from branch \"%s\" (api version: %s)" % (len(specifications), branch, api_info["version"]))

        self.generate(specification_info=specification_info)

    def generate(self, specification_info):
        """
        """
        pass

    def install_user_vanilla(self, user_vanilla_path, output_path, multi_lang=True):
        """
        """
        if not user_vanilla_path or not len(user_vanilla_path):
            return

        if multi_lang:
            user_vanilla_path = os.path.join(user_vanilla_path, self.monolithe_config.language)
        else:
            user_vanilla_path = os.path.join(user_vanilla_path)

        if not os.path.exists(user_vanilla_path):
            Printer.warn("Could not find user vanilla folder at path %s. Ignoring" % user_vanilla_path)
            return

        for item in os.listdir(user_vanilla_path):
            s = os.path.join(user_vanilla_path, item)
            d = os.path.join(output_path, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)

    def generate_documentation(self):
        """
        """
        pass

    # Utilities
    def _resolve_parent_apis(self, specifications):
        """
        """

        # certainly not the best algo ever... but I need to get somthing done :)
        for specification_rest_name, specification in specifications.items():

            for rest_name, remote_spec in specifications.items():

                for related_child_api in remote_spec.child_apis:

                    if related_child_api.rest_name == specification.rest_name:

                        parent_api = SpecificationAPI(specification=specification)
                        parent_api.rest_name = related_child_api.rest_name
                        if specification.allows_get:
                            parent_api.allows_get = True
                        if specification.allows_create:
                            parent_api.allows_create = True
                        if specification.allows_update:
                            parent_api.allows_update = True
                        if specification.allows_delete:
                            parent_api.allows_Delete = True

                        specification.parent_apis.append(parent_api)
