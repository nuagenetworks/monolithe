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

from monolithe.lib import SDKUtils
from monolithe.generators.lib import TemplateFileWriter


class GeneralWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        super(GeneralWriter, self).__init__(package="monolithe.generators.sdk.lang.python")

        self.monolithe_config = monolithe_config
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._sdk_version = self.monolithe_config.get_option("sdk_version", "sdk")
        self._sdk_revision_number = self.monolithe_config.get_option("sdk_revision_number", "sdk")
        self._sdk_url = self.monolithe_config.get_option("sdk_url", "sdk")
        self._sdk_author = self.monolithe_config.get_option("sdk_author", "sdk")
        self._sdk_email = self.monolithe_config.get_option("sdk_email", "sdk")
        self._sdk_description = self.monolithe_config.get_option("sdk_description", "sdk")
        self._sdk_license_name = self.monolithe_config.get_option("sdk_license_name", "sdk")
        self._sdk_cli_name = self.monolithe_config.get_option("sdk_cli_name", "sdk")
        self._sdk_bambou_version = self.monolithe_config.get_option("sdk_bambou_version", "sdk")
        self._copyright = self.monolithe_config.get_option("copyright")
        self.output_directory = "%s/python" % self.monolithe_config.get_option("sdk_output", "sdk")

        with open("%s/__code_header" % self.output_directory, "r") as f:
            self.header_content = f.read()

    def perform(self, apiversions):
        """
        """
        self._write_setup()
        self._write_root_init()
        self._write_utils()
        self._write_manifest(apiversions)
        self._write_requirements()

    def _write_setup(self):
        """
        """
        self.write(destination=self.output_directory, filename="setup.py", template_name="setup.py.tpl",
                   sdk_name=self._sdk_name,
                   sdk_version=self._sdk_version,
                   sdk_revision_number=self._sdk_revision_number,
                   sdk_url=self._sdk_url,
                   sdk_author=self._sdk_author,
                   sdk_email=self._sdk_email,
                   sdk_description=self._sdk_description,
                   sdk_license_name=self._sdk_license_name,
                   sdk_cli_name=self._sdk_cli_name,
                   copyright=self._copyright,
                   header=self.header_content)

    def _write_manifest(self, apiversions):
        """
        """
        self.write(destination=self.output_directory, filename="MANIFEST.in", template_name="MANIFEST.in.tpl",
                   sdk_name=self._sdk_name,
                   apiversions=[SDKUtils.get_string_version(version) for version in apiversions])

    def _write_requirements(self):
        """
        """
        self.write(destination=self.output_directory, filename="requirements.txt", template_name="requirements.txt.tpl",
                   sdk_bambou_version=self._sdk_bambou_version)

    def _write_root_init(self):
        """
        """
        destination = "%s/%s" % (self.output_directory, self._sdk_name)
        self.write(destination=destination, filename="__init__.py", template_name="__init__.py.tpl",
                   header=self.header_content)

    def _write_utils(self):
        """
        """
        destination = "%s/%s" % (self.output_directory, self._sdk_name)
        self.write(destination=destination, filename="utils.py", template_name="utils.py.tpl",
                   sdk_name=self._sdk_name,
                   header=self.header_content)
