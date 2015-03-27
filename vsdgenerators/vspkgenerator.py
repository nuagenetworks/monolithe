#!/usr/bin/env python

import argparse
import sys
import os
import shutil

PATH_VANILLA_VSPK   = "./vanilla/vspk"
PATH_CODEGEN        = "./codegen"
PATH_GENERATED_VSPK = "%s/vspk" % PATH_CODEGEN


def prepare_vspk_destination(source_path, destination_path):
    """ Clean up detination environement """

    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)

    shutil.copytree(source_path, destination_path)


def include_vsdk(vsdk_version, vsdk_base_path, vspk_path):
    """ Install Generated version of VSDK to VSPK"""

    parsed_version  = "v%s" % vsdk_version.replace(".", "_")
    source_sdk_path = "%s/%s/vsdk/" % (vsdk_base_path, vsdk_version)
    dest_sdk_path   = "%s/vspk/vsdk/%s" % (vspk_path, parsed_version)

    print " * Installing vsdk version %s to vspk" % vsdk_version

    shutil.copytree(source_sdk_path, dest_sdk_path)


def main(argv=sys.argv):

    parser = argparse.ArgumentParser(description="VSPK Package Generator.")
    parser.add_argument('-v', "--versions", dest="versions", help="versions of the vsdks to package coma separated, no space", required=True, type=str)

    args = parser.parse_args()

    prepare_vspk_destination(PATH_VANILLA_VSPK, PATH_GENERATED_VSPK)

    for version in args.versions.split(","):
        include_vsdk(version, PATH_CODEGEN, PATH_GENERATED_VSPK)


if __name__ == '__main__':
    main()
