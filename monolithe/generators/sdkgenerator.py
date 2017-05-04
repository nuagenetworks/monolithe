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

import os
import shutil

from monolithe.lib import Printer
from monolithe.generators.lib import Generator
from monolithe.generators.managers import MainManager, CLIManager, VanillaManager
from .sdkapiversiongenerator import SDKAPIVersionGenerator


class SDKGenerator(Generator):

    def cleanup(self):
        output = self.config.get_option("output", "transformer")
        language = self.config.language

        overrides_path = "%s/%s/__overrides" % (output, language)
        if os.path.exists(overrides_path):
            shutil.rmtree(overrides_path)

        attrs_defaults_path = "%s/%s/__attributes_defaults" % (output, language)
        if os.path.exists(attrs_defaults_path):
            shutil.rmtree(attrs_defaults_path)

        code_header_path = "%s/%s/__code_header" % (output, language)
        if os.path.exists(code_header_path):
            os.remove(code_header_path)

    def generate(self, specification_info):
        user_vanilla = self.config.get_option("user_vanilla", "transformer")
        output = self.config.get_option("output", "transformer")
        name = self.config.get_option("name", "transformer")
        lang = self.config.language

        if not os.path.exists(os.path.join(output, lang)):
            os.makedirs(os.path.join(output, lang))

        vanilla_manager = VanillaManager(monolithe_config=self.config)
        vanilla_manager.execute(output_path="%s/%s" % (output, lang))

        self.install_user_vanilla(user_vanilla_path=user_vanilla, output_path="%s/%s" % (output, lang))

        version_generator = SDKAPIVersionGenerator(self.config)
        apiversions = []

        for info in specification_info:
            Printer.log("transforming specifications into %s for version %s..." % (lang, info["api"]["version"]))
            apiversions.append(info["api"]["version"])

        version_generator.generate(specification_info=specification_info)

        Printer.log("assembling...")
        manager = MainManager(monolithe_config=self.config)
        manager.execute(apiversions=apiversions)

        cli_manager = CLIManager(monolithe_config=self.config)
        cli_manager.execute()

        self.cleanup()
        Printer.success("%s generation complete and available in \"%s/%s\"" % (name, output, self.config.language))
