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

from monolithe.generators.lib import TemplateFileWriter

from ..python.writers.sdkwriter import _PythonSDKFileWriter
from ..ruby.writers.sdkwriter import _RubySDKFileWriter
from ..go.writers.sdkwriter import _GoSDKFileWriter


class SDKWriter(object):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None

        self.monolithe_config = monolithe_config

    def write(self, apiversions):
        """
        """
        self.writer = self._get_writer()

        if not hasattr(self.writer, "write_sdk"):
            return

        self.writer.write_sdk(apiversions=apiversions)

    def _get_writer(self):
        """ Get the appropriate writer
        """
        language = self.monolithe_config.language
        klass = None

        if language == 'ruby':
            klass = _RubySDKFileWriter

        elif language == 'python':
            klass = _PythonSDKFileWriter

        elif language == 'go':
            klass = _GoSDKFileWriter

        if klass is None:
            raise Exception('Unsupported language %s. Please create the appropriate class in sdkwriter.py' % language)

        return klass(monolithe_config=self.monolithe_config)
