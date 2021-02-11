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
from builtins import str
import os
import shutil
from collections import OrderedDict

from monolithe.lib import SDKUtils, TaskManager
from monolithe.generators.lib import TemplateFileWriter


class APIVersionWriter(TemplateFileWriter):
    """ Provide usefull method to write Python files.

    """
    def __init__(self, monolithe_config, api_info):
        """ Initializes a _PythonSDKAPIVersionFileWriter

        """
        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.python")

        self.api_version = api_info["version"]
        self.api_root = api_info["root"]
        self.api_prefix = api_info["prefix"]

        self.monolithe_config = monolithe_config
        self._output = self.monolithe_config.get_option("output", "transformer")
        self._transformation_name = self.monolithe_config.get_option("name", "transformer")
        self._class_prefix = self.monolithe_config.get_option("class_prefix", "transformer")
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._product_name = self.monolithe_config.get_option("product_name")

        self.output_directory = "%s/python/%s/%s" % (self._output, self._transformation_name, SDKUtils.get_string_version(self.api_version))
        self.override_folder = os.path.normpath("%s/../../__overrides" % self.output_directory)
        self.fetchers_path = "/fetchers/"

        with open("%s/python/__code_header" % self._output, "r") as f:
            self.header_content = f.read()

    def perform(self, specifications):
        """
        """
        self.model_filenames = dict()
        self.fetcher_filenames = dict()

        task_manager = TaskManager()
        for rest_name, specification in specifications.items():
            task_manager.start_task(method=self._write_model, specification=specification, specification_set=specifications)
            task_manager.start_task(method=self._write_fetcher, specification=specification, specification_set=specifications)
        task_manager.wait_until_exit()

        self._write_session()
        self._write_info()
        self._write_init_models(filenames=self.model_filenames)
        self._write_init_fetchers(filenames=self.fetcher_filenames)
        self._write_attrs_defaults()

    def _write_session(self):
        """ Write SDK session file

            Args:
                version (str): the version of the server

        """
        base_name = "%ssession" % self._product_accronym.lower()
        filename = "%s%s.py" % (self._class_prefix.lower(), base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=self.output_directory, filename=filename, template_name="session.py.tpl",
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content)

    def _write_info(self):
        """ Write API Info file
        """
        self.write(destination=self.output_directory, filename="sdkinfo.py", template_name="sdkinfo.py.tpl",
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._transformation_name,
                   header=self.header_content)

    def _write_init_models(self, filenames):
        """ Write init file

            Args:
                filenames (dict): dict of filename and classes

        """

        self.write(destination=self.output_directory, filename="__init__.py", template_name="__init_model__.py.tpl",
                   filenames=self._prepare_filenames(filenames),
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   header=self.header_content)

    def _prepare_filenames(self, filenames, suffix=''):
        """
        """
        formatted_filenames = {}

        for filename, classname in filenames.items():
            formatted_filenames[filename[:-3]] = str("%s%s%s" % (self._class_prefix, classname, suffix))

        return OrderedDict(sorted(formatted_filenames.items()))

    def _write_model(self, specification, specification_set):
        """ Write autogenerate specification file

        """
        filename = "%s%s.py" % (self._class_prefix.lower(), specification.entity_name.lower())

        override_content = self._extract_override_content(specification.entity_name)
        constants = self._extract_constants(specification)
        superclass_name = "NURESTRootObject" if specification.rest_name == self.api_root else "NURESTObject"

        self.write(destination=self.output_directory, filename=filename, template_name="model.py.tpl",
                   specification=specification,
                   specification_set=specification_set,
                   version=self.api_version,
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   override_content=override_content,
                   superclass_name=superclass_name,
                   constants=constants,
                   header=self.header_content)

        self.model_filenames[filename] = specification.entity_name

    def _write_init_fetchers(self, filenames):
        """ Write fetcher init file

            Args:
                filenames (dict): dict of filename and classes

        """
        destination = "%s%s" % (self.output_directory, self.fetchers_path)
        self.write(destination=destination, filename="__init__.py", template_name="__init_fetcher__.py.tpl",
                   filenames=self._prepare_filenames(filenames, suffix='Fetcher'),
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   header=self.header_content)

    def _write_fetcher(self, specification, specification_set):
        """ Write fetcher

        """
        destination = "%s%s" % (self.output_directory, self.fetchers_path)
        base_name = "%s_fetcher" % specification.entity_name_plural.lower()
        filename = "%s%s.py" % (self._class_prefix.lower(), base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=destination, filename=filename, template_name="fetcher.py.tpl",
                   specification=specification,
                   specification_set=specification_set,
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   override_content=override_content,
                   header=self.header_content)

        self.fetcher_filenames[filename] = specification.entity_name_plural

    def _write_attrs_defaults(self):
        """
        """
        attrs_defaults_path = "%s/../../__attributes_defaults" % self.output_directory

        if not os.path.exists(attrs_defaults_path):
            return None

        defaults_name = "attrs_defaults.ini"
        specific_defaults_name = "%s_attrs_defaults.ini" % self.api_version
        target_folder = "%s/resources" % self.output_directory

        specific_defaults_path = "%s/%s" % (attrs_defaults_path, specific_defaults_name)
        if os.path.exists(specific_defaults_path):
            return (specific_defaults_path, "%s/%s" % (target_folder, defaults_name), target_folder)

        general_defaults_path = "%s/%s" % (attrs_defaults_path, defaults_name)
        if not os.path.exists(general_defaults_path):
            return

        attributes_file = (general_defaults_path, "%s/%s" % (target_folder, defaults_name), target_folder)

        if not attributes_file:
            return

        src, dst, target = attributes_file

        if not os.path.exists(target):
            os.makedirs(target)

        shutil.copyfile(src, dst)

    def _extract_override_content(self, name):
        """
        """
        # find override file
        specific_override_path = "%s/%s_%s%s.override.py" % (self.override_folder, self.api_version, self._class_prefix.lower(), name.lower())
        generic_override_path = "%s/%s%s.override.py" % (self.override_folder, self._class_prefix.lower(), name.lower())
        final_path = specific_override_path if os.path.exists(specific_override_path) else generic_override_path

        # Read override from file
        override_content = None
        if os.path.isfile(final_path):
            override_content = open(final_path).read()

        return override_content

    def _extract_constants(self, specification):
        """ Removes attributes and computes constants

        """
        constants = {}

        for attribute in specification.attributes:

            if attribute.allowed_choices and len(attribute.allowed_choices) > 0:

                name = attribute.local_name.upper()

                for choice in attribute.allowed_choices:
                    constants["CONST_%s_%s" % (name, choice.upper())] = choice

        return constants
