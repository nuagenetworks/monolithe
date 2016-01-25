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
from monolithe.specifications import RepositoryManager, FolderManager
from monolithe.generators.lib import Generator
from .lib import APIDocWriter


class APIDocumentationGenerator(Generator):
    """ Generate SDK API Documentation

    """

    def generate(self, specification_info):
        """ Start generation ofthe API Documentation
        """
        apidoc_output = self.monolithe_config.get_option("apidoc_output", "apidoc")
        apidoc_user_vanilla = self.monolithe_config.get_option("apidoc_user_vanilla", "apidoc")
        sdk_name = self.monolithe_config.get_option("product_name")
        product_name = self.monolithe_config.get_option("product_name")

        writer = APIDocWriter(self.monolithe_config)
        apiversions = []

        for info in specification_info:

            vanilla_output_path = "%s/%s/%s" % (apidoc_output, sdk_name, info["api"]["version"])

            self.install_system_vanilla(current_file=__file__, output_path=vanilla_output_path, multiple_languages=False)
            self.install_user_vanilla(user_vanilla_path=apidoc_user_vanilla, output_path=vanilla_output_path)

            Printer.log("generating %s api documentation for api version: %s" % (product_name, info["api"]["version"]))
            writer.write(specifications=info["specifications"], api_info=info["api"])

        Printer.success("%s api documentation generation complete and available at \"%s\"" % (product_name, apidoc_output))
