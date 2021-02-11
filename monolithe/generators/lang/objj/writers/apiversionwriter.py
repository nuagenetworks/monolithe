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
from collections import OrderedDict
from configparser import RawConfigParser

from monolithe.lib import TaskManager
from monolithe.generators.lib import TemplateFileWriter


class APIVersionWriter(TemplateFileWriter):
    """ Provide usefull method to write Objj files.

    """
    def __init__(self, monolithe_config, api_info):
        """
        """
        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.objj")

        self.api_version = api_info["version"]
        self.api_root = api_info["root"]
        self.api_prefix = api_info["prefix"]

        self.monolithe_config = monolithe_config
        self._output = self.monolithe_config.get_option("output", "transformer")
        self._transformation_name = self.monolithe_config.get_option("name", "transformer")
        self._class_prefix = self.monolithe_config.get_option("class_prefix", "transformer")
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._product_name = self.monolithe_config.get_option("product_name")

        self.output_directory = "%s/objj/" % (self._output)
        self.override_folder = os.path.normpath("%s/../../__overrides" % self.output_directory)
        self.fetchers_path = "/Fetchers/"

        self.attrs_defaults = RawConfigParser()
        path = "%s/objj/__attributes_defaults/attrs_defaults.ini" % self._output
        self.attrs_defaults.optionxform = str
        self.attrs_defaults.read(path)

        with open("%s/objj/__code_header" % self._output, "r") as f:
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

        self._write_init_models(filenames=self.model_filenames)
        self._write_init_fetchers(filenames=self.fetcher_filenames)

    def _write_model(self, specification, specification_set):
        """
        """
        filename = "%s%s.j" % (self._class_prefix, specification.entity_name)

        override_content = self._extract_override_content(specification.entity_name)
        constants = self._extract_constants(specification)
        superclass_name = "NURESTAbstractRoot" if specification.rest_name == self.api_root else "NURESTObject"

        defaults = {}
        section = "%s%s" % (self._class_prefix, specification.entity_name)
        if self.attrs_defaults.has_section(section):
            for attribute in self.attrs_defaults.options(section):
                defaults[attribute] = self.attrs_defaults.get(section, attribute)

        self.write(destination=self.output_directory, filename=filename, template_name="ObjectModel.j.tpl",
                   specification=specification,
                   specification_set=specification_set,
                   version=self.api_version,
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   override_content=override_content,
                   superclass_name=superclass_name,
                   constants=constants,
                   header=self.header_content,
                   attribute_defaults=defaults)

        self.model_filenames[filename] = specification.entity_name

    def _write_init_models(self, filenames):
        """
        """
        filename = "Models.j"
        ordered = OrderedDict(sorted(filenames.items()))

        self.write(destination=self.output_directory, filename=filename, template_name="Models.j.tpl",
                   filenames=ordered,
                   class_prefix=self._class_prefix,
                   header=self.header_content)

    def _write_fetcher(self, specification, specification_set):
        """
        """
        destination = "%s/%s" % (self.output_directory, self.fetchers_path)
        base_name = "%sFetcher" % specification.entity_name_plural
        filename = "%s%s.j" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=destination, filename=filename, template_name="ObjectFetcher.j.tpl",
                   specification=specification,
                   class_prefix=self._class_prefix,
                   override_content=override_content,
                   header=self.header_content)

        self.fetcher_filenames[filename] = specification.entity_name_plural

    def _write_init_fetchers(self, filenames):
        """
        """
        filename = "Fetchers/Fetchers.j"
        ordered = OrderedDict(sorted(filenames.items()))

        self.write(destination=self.output_directory, filename=filename, template_name="Fetchers.j.tpl",
                   filenames=ordered,
                   class_prefix=self._class_prefix,
                   header=self.header_content)

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
                name = attribute.local_name
                name = name[:1].upper() + name[1:]
                for choice in attribute.allowed_choices:
                    constants["%s%s%s_%s" % (self._class_prefix, specification.entity_name, name, choice.upper())] = choice
        return constants
