# -*- coding: utf-8 -*-

import os
import shutil
import importlib
import inspect
import json

from monolithe import MonolitheConfig
from monolithe.lib import Printer, SDKUtils, TaskManager
from monolithe.generators.lib.writers import TemplateFileWriter


class SDKDocWriter(object):
    """ Writer of the Python VSD Documentation

    """

    def __init__(self, directory):
        """
        """
        self.writer_directory = directory

    def get_writer(self):
        """
        """
        return SDKDocFileWriter(directory=self.writer_directory)

    def _parse_module(self, module):
        """
        """
        classes = []

        for module_info in inspect.getmembers(module):

            if not inspect.isclass(module_info[1]):
                continue

            inspected_class = module_info[1]
            inspected_class_name = module_info[0]

            if inspected_class_name in ("AutoGenerate", "NullHandler"):
                continue

            info = {"class_name": inspected_class_name, "property_names": [], "method_names": [], "inherited_method_names": [], "class_method_names": []}

            for class_info in inspect.getmembers(inspected_class):

                inspected_object = class_info[1]
                inspected_object_name = class_info[0]

                if inspected_object_name.startswith("_"):
                    continue

                if inspect.isbuiltin(inspected_object):
                    continue

                if inspect.ismethod(inspected_object):
                    if not inspected_object in inspected_class.__dict__:
                        if inspected_object.__self__ is inspected_class:
                            info["method_names"].append(inspected_object_name)
                        else:
                            info["inherited_method_names"].append(inspected_object_name)
                    else:
                        info["method_names"].append(inspected_object_name)

                elif inspect.isdatadescriptor(inspected_object):
                    info["property_names"].append(inspected_object_name)

            classes.append(info)

        return classes

    def write(self):
        """
        """
        sdk_name = MonolitheConfig.get_option("sdk_name", "sdk")
        sdk_output = MonolitheConfig.get_option("sdk_output", "sdk")

        task_manager = TaskManager()

        writer = self.get_writer()
        writer.write_index()
        writer.write_conf()
        writer.write_general_concepts()

        # bambou
        bambou_module = importlib.import_module("bambou")
        bambou_classes = self._parse_module(bambou_module)

        writer.write_bambou_reference()
        for bambou_class in bambou_classes:
            task_manager.start_task(self._write_class_references, bambou_class, "bambou", "bambou", "bambou")

        # sdk
        generated_sdk_path = "%s/%s" % (sdk_output, sdk_name)

        for folder in os.listdir(generated_sdk_path):

            if not os.path.isdir("%s/%s" % (generated_sdk_path, folder)):
                continue

            version = SDKUtils.get_float_version(folder)
            writer.write_sdk_version_reference(version)

            # sdk model
            sdk_model_module_name = "%s.%s" % (sdk_name, folder)
            sdk_model_module = importlib.import_module(sdk_model_module_name)
            sdk_model_classes = self._parse_module(sdk_model_module)

            for sdk_model_class in sdk_model_classes:
                task_manager.start_task(self._write_class_references, sdk_model_class, sdk_model_module_name, "models", "%s/%s" % (sdk_name, version))

            # sdk fetchers
            sdk_fetcher_module_name = "%s.%s.fetchers" % (sdk_name, folder)
            sdk_fetcher_module = importlib.import_module(sdk_fetcher_module_name)
            sdk_fetcher_classes = self._parse_module(sdk_fetcher_module)

            for sdk_fetcher_class in sdk_fetcher_classes:
                task_manager.start_task(self._write_class_references, sdk_fetcher_class, sdk_fetcher_module_name, "fetchers", "%s/%s" % (sdk_name, version))

        task_manager.wait_until_exit()


    def _write_class_references(self, class_info, module_name, file_prefix, folder):
        """
        """
        writer = self.get_writer()
        writer.write_class_reference(class_info, module_name, file_prefix, folder)


class SDKDocFileWriter(TemplateFileWriter):
    """
    """

    def __init__(self, directory):
        """
        """
        super(SDKDocFileWriter, self).__init__(directory=directory, package='monolithe.generators.sdkdoc')

        self._sdk_name = MonolitheConfig.get_option("sdk_name", "sdk")
        self._product_name = MonolitheConfig.get_option("product_name")

    def write_conf(self):
        """
        """
        self.write( destination=self.directory, filename="conf.py", template_name="conf.py.tpl",
                    sdk_name=self._sdk_name,
                    copyright=MonolitheConfig.get_option("copyright"))

    def write_index(self):
        """
        """
        with open("%s/pages.json" % self.directory) as f:
            pages_info = json.loads(f.read())

        self.write( destination=self.directory, filename="index.rst", template_name="index.rst.tpl",
                    sdk_name=self._sdk_name,
                    product_name=self._product_name,
                    pages_info=pages_info)

    def write_general_concepts(self):
        """
        """
        self.write( destination=self.directory, filename="general_concepts.rst", template_name="general_concepts.rst.tpl",
                    sdk_name=self._sdk_name,
                    product_name=self._product_name)

    def write_bambou_reference(self):
        """
        """
        self.write( destination=self.directory, filename="bambou_reference.rst", template_name="bambou_reference.rst.tpl",
                    sdk_name=self._sdk_name)

    def write_sdk_version_reference(self, version):
        """
        """
        filename = "%s_%s_reference.rst" % (self._sdk_name, version)

        self.write( destination=self.directory, filename=filename, template_name="sdk_reference.rst.tpl",
                    sdk_name=self._sdk_name,
                    version=version)

    def write_class_reference(self, class_info, module_name, file_prefix, folder):
        """
        """
        destination = "%s/%s" % (self.directory, folder)

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
                    class_method_names=class_info["class_method_names"],
                    method_names=class_info["method_names"],
                    inherited_method_names=class_info["inherited_method_names"])









