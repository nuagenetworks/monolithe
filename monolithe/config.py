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
from builtins import object

from configparser import ConfigParser
import os
import io


class MonolitheConfig(object):

    def __init__(self, path=None):
        self.path = path
        self.config = None
        self.mapping = None
        self.language = 'python'

        if self.path:
            if not os.path.exists(path):
                raise Exception("Could not find path %s" % path)
            config = ConfigParser()
            config.read(path)
            self.set_config(config)

    def copy(self):
        # duplicate the config parser
        conf_data = io.StringIO()
        self.config.write(conf_data)
        conf_data.seek(0)
        new_config_parser = ConfigParser()
        new_config_parser.readfp(conf_data)

        # create a new MonolitheConfig and give it the duplicate config parser
        monolithe_config_copy = MonolitheConfig(path=self.path)
        monolithe_config_copy.set_config(new_config_parser)

        return monolithe_config_copy

    def set_config(self, config):
        self.config = config

        # vanilla
        self.user_vanilla = self.get_option("user_vanilla", "transformer")

        # mapping
        if not self.path:
            return

        mapping_path = "%s/mapping.ini" % os.path.dirname(self.path)

        if not os.path.exists(self.path):
            return

        self.mapping = ConfigParser()
        self.mapping.read(mapping_path)

    def get_option(self, option, section="monolithe", **kwargs):
        return self.config.get(section, option, **kwargs)

    def set_option(self, option, value, section="monolithe"):
        return self.config.set(section, option, value)

    def map_attribute(self, rest_name, attribute_name):
        if self.mapping is None \
                or not self.mapping.has_section(rest_name) \
                or not self.mapping.has_option(rest_name, attribute_name):
            return attribute_name

        return self.mapping.get(rest_name, attribute_name)
