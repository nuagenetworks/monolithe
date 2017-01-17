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
from monolithe.lib import SDKUtils
from monolithe.generators.lib import TemplateFileWriter


class PackageWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        super(PackageWriter, self).__init__(package="monolithe.generators.lang.python")

        self.monolithe_config = monolithe_config
        self._transformation_name = self.monolithe_config.get_option("name", "transformer")
        self._transformation_version = self.monolithe_config.get_option("version", "transformer")
        self._revision_number = self.monolithe_config.get_option("revision_number", "transformer")
        self._url = self.monolithe_config.get_option("url", "transformer")
        self._author = self.monolithe_config.get_option("author", "transformer")
        self._email = self.monolithe_config.get_option("email", "transformer")
        self._description = self.monolithe_config.get_option("description", "transformer")
        self._license = self.monolithe_config.get_option("license_name", "transformer")
        self._cli_name = self.monolithe_config.get_option("cli_name", "transformer")
        self._copyright = self.monolithe_config.get_option("copyright")
        self.output_directory = "%s/python" % self.monolithe_config.get_option("output", "transformer")

        with open("%s/__code_header" % self.output_directory, "r") as f:
            self.header_content = f.read()

    def perform(self, apiversions):
        """
        """
        self._write_setup()
        self._write_root_init()
        self._write_utils()
        self._write_manifest(apiversions)
        self._write_documentation(apiversions)

    def _write_setup(self):
        """
        """
        self.write(destination=self.output_directory, filename="setup.py", template_name="setup.py.tpl",
                   name=self._transformation_name,
                   version=self._transformation_version,
                   revision_number=self._revision_number,
                   url=self._url,
                   author=self._author,
                   email=self._email,
                   description=self._description,
                   license_name=self._license,
                   cli_name=self._cli_name,
                   copyright=self._copyright,
                   header=self.header_content)

    def _write_documentation(self, apiversions):
        destination = "%s/doc" % self.output_directory
        self.write(
            destination=destination,
            filename="index.rst",
            template_name="index.rst.tpl",
            apiversions=[SDKUtils.get_string_version(version) for version in apiversions]
        )


    def _write_manifest(self, apiversions):
        """
        """
        self.write(destination=self.output_directory, filename="MANIFEST.in", template_name="MANIFEST.in.tpl",
                   name=self._transformation_name,
                   apiversions=[SDKUtils.get_string_version(version) for version in apiversions])

    def _write_root_init(self):
        """
        """
        destination = "%s/%s" % (self.output_directory, self._transformation_name)
        self.write(destination=destination, filename="__init__.py", template_name="__init__.py.tpl",
                   header=self.header_content)

    def _write_utils(self):
        """
        """
        destination = "%s/%s" % (self.output_directory, self._transformation_name)
        self.write(destination=destination, filename="utils.py", template_name="utils.py.tpl",
                   name=self._transformation_name,
                   header=self.header_content)
