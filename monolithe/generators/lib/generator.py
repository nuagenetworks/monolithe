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
from builtins import object

import os
import shutil

from monolithe.lib import Printer
from monolithe.specifications import SpecificationAPI


class Generator(object):

    def __init__(self, directory_manager, branches):
        self.directory_manager = directory_manager
        self.branches = branches

    @property
    def config(self):
        return self.directory_manager.monolithe_config

    def run(self, branches=None):
        specification_info = []

        if branches:
            for branch in branches:
                Printer.log("Switching to branch %s" % branch)
                self.directory_manager.switch_branch(branch)
                specification_info.append(self.get_specifications_infos_from_folder())
        else:
            specification_info.append(self.get_specifications_infos_from_folder())

        self.generate(specification_info=specification_info)

    def get_specifications_infos_from_folder(self):
        Printer.log("retrieving specifications from folder \"%s\"" % (self.directory_manager.folder))
        api_info = self.directory_manager.get_api_info()
        specifications = self.directory_manager.get_all_specifications()
        self._resolve_parent_apis(specifications)
        Printer.log("%d specifications retrieved from folder \"%s\" (api version: %s)" % (len(specifications), self.directory_manager.folder, api_info["version"]))
        return {"specifications": specifications, "api": api_info}

    def generate(self, specification_info):
        raise NotImplementedError()

    def install_user_vanilla(self, user_vanilla_path, output_path, multi_lang=True):
        """
        """
        if not user_vanilla_path or not len(user_vanilla_path):
            return

        if multi_lang:
            user_vanilla_path = os.path.join(user_vanilla_path, self.config.language)
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
