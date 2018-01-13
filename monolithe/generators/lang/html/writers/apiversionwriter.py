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

from monolithe.generators.lib import TemplateFileWriter
from monolithe.lib import SDKUtils, TaskManager


class APIVersionWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config, api_info):
        """
        """
        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.html")

        self.monolithe_config = monolithe_config

        self._api_version = api_info["version"]
        self._output = self.monolithe_config.get_option("output", "transformer")
        self._product_name = self.monolithe_config.get_option("product_name")

        self.output_directory = "%s/html/%s" % (self._output, SDKUtils.get_string_version(self._api_version))

    def _get_actions(self, obj):
        """
        """
        actions = []
        if obj.allows_get:
            actions.append("GET")

        if obj.allows_create:
            actions.append("POST")

        if obj.allows_update:
            actions.append("PUT")

        if obj.allows_delete:
            actions.append("DELETE")
        return actions

    def perform(self, specifications):
        """
        """

        task_manager = TaskManager()
        for rest_name, specification in specifications.items():
            task_manager.start_task(method=self._write_specification, specification=specification, specification_set=specifications)
        task_manager.wait_until_exit()

        self._write_index(specifications)

    def _write_specification(self, specification, specification_set):
        """
        """
        filename = "%s.html" % specification.rest_name.lower()

        # remove this when template can use the things resolved by _resolve_parent_apis
        parent_apis = []
        for rest_name, remote_spec in specification_set.items():
            for related_child_api in remote_spec.child_apis:
                if related_child_api.rest_name == specification.rest_name:
                    parent_apis.append({"remote_spec": remote_spec, "actions": self._get_actions(related_child_api), "relationship": related_child_api.relationship})

        child_apis = []
        member_apis = []
        for child_api in specification.child_apis:
            if child_api.relationship == "member":
                member_apis.append({"remote_spec": specification_set[child_api.rest_name], "actions": self._get_actions(child_api), "relationship": child_api.relationship})
            else:
                child_apis.append({"remote_spec": specification_set[child_api.rest_name], "actions": self._get_actions(child_api), "relationship": child_api.relationship})

        self_apis = [{"actions": self._get_actions(specification)}]

        self.write(destination=self.output_directory, filename=filename, template_name="object.html.tpl",
                   apiversion=self._api_version,
                   specification=specification,
                   parent_apis=parent_apis,
                   child_apis=child_apis,
                   member_apis=member_apis,
                   self_apis=self_apis,
                   product_name=self._product_name)

        return (filename, specification.entity_name)

    def _write_index(self, specifications):
        """
        """
        self.write(destination=self.output_directory, filename="index.html", template_name="index.html.tpl",
                   apiversion=self._api_version,
                   specifications=list(specifications.values()),
                   product_name=self._product_name)
