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

from builtins import object
import importlib

from monolithe.lib.sdkutils import SDKUtils
from bambou import NURESTModelController


class SDKLoader(object):
    """
    """
    def __init__(self, version, sdk_identifier):
        """
        """
        self._sdk_identifier = sdk_identifier
        self._version = SDKUtils.get_string_version(version)
        self._sdk_module = importlib.import_module("%s.%s" % (self._sdk_identifier, self._version))
        self._sdk_utils_module = importlib.import_module("%s.utils" % self._sdk_identifier)

    @property
    def sdk(self):
        return self._sdk_module

    @property
    def sdk_utils(self):
        return self._sdk_utils_module

    @property
    def version(self):
        return self._version

    @property
    def sdk_identifier(self):
        return self._sdk_identifier

    def class_from_rest_name(self, rest_name):
        """
        """
        return NURESTModelController.get_first_model_with_rest_name(rest_name=rest_name)

    def get_instance_from_rest_name(self, rest_name):
        """
        """
        klass = self.class_from_rest_name(rest_name)

        if klass:
            return klass()

        return None
