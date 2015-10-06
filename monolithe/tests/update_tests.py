#!/usr/bin/env python

import os
import subprocess
import argparse
import sys


def copy_files(origin, destination):
    """
    """
    subprocess.call(['rm', '-rf', destination])
    subprocess.call(["cp", "-a", origin, destination])


def update_sdk():
    """
    """
    print "Updating SDK"
    origin_path = "%s/../../examples/codegen" % os.getcwd()
    destination_path = "%s/../../monolithe/tests/base/sdk" % os.getcwd()

    copy_files(origin_path, destination_path)


def update_sdkdoc():
    """
    """
    print "Updating SDK Doc"
    origin_path = "%s/../../examples/sdkdocgen/" % os.getcwd()
    destination_path = "%s/../../monolithe/tests/base/sdkdoc" % os.getcwd()

    copy_files(origin_path, destination_path)


def update_apidoc():
    """
    """
    print "Updating API Doc"
    origin_path = "%s/../../examples/apidocgen/" % os.getcwd()
    destination_path = "%s/../../monolithe/tests/base/apidoc" % os.getcwd()

    copy_files(origin_path, destination_path)

def main(argv=sys.argv):
    """
    """

    parser = argparse.ArgumentParser(description="Update function tests")

    parser.add_argument("--sdk",
                        dest="update_sdk",
                        help="Update SDK tests",
                        action='store_true')

    parser.add_argument("--sdkdoc",
                        dest="update_sdkdoc",
                        help="Update SDK Doc tests",
                        action='store_true')

    parser.add_argument("--apidoc",
                        dest="update_apidoc",
                        help="Update API Doc tests",
                        action='store_true')

    parser.add_argument("-a", "--all",
                        dest="update_all",
                        help="Update all tests",
                        action='store_true')

    args = parser.parse_args()

    if args.update_all or args.update_sdk:
        update_sdk()

    if args.update_all or args.update_sdkdoc:
        update_sdkdoc()

    if args.update_all or args.update_apidoc:
        update_apidoc()


if __name__ == "__main__":
    main()
