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
from builtins import str
from collections import OrderedDict

from monolithe.lib import SDKUtils, TaskManager
from monolithe.generators.lib import TemplateFileWriter


class DocumentationWriter(TemplateFileWriter):

    def __init__(self, monolithe_config, api_info):
        super(DocumentationWriter, self).__init__(package="monolithe.generators.lang.python")
        self.api_version = api_info["version"]
        self.api_root = api_info["root"]
        self.api_prefix = api_info["prefix"]

        self.monolithe_config = monolithe_config
        self._output = self.monolithe_config.get_option("output", "transformer")
        self._transformation_name = self.monolithe_config.get_option("name", "transformer")
        self._class_prefix = self.monolithe_config.get_option("class_prefix", "transformer")
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._product_name = self.monolithe_config.get_option("product_name")

        self.output_directory = "%s/python/doc/%s" % (self._output, SDKUtils.get_string_version(self.api_version))

    def perform(self, specifications):
        self.model_filenames = dict()
        self.fetcher_filenames = dict()
        task_manager = TaskManager()
        for rest_name, specification in specifications.items():
            task_manager.start_task(
                method=self._write_model,
                specification=specification,
                specification_set=specifications)
        task_manager.wait_until_exit()
        # self._write_index(filenames=self.model_filenames)

    # def _write_index(self, filenames):
    #     self.write(destination=self.output_directory,
    #                filename="index.rst",
    #                template_name="index.rst.tpl",
    #                filenames=self._prepare_filenames(filenames),
    #                class_prefix=self._class_prefix,
    #                product_accronym=self._product_accronym)

    def _write_model(self, specification, specification_set):
        filename = "%s%s.rst" % (self._class_prefix.lower(), specification.entity_name.lower())
        parent_apis = []
        for rest_name, remote_spec in specification_set.items():
            for related_child_api in remote_spec.child_apis:
                if related_child_api.rest_name == specification.rest_name:
                    parent_apis.append(remote_spec)
        self.write(destination=self.output_directory,
                   filename=filename,
                   template_name="model.rst.tpl",
                   specification=specification,
                   specification_set=specification_set,
                   parent_apis=parent_apis,
                   class_prefix=self._class_prefix)
        self.model_filenames[filename] = specification.entity_name

    def _prepare_filenames(self, filenames, suffix=''):
        formatted_filenames = {}
        for filename, classname in filenames.items():
            formatted_filenames[filename[:-4]] = str("%s%s%s" % (self._class_prefix, classname, suffix))
        return OrderedDict(sorted(formatted_filenames.items()))
