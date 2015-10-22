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
import importlib
import inspect
import json

from monolithe.lib import Printer, SDKUtils, TaskManager
from monolithe.generators.lib import TemplateFileWriter


class SDKDocWriter(object):
    """ Writer of the Python SDK Documentation

    """

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None

        self.monolithe_config = monolithe_config
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._sdk_output = self.monolithe_config.get_option("sdk_output", "sdk")

    def _parse_module(self, module):
        """
        """
        classes = []

        for module_info in inspect.getmembers(module):

            if not inspect.isclass(module_info[1]):
                continue

            inspected_class = module_info[1]
            inspected_class_name = module_info[0]

            if inspected_class_name in ("NullHandler"):
                continue

            info = {"class_name": inspected_class_name, "constant_names": [], "property_names": [], "inherited_property_names": [], "method_names": [], "inherited_method_names": [], "class_method_names": []}

            for class_info in inspect.getmembers(inspected_class):

                inspected_object = class_info[1]
                inspected_object_name = class_info[0]

                if inspected_object_name.startswith("_"):
                    continue

                if inspect.isbuiltin(inspected_object):
                    continue

                if inspect.ismethod(inspected_object):
                    if inspected_object_name in inspected_class.__dict__:
                        info["method_names"].append(inspected_object_name)
                    else:
                        info["inherited_method_names"].append(inspected_object_name)

                elif inspect.isdatadescriptor(inspected_object):
                    if inspected_object in inspected_class.__dict__.values():
                        info["property_names"].append(inspected_object_name)
                    else:
                        info["inherited_property_names"].append(inspected_object_name)

                elif inspected_object_name.startswith("CONST_"):
                    info["constant_names"].append(inspected_object_name)

            classes.append(info)

        return classes

    def write(self):
        """
        """
        task_manager = TaskManager()

        self.writer = SDKDocFileWriter(self.monolithe_config)
        self.writer.write_index()
        self.writer.write_conf()
        self.writer.write_general_concepts()

        # bambou
        bambou_module = importlib.import_module("bambou")
        bambou_classes = self._parse_module(bambou_module)

        self.writer.write_bambou_reference()
        for bambou_class in bambou_classes:
            task_manager.start_task(self._write_class_references, bambou_class, "bambou", "bambou", "bambou")

        # sdk
        generated_sdk_path = "%s/%s" % (self._sdk_output, self._sdk_name)

        for folder in os.listdir(generated_sdk_path):

            if folder == "cli":
                continue

            if not os.path.isdir("%s/%s" % (generated_sdk_path, folder)):
                continue

            version = SDKUtils.get_float_version(folder)
            self.writer.write_sdk_version_reference(version)

            # sdk model
            sdk_model_module_name = "%s.%s" % (self._sdk_name, folder)
            sdk_model_module = importlib.import_module(sdk_model_module_name)
            sdk_model_classes = self._parse_module(sdk_model_module)

            for sdk_model_class in sdk_model_classes:
                task_manager.start_task(self._write_class_references, sdk_model_class, sdk_model_module_name, "models", "%s/%s" % (self._sdk_name, version))

            # sdk fetchers
            sdk_fetcher_module_name = "%s.%s.fetchers" % (self._sdk_name, folder)
            sdk_fetcher_module = importlib.import_module(sdk_fetcher_module_name)
            sdk_fetcher_classes = self._parse_module(sdk_fetcher_module)

            for sdk_fetcher_class in sdk_fetcher_classes:
                task_manager.start_task(self._write_class_references, sdk_fetcher_class, sdk_fetcher_module_name, "fetchers", "%s/%s" % (self._sdk_name, version))

        task_manager.wait_until_exit()


    def _write_class_references(self, class_info, module_name, file_prefix, folder):
        """
        """
        self.writer.write_class_reference(class_info, module_name, file_prefix, folder)


class SDKDocFileWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        super(SDKDocFileWriter, self).__init__(package="monolithe.generators.sdkdoc")

        self.monolithe_config = monolithe_config
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._product_name = self.monolithe_config.get_option("product_name")
        self._copyright = self.monolithe_config.get_option("copyright")

        self.output_directory = self.monolithe_config.get_option("sdkdoc_tmp_path", "sdkdoc")

    def write_conf(self):
        """
        """
        self.write( destination=self.output_directory, filename="conf.py", template_name="conf.py.tpl",
                    sdk_name=self._sdk_name,
                    copyright=self._copyright)

    def write_index(self):
        """
        """
        with open("%s/pages.json" % self.output_directory) as f:
            pages_info = json.loads(f.read())

        self.write( destination=self.output_directory, filename="index.rst", template_name="index.rst.tpl",
                    sdk_name=self._sdk_name,
                    product_name=self._product_name,
                    pages_info=pages_info)

    def write_general_concepts(self):
        """
        """
        self.write( destination=self.output_directory, filename="general_concepts.rst", template_name="general_concepts.rst.tpl",
                    sdk_name=self._sdk_name,
                    product_name=self._product_name)

    def write_bambou_reference(self):
        """
        """
        self.write( destination=self.output_directory, filename="bambou_reference.rst", template_name="bambou_reference.rst.tpl",
                    sdk_name=self._sdk_name)

    def write_sdk_version_reference(self, version):
        """
        """
        filename = "%s_%s_reference.rst" % (self._sdk_name, version)

        self.write( destination=self.output_directory, filename=filename, template_name="sdk_reference.rst.tpl",
                    sdk_name=self._sdk_name,
                    version=version)

    def write_class_reference(self, class_info, module_name, file_prefix, folder):
        """
        """
        destination = "%s/%s" % (self.output_directory, folder)

        if not os.path.exists(destination):
            try:
                os.makedirs(destination)
            except:
                pass

        filename = "%s.%s.rst" % (file_prefix, class_info["class_name"].lower())

        self.write( destination=destination, filename=filename, template_name="class_reference.rst.tpl",
                    module_name=module_name,
                    class_name=class_info["class_name"],
                    property_names=class_info["property_names"],
                    inherited_property_names=class_info["inherited_property_names"],
                    constant_names=class_info["constant_names"],
                    class_method_names=class_info["class_method_names"],
                    method_names=class_info["method_names"],
                    inherited_method_names=class_info["inherited_method_names"])









