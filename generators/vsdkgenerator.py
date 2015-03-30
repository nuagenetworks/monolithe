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

    parser.add_argument('-v', "--apiversion",
                        dest="apiversion",
                        help="version of the SDK to generate (examples: 1.0, 3.0, 3.1)",
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

    parser.add_argument('-g', "--giturl",
                        dest="giturl",
                        help="GIT repository URL. If not specified, it will create an SDK from scratch.",
                        # default='https://github.com/nuagenetworks/vsdk',
                        type=str)

    parser.add_argument('-p', "--push",
                        dest='push',
                        help="Push to the GIT repository when finished",
                        action="store_true")

    parser.add_argument('-o', "--output",
                        dest='dest',
                        help="directory where the sources will be generated",
                        type=str)

    args = parser.parse_args()

    from generators import Command
    Command.generate_sdk(vsdurl=args.vsdurl, path=args.path, apiversion=args.apiversion, output_path=args.dest, revision=args.revision, git_repository=args.giturl, push=args.push)

if __name__ == '__main__':
    main()
