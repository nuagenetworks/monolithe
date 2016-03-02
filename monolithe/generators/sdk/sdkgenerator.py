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

import os
import shutil

from monolithe.lib import Printer
from monolithe.generators.lib import Generator
from .lib import SDKWriter, CLIWriter
from .sdkapiversiongenerator import SDKAPIVersionGenerator


class SDKGenerator(Generator):
    """
    """

    def cleanup(self):
        """
        """
        sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        language = self.monolithe_config.language

        overrides_path = "%s/%s/__overrides" % (sdk_output, language)
        if os.path.exists(overrides_path):
            shutil.rmtree(overrides_path)

        attrs_defaults_path = "%s/%s/__attributes_defaults" % (sdk_output, language)
        if os.path.exists(attrs_defaults_path):
            shutil.rmtree(attrs_defaults_path)

        code_header_path = "%s/%s/__code_header" % (sdk_output, language)
        if os.path.exists(code_header_path):
            os.remove(code_header_path)

    def generate(self, specification_info):
        """
        """
        sdk_user_vanilla = self.monolithe_config.get_option("sdk_user_vanilla", "sdk")
        sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")

        self.install_system_vanilla(current_file=__file__, output_path="%s/%s" % (sdk_output, self.monolithe_config.language))
        self.install_user_vanilla(user_vanilla_path=sdk_user_vanilla, output_path="%s/%s" % (sdk_output, self.monolithe_config.language))

        generator = SDKAPIVersionGenerator(monolithe_config=self.monolithe_config)
        apiversions = []

        for info in specification_info:
            apiversions.append(info["api"]["version"])

        generator.generate(specification_info=specification_info)

        Printer.log("assembling all packages...")
        sdk_writer = SDKWriter(monolithe_config=self.monolithe_config)
        sdk_writer.write(apiversions=apiversions)

        cli_writer = CLIWriter(monolithe_config=self.monolithe_config)
        cli_writer.perform()

        self.cleanup()
        Printer.success("%s generation complete and available in \"%s/%s\"" % (sdk_name, sdk_output, self.monolithe_config.language))

    def generate_documentation(self):
        """
        """
        sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")
        sdk_doc_output = self.monolithe_config.get_option("sdk_doc_output", "sdk")

        input_path = os.path.join(sdk_output, self.monolithe_config.language, sdk_name)
        output_path = os.path.join(sdk_doc_output, self.monolithe_config.language)

        if self.monolithe_config.language == 'python':
            Printer.log("generating documentation...")
            os.system("pdoc --overwrite --html --html-dir '%s' '%s' >/dev/null 2>&1" % (output_path, input_path))
            Printer.success("%s documentation generation complete and available in \"%s\"" % (sdk_name, output_path))
        else:
            Printer.warn("no documentation generator for this language. ignoring")
