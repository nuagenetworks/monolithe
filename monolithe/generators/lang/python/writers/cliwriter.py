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
from monolithe.generators.lib import TemplateFileWriter


class CLIWriter(TemplateFileWriter):
    """ Implements `write_cli` that writes CLI python files
    """

    def __init__(self, monolithe_config):
        """
        """
        super(CLIWriter, self).__init__(package="monolithe.generators.lang.python")

        self.monolithe_config = monolithe_config
        self._output = self.monolithe_config.get_option("output", "transformer")
        self._transformation_name = self.monolithe_config.get_option("name", "transformer")
        self._cli_name = self.monolithe_config.get_option("cli_name", "transformer")
        self._class_prefix = self.monolithe_config.get_option("class_prefix", "transformer")
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._product_name = self.monolithe_config.get_option("product_name")
        self.output_directory = "%s/python/%s/cli" % (self._output, self._transformation_name)

        with open("%s/python/__code_header" % self._output, "r") as f:
            self.header_content = f.read()

    def perform(self):
        """
        """
        self._write_init()
        self._write_cli()
        self._write_commands()
        self._write_printer()
        self._write_utils()

    def _write_init(self):
        """
        """
        self.write(destination=self.output_directory, filename="__init__.py", template_name="cli__init__.py.tpl",
                   header=self.header_content)

    def _write_cli(self):
        """
        """
        self.write(destination=self.output_directory, filename="cli.py", template_name="cli.py.tpl",
                   product_accronym=self._product_accronym,
                   product_name=self._product_name,
                   header=self.header_content)

    def _write_commands(self):
        """
        """
        self.write(destination=self.output_directory, filename="commands.py", template_name="cli_commands.py.tpl",
                   product_accronym=self._product_accronym,
                   product_name=self._product_name,
                   cli_name=self._cli_name,
                   header=self.header_content)

    def _write_printer(self):
        """
        """
        self.write(destination=self.output_directory, filename="printer.py", template_name="cli_printer.py.tpl",
                   header=self.header_content)

    def _write_utils(self):
        """
        """
        self.write(destination=self.output_directory, filename="utils.py", template_name="cli_utils.py.tpl",
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   name=self._transformation_name,
                   header=self.header_content)
