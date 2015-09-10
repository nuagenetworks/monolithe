#!/usr/bin/env python

import argparse
import sys
import os


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description="VSD Documentation Generator.")

    parser.add_argument('-g', "--github",
                        dest="api_url",
                        help="Github API URL",
                        type=str)

    parser.add_argument('-t', "--token",
                        dest="login_or_token",
                        help="Github Token to connect with",
                        type=str)

    parser.add_argument('-o', "--organization",
                        dest="organization",
                        help="Github organization name",
                        type=str)

    parser.add_argument('-r', "--r",
                        dest="repository",
                        help="Github repository name",
                        type=str)

    parser.add_argument('-v', "--versions",
                        dest="versions",
                        help="versions of the SDK to generate (examples: master 3.0 3.1)",
                        nargs="*",
                        type=str,
                        required=True)

    parser.add_argument('-d', "--destination",
                        dest='output_path',
                        default="docgen/apidoc",
                        help="directory where the generated sources will be placed",
                        type=str)

    parser.add_argument("--force",
                        dest="force_removal",
                        help="Force removal of the existing generated code",
                        action="store_true")

    args = parser.parse_args()

    # Use environment variable if necessary
    if not args.api_url and "api_url" in os.environ:
        args.api_url = os.environ["api_url"]

    if not args.login_or_token and "login_or_token" in os.environ:
        args.login_or_token = os.environ["login_or_token"]

    if not args.organization and "GITHUB_ORGANIZATION" in os.environ:
        args.organization = os.environ["GITHUB_ORGANIZATION"]

    if not args.repository and "GITHUB_REPOSITORY" in os.environ:
        args.repository = os.environ["GITHUB_REPOSITORY"]

    # Additional validation
    if not args.api_url:
        parser.error('Please specify a Github API URL using -g or `api_url` environment variable')

    if not args.login_or_token:
        parser.error('Please specify a Github Token using -t or `login_or_token` environment variable')

    if not args.organization:
        parser.error('Please specify a Github Organization name using -o or `GITHUB_ORGANIZATION` environment variable')

    if not args.repository:
        parser.error('Please specify a Github Repository name using -r or `GITHUB_REPOSITORY` environment variable')

    from monolithe.generators import APIDocumentationGenerator

    for version in args.versions:
        generator = APIDocumentationGenerator(api_url=args.api_url, \
                                              login_or_token=args.login_or_token, \
                                              organization=args.organization, \
                                              repository=args.repository, \
                                              version=version, \
                                              output_path=args.output_path, \
                                              force_removal=args.force_removal)
        generator.run()

if __name__ == '__main__':
    main()
