#!/usr/bin/env python

import argparse
import sys

sys.path.append("../")


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description="Python SDK Generator.")

    parser.add_argument('-u', "--vsdurl",
                        dest="vsdurl",
                        help="URL of your VSD API where to get the get JSON information without version (ex: https://host:port/web/docs/api/)",
                        type=str)

    parser.add_argument('-v', "--apiversions",
                        dest="versions",
                        help="versions of the SDK to generate (examples: 1.0 3.0 3.1)",
                        nargs="*",
                        type=float)

    parser.add_argument('-f', "--file",
                        dest="path",
                        help="Path to a repository containing api-docs file ",
                        type=str)

    parser.add_argument('-r', "--revision",
                        dest="revision",
                        help="Revision number of the SDK",
                        default=1,
                        type=int)

    parser.add_argument('-o', "--output",
                        dest='dest',
                        help="directory where the sources will be generated",
                        type=str)

    parser.add_argument("--force",
                        dest="force_removal",
                        help="Force removal of the existing generated code",
                        action="store_true")

    parser.add_argument('-s', "--specs",
                        dest='specs_path',
                        help="Path to directory that contains .spec files",
                        type=str)

    args = parser.parse_args()

    from monolithe.command import Command

    if args.versions:
        for version in args.versions:
            Command.generate_sdk(vsdurl=args.vsdurl, path=args.path, apiversion=version, output_path=args.dest, revision=args.revision, force_removal=args.force_removal, specs_path=args.specs_path)
    else:
        Command.generate_sdk(vsdurl=args.vsdurl, path=args.path, apiversion=None, output_path=args.dest, revision=args.revision, force_removal=args.force_removal, specs_path=args.specs_path)

if __name__ == '__main__':
    main()
