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

import os
from configparser import RawConfigParser

from monolithe.lib import SDKUtils, TaskManager
from monolithe.generators.lib import TemplateFileWriter


class APIVersionWriter(TemplateFileWriter):
    """ Provide useful method to write Java files.

    """
    def __init__(self, monolithe_config, api_info):
        """ Initializes a _JavaSDKAPIVersionFileWriter

        """
        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.java")

        self.api_version = api_info["version"]
        self._api_version_string = SDKUtils.get_string_version(self.api_version)
        self.api_root = api_info["root"]
        self.api_prefix = api_info["prefix"]

        self.monolithe_config = monolithe_config
        self._output = self.monolithe_config.get_option("output", "transformer")
        self._name = self.monolithe_config.get_option("name", "transformer")
        self._class_prefix = "" # self.monolithe_config.get_option("class_prefix", "transformer")
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._product_name = self.monolithe_config.get_option("product_name")

        self.output_directory = "%s/java/%s/%s" % (self._output, self._name, self._api_version_string)
        self.override_folder = os.path.normpath("%s/../../__overrides" % self.output_directory)
        self.fetchers_path = "/fetchers/"
        self.enums_path = "/enums"
        
        with open("%s/java/__code_header" % self._output, "r") as f:
            self.header_content = f.read()

    def perform(self, specifications):
        """
        """
        self._write_info()
        self._write_session()

        task_manager = TaskManager()
        for rest_name, specification in specifications.items():
            task_manager.start_task(method=self._write_model, specification=specification, specification_set=specifications)
            task_manager.start_task(method=self._write_fetcher, specification=specification, specification_set=specifications)
        task_manager.wait_until_exit()

    def _write_session(self):
        """ Write SDK session file

            Args:
                version (str): the version of the server

        """
        base_name = "%sSession" % self._product_accronym
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=self.output_directory, filename=filename, template_name="session.java.tpl",
                    version=self.api_version,
                    product_accronym=self._product_accronym,
                    class_prefix=self._class_prefix,
                    root_api=self.api_root,
                    name=self._name,
                    api_prefix=self.api_prefix,
                    override_content=override_content,
                    header=self.header_content,
                    version_string=self._api_version_string)

    def _write_info(self):
        """ Write API Info file
        """
        self.write(destination=self.output_directory, filename="SdkInfo.java", template_name="sdkinfo.java.tpl",
                    version=self.api_version,
                    product_accronym=self._product_accronym,
                    class_prefix=self._class_prefix,
                    root_api=self.api_root,
                    api_prefix=self.api_prefix,
                    product_name=self._product_name,
                    name=self._name,
                    header=self.header_content,
                    version_string=self._api_version_string)

    def _write_model(self, specification, specification_set):
	""" Write autogenerate specification file

	"""
	filename = "%s%s.java" % (self._class_prefix, specification.entity_name)

	override_content = self._extract_override_content(specification.entity_name)
	superclass_name = "RestRootObject" if specification.rest_name == self.api_root else "RestObject"

	self.write(destination=self.output_directory, filename=filename, template_name="model.java.tpl",
		    specification=specification,
		    specification_set=specification_set,
		    version=self.api_version,
		    name=self._name,
		    class_prefix=self._class_prefix,
		    product_accronym=self._product_accronym,
		    override_content=override_content,
		    superclass_name=superclass_name,
		    header=self.header_content,
		    version_string=self._api_version_string)

	return (filename, specification.entity_name)

    def _write_fetcher(self, specification, specification_set):
        """ Write fetcher

        """
        destination = "%s%s" % (self.output_directory, self.fetchers_path)
        base_name = "%sFetcher" % specification.entity_name_plural
        filename = "%s%s.java" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=destination, filename=filename, template_name="fetcher.java.tpl",
                    specification=specification,
                    specification_set=specification_set,
                    class_prefix=self._class_prefix,
                    product_accronym=self._product_accronym,
                    override_content=override_content,
                    header=self.header_content,
                    name=self._name,
                    version_string=self._api_version_string)

        return (filename, specification.entity_name_plural)

    def postprocess(self):
        """ Perform some linting operations

        """

    def _extract_override_content(self, name):
        """
        """
        # find override file
        specific_override_path = "%s/%s_%s%s.override.java" % (self.override_folder, self.api_version, self._class_prefix, name.title())
        generic_override_path = "%s/%s%s.override.java" % (self.override_folder, self._class_prefix, name.title())
        final_path = specific_override_path if os.path.exists(specific_override_path) else generic_override_path

        # Read override from file
        override_content = None
        if os.path.isfile(final_path):
            override_content = open(final_path).read()
        
        return override_content
