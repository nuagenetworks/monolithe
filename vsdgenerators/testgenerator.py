#!/usr/bin/env python

import argparse
import sys


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description="Courgette Tests Generator.")

    parser.add_argument('-u', "--vsdurl",
                        dest="vsdurl",
                        help="URL of your VSD API where to get the get JSON information without version (ex: https://host:port/web/docs/api/)",
                        required=True,
                        type=str)

    parser.add_argument('-v', "--apiversion",
                        dest="apiversion",
                        help="version of the documentation to generate (examples: 1.0, 3.0, 3.1)",
                        required=True,
                        type=float)

    parser.add_argument('-o', "--output",
                        dest="output_path",
                        help="Output path directory where to write generated files",
                        required=True,
                        type=str)

    args = parser.parse_args()

    from vsdgenerators import Command
    Command.generate_courgette(vsdurl=args.vsdurl, apiversion=args.apiversion, output_path=args.output_path)

if __name__ == '__main__':
    main()
