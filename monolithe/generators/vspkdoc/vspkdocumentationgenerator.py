# -*- coding: utf-8 -*-

import sys
import importlib
import os
import shutil
import re
import inspect
import subprocess

from monolithe.lib.utils.printer import Printer


class VSPKDocumentationGenerator(object):
    """ Create a VSPK Documentation

    """
    def __init__(self):
        """ Initialize a VSPKGenerator

        """
        self.vanilla_path = "%s/vanilla" % os.path.dirname(os.path.realpath(__file__))
        self.vspk_path       = "codegen/vspk/vspk"
        self.temp_doc_path   = "/tmp/docgen/vspkdoc"
        self.export_doc_path = "docgen/vspkdoc"

    def run(self):
        """ Create the VSPK package

        """
        Printer.log("Starting VSPK documentation generation")
        sys.path.append(os.path.abspath(self.vspk_path))
        python_path = sys.path
        python_path.append("%s/../../codegen/vspk" % os.path.dirname(os.path.realpath(__file__)))
        subprocess_environ = {"PYTHONPATH": ":".join(python_path), "PATH": os.environ["PATH"]}

        ## Sphinx preprocess
        if os.path.exists(self.temp_doc_path):
            shutil.rmtree(self.temp_doc_path)
        shutil.copytree(self.vanilla_path, self.temp_doc_path)
        process = subprocess.Popen(['sphinx-apidoc', '-o', self.temp_doc_path, self.vspk_path], env=subprocess_environ)
        process.communicate()

        ## Bambou
        bambou_doc_path = "%s/bambou" % self.temp_doc_path
        if os.path.exists(bambou_doc_path):
            shutil.rmtree(bambou_doc_path)
        os.makedirs(bambou_doc_path)
        self._write_bambou_reference(self.temp_doc_path)
        bambou_module = importlib.import_module("bambou")
        self._generate_classes_doc(bambou_doc_path, self._parse_module(bambou_module), "bambou", "bambou")

        ## VSPK
        vspk_doc_path = "%s/vspk" % self.temp_doc_path
        vsdks_path = "%s/vsdk" % self.vspk_path

        for item in os.listdir(vsdks_path):

            if os.path.isfile("%s/%s" % (vsdks_path, item)):
                continue

            version = item.replace("v", "").replace("_", ".")
            version_doc_path = "%s/%s" % (vspk_doc_path, version)

            if os.path.exists(version_doc_path):
                shutil.rmtree(version_doc_path)
            os.makedirs(version_doc_path)

            self._write_vsdk_reference(self.temp_doc_path, version)

            vsdk_model_module = importlib.import_module("vspk.vsdk.%s" % item)
            self._generate_classes_doc(version_doc_path, self._parse_module(vsdk_model_module), "vspk.vsdk.%s" % item, "models")

            vsdk_fetchers_module = importlib.import_module("vspk.vsdk.%s.fetchers" % item)
            self._generate_classes_doc(version_doc_path, self._parse_module(vsdk_fetchers_module), "vspk.vsdk.%s.fetchers" % item, "fetchers")

        ## Sphinx postproccess
        os.system("rm -rf %s/vspk.*.rst" % self.temp_doc_path)
        os.system("rm -rf %s/vspk.rst" % self.temp_doc_path)

        origin_path = os.getcwd()
        os.chdir(self.temp_doc_path)
        process = subprocess.Popen(['make', 'html'], env=subprocess_environ)
        process.communicate()
        os.chdir(origin_path)

        if os.path.exists(self.export_doc_path):
            shutil.rmtree(self.export_doc_path)
        shutil.copytree("%s/_build/html/" % self.temp_doc_path, self.export_doc_path)

        os.system("rm -rf '%s'" % self.temp_doc_path)

        Printer.success("Generated VSPK documentation")

    def _parse_module(self, module):

        classes = []

        for module_info in inspect.getmembers(module):

            if not inspect.isclass(module_info[1]):
                continue

            inspected_class = module_info[1]
            inspected_class_name = module_info[0]

            if inspected_class_name in ("AutoGenerate", "NullHandler"):
                continue

            info = {"classname": inspected_class_name, "properties": [], "methods": [], "inheritedmethods": [], "classmethods": []}

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
                            info["classmethods"].append(inspected_object_name)
                        else:
                            info["inheritedmethods"].append(inspected_object_name)
                    else:
                        info["methods"].append(inspected_object_name)

                elif inspect.isdatadescriptor(inspected_object):
                    info["properties"].append(inspected_object_name)

            classes.append(info)

        return classes

    def _generate_classes_doc(self, doc_path, some_classes, module_name, file_prefix):

        for class_info in some_classes:

            class_name = class_info["classname"]
            title = "%s" % class_name
            f = open("%s/%s.%s.rst" % (doc_path, file_prefix, class_name.lower()), "w")
            f.write("%s\n" % title)
            f.write("%s\n\n" % re.sub(r".", "=", title))

            f.write(".. autoclass:: %s.%s\n\n" % (module_name, class_name))

            properties = class_info["properties"]
            if len(properties):
                f.write("Properties\n----------\n\n")
                for prop_name in properties:
                    f.write("    .. autoattribute:: %s.%s.%s\n\n" % (module_name, class_name, prop_name))

            classmethods = class_info["classmethods"]
            if len(classmethods):
                f.write("Class Methods\n-------------\n\n")
                for method_name in classmethods:
                    f.write("    .. automethod:: %s.%s.%s\n\n" % (module_name, class_name, method_name))

            methods = class_info["methods"]
            if len(methods):
                f.write("Methods\n-------------\n\n")
                for method_name in methods:
                    f.write("    .. automethod:: %s.%s.%s\n\n" % (module_name, class_name, method_name))

            inheritedmethods = class_info["inheritedmethods"]
            if len(inheritedmethods):
                f.write("Inherited Methods\n-----------------\n\n")

                for method_name in inheritedmethods:
                    f.write("    .. automethod:: %s.%s.%s\n\n" % (module_name, class_name, method_name))

            f.write("\n")
            f.close()

    def _write_bambou_reference(self, base_doc_path):
        f = open("%s/bambou_reference.rst" % (base_doc_path), "w")
        f.write("Bambou API Reference\n")
        f.write("====================\n\n")
        f.write(".. toctree::\n")
        f.write("    :maxdepth: 1\n")
        f.write("    :glob:\n\n")
        f.write("    bambou/*\n\n")
        f.close()

    def _write_vsdk_reference(self, base_doc_path, version):
        model_api_file = open("%s/vsdk_%s_reference.rst" % (base_doc_path, version), "w")
        model_api_file.write("VSDK API %s Reference\n" % version)
        model_api_file.write("=======================\n\n")
        model_api_file.write("**Models**\n\n")
        model_api_file.write(".. toctree::\n")
        model_api_file.write("    :maxdepth: 1\n")
        model_api_file.write("    :glob:\n\n")
        model_api_file.write("    vspk/%s/models.*\n\n\n" % version)
        model_api_file.write("**Fetchers**\n\n")
        model_api_file.write(".. toctree::\n")
        model_api_file.write("    :maxdepth: 1\n")
        model_api_file.write("    :glob:\n\n")
        model_api_file.write("    vspk/%s/fetchers.*\n\n\n" % version)
