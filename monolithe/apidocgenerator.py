#!/usr/bin/env python

import argparse
import sys


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description="VSD Documentation Generator.")

    parser.add_argument('-u', "--vsdurl",
                        dest="vsdurl",
                        help="URL of your VSD API where to get the get JSON information without version (ex: https://host:port/web/docs/api/)",
                        type=str)

    parser.add_argument('-v', "--apiversion",
                        dest="apiversion",
                        help="version of the documentation to generate (examples: 1.0, 3.0, 3.1)",
                        type=float)

    parser.add_argument('-f', "--file",
                        dest="path",
                        help="Path to a repository containing api-docs file ",
                        type=str)

    parser.add_argument('-o', "--output",
                        dest="dest",
                        default="docgen/apidoc",
                        help="destination directory for the sources",
                        type=str)

    args = parser.parse_args()

    from monolithe.command import Command
    Command.generate_doc(vsdurl=args.vsdurl, path=args.path, apiversion=args.apiversion, output_path=args.dest)

if __name__ == '__main__':
    main()
