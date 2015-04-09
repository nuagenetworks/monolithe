#!/usr/bin/env python

import argparse
import sys
import os
import shutil

PATH_VANILLA_VSPK = '%s/vanilla/vspk' % os.path.dirname(os.path.realpath(__file__))
PATH_CODEGEN        = "./codegen"
PATH_GENERATED_VSPK = "%s/vspk" % PATH_CODEGEN


def prepare_vspk_destination(source_path, destination_path):
    """ Clean up detination environement """

    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)

    shutil.copytree(source_path, destination_path)


def include_vsdk(vsdk_version, vsdk_base_path, vspk_path):
    """ Install Generated version of vsdk to vspk"""

    parsed_version  = "v%s" % vsdk_version.replace(".", "_")
    source_sdk_path = "%s/%s/vsdk/" % (vsdk_base_path, vsdk_version)
    dest_sdk_path   = "%s/vspk/vsdk/%s" % (vspk_path, parsed_version)

    print " * Packaging vsdk version %s to vspk" % vsdk_version

    shutil.copytree(source_sdk_path, dest_sdk_path)


def main(argv=sys.argv):

    parser = argparse.ArgumentParser(description="vspk Package Generator.")
    parser.add_argument('-v', "--versions", dest="versions", nargs='*', help="Specify all supported VSDK versions", required=True, type=str)

    args = parser.parse_args()

    prepare_vspk_destination(PATH_VANILLA_VSPK, PATH_GENERATED_VSPK)

    for version in args.versions:
        include_vsdk(version, PATH_CODEGEN, PATH_GENERATED_VSPK)


if __name__ == '__main__':
    main()
