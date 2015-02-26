#!/usr/bin/env python

import argparse
import sys
import importlib
import os
import shutil
import re
import inspect
import subprocess

VANILLA_DOC = "./vanilla/sphinx"

def _parse_module(module):

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






def _generate_classes_doc(doc_path, some_classes, module_name, file_prefix):

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







def _write_bambou_reference(base_doc_path):
    f = open("%s/bambou_reference.rst" % (base_doc_path), "w")
    f.write("Bambou API Reference\n")
    f.write("====================\n\n")
    f.write(".. toctree::\n")
    f.write("    :maxdepth: 1\n")
    f.write("    :glob:\n\n")
    f.write("    bambou/*\n\n")
    f.close()




def _write_vsdk_reference(base_doc_path):
    model_api_file = open("%s/vsdk_reference.rst" % (base_doc_path), "w")
    model_api_file.write("VSDK API Reference\n")
    model_api_file.write("==================\n\n")
    model_api_file.write("**Models**\n\n")
    model_api_file.write(".. toctree::\n")
    model_api_file.write("    :maxdepth: 1\n")
    model_api_file.write("    :glob:\n\n")
    model_api_file.write("    vsdk/models.*\n\n\n")
    model_api_file.write("**Fetchers**\n\n")
    model_api_file.write(".. toctree::\n")
    model_api_file.write("    :maxdepth: 1\n")
    model_api_file.write("    :glob:\n\n")
    model_api_file.write("    vsdk/fetchers.*\n\n\n")
    model_api_file.close()


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description="VSDK API Reference Documentation Generator.")
    parser.add_argument('-s', "--sources", dest="sources", help="path to directory containing the sources", default='codegen', type=str)
    parser.add_argument('-v', "--version", dest="version", help="version of the vsdk", required=True, type=str)

    args          = parser.parse_args()
    vsdk_path     = "%s/%s" % (args.sources, args.version)
    base_doc_path = "%s/sphinx/" % os.path.abspath(vsdk_path)

    sys.path.append(os.path.abspath(vsdk_path))
    subprocess_environ = {"PYTHONPATH": ":".join(sys.path), "PATH": os.environ["PATH"]}


    ## Sphinx preprocess

    if os.path.exists(base_doc_path):
        shutil.rmtree(base_doc_path)
    shutil.copytree(VANILLA_DOC, base_doc_path)

    process = subprocess.Popen(['sphinx-apidoc', '-o', base_doc_path, vsdk_path], env=subprocess_environ)
    process.communicate()

    ## Bambou

    bambou_doc_path   = "%s/bambou" % base_doc_path

    if os.path.exists(bambou_doc_path):
        shutil.rmtree(bambou_doc_path)
    os.makedirs(bambou_doc_path)

    _write_bambou_reference(base_doc_path)

    bambou_module = importlib.import_module("bambou")
    _generate_classes_doc(bambou_doc_path, _parse_module(bambou_module), "bambou", "bambou")


    ## VSDK

    vsdk_doc_path   = "%s/vsdk" % base_doc_path

    if os.path.exists(vsdk_doc_path):
        shutil.rmtree(vsdk_doc_path)
    os.makedirs(vsdk_doc_path)

    _write_vsdk_reference(base_doc_path)

    vsdk_model_module = importlib.import_module("vsdk")
    _generate_classes_doc(vsdk_doc_path, _parse_module(vsdk_model_module), "vsdk", "models")

    vsdk_fetchers_module = importlib.import_module("vsdk.fetchers")
    _generate_classes_doc(vsdk_doc_path, _parse_module(vsdk_fetchers_module), "vsdk.fetchers", "fetchers")


    ## Sphinx postproccess

    os.remove("%s/vsdk.rst" % base_doc_path)
    os.remove("%s/vsdk.autogenerates.rst" % base_doc_path)
    os.remove("%s/vsdk.fetchers.rst" % base_doc_path)
    os.remove("%s/modules.rst" % base_doc_path)
    os.remove("%s/setup.rst" % base_doc_path)

    #os.system("cd '%s' && make html" % base_doc_path)
    origin_path = os.getcwd()
    os.chdir(base_doc_path)
    process = subprocess.Popen(['make', 'html'], env=subprocess_environ)
    process.communicate()
    os.chdir(origin_path)

    os.system("cd '%s' && rm -rf ./documentation && mv sphinx/_build/html ./documentation && rm -rf sphinx" % vsdk_path)


if __name__ == '__main__':
    main()
