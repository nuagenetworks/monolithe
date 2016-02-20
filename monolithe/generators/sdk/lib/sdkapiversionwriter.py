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


from monolithe.lib import TaskManager

from ..python.writers.sdkapiversionwriter import _PythonSDKAPIVersionFileWriter
from ..ruby.writers.sdkapiversionwriter import _RubySDKAPIVersionFileWriter
from ..go.writers.sdkapiversionwriter import _GoSDKAPIVersionFileWriter


class SDKAPIVersionWriter(object):
    """ Writer of the Python SDK SDK

    """

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None

        self.monolithe_config = monolithe_config

    def write(self, specifications, api_info):
        """ Write all files according to data

            Args:
                specifications: A dict of all specifications to manage
                api_info: the version of the api

            Returns:
                Writes specifications and fetchers files

        """
        model_filenames = dict()
        fetcher_filenames = dict()

        self.api_info = api_info

        self.writer = self._get_writer()

        task_manager = TaskManager()

        for rest_name, specification in specifications.iteritems():
            task_manager.start_task(method=self._write_models, specification=specification, filenames=model_filenames, specification_set=specifications)
            task_manager.start_task(method=self._write_fetcher_file, specification=specification, filenames=fetcher_filenames, specification_set=specifications)

        task_manager.wait_until_exit()

        self.writer.write_sdkapiversion(model_filenames=model_filenames, fetcher_filenames=fetcher_filenames)
        self.postprocess()

    def postprocess(self):
        """
        Allows the sub writer to do some post generation operations
        """
        if not hasattr(self.writer, "postprocess"):
            return

        self.writer.postprocess()

    def _get_writer(self):
        """ Get the appropriate writer
        """
        language = self.monolithe_config.language
        klass = None

        if language == 'ruby':
            klass = _RubySDKAPIVersionFileWriter

        elif language == 'python':
            klass = _PythonSDKAPIVersionFileWriter

        elif language == 'go':
            klass = _GoSDKAPIVersionFileWriter

        if klass is None:
            raise Exception('Unsupported language %s. Please create the appropriate class in sdkapiversionwriter.py' % language)

        return klass(monolithe_config=self.monolithe_config, api_info=self.api_info)

    def _write_models(self, specification, filenames, specification_set):
        """
        """

        if not hasattr(self.writer, "write_model"):
            return

        (filename, classname) = self.writer.write_model(specification=specification, specification_set=specification_set)
        filenames[filename] = classname

    def _write_fetcher_file(self, specification, filenames, specification_set):
        """ Write the fetcher file for the specification

            Args:
                specification: the specification to write
                filenames: list of generates filenames

        """
        if not hasattr(self.writer, "write_fetcher"):
            return

        if specification.rest_name != self.api_info["root"]:
            (filename, classname) = self.writer.write_fetcher(specification=specification, specification_set=specification_set)
            filenames[filename] = classname
