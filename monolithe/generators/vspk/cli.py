#!/usr/bin/env python

import argparse
import getpass
import os
import sys


def main(argv=sys.argv):
    """

    """
    parser = argparse.ArgumentParser(description="VSP SDK Generator.")

    parser.add_argument('-g', "--github",
                        dest="api_url",
                        help="Github API URL",
                        type=str)

    parser.add_argument('-l', "--login",
                        dest="login",
                        help="Github login to connect with",
                        type=str)

    parser.add_argument('-t', "--token",
                        dest="token",
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
                        help="directory where the generated sources will be placed",
                        type=str)

    parser.add_argument("--force",
                        dest="force_removal",
                        help="Force removal of the existing generated code",
                        action="store_true")

    parser.add_argument("--doc",
                        dest="generate_doc",
                        help="Flag to generate documentation of the VSPK",
                        action="store_true")

    args = parser.parse_args()

    # Use environment variable if necessary
    if not args.api_url and "GITHUB_API_URL" in os.environ:
        args.api_url = os.environ["GITHUB_API_URL"]

    if not args.token and not args.login:

        if "GITHUB_TOKEN" in os.environ:
            args.token = os.environ["GITHUB_TOKEN"]

        elif "GITHUB_LOGIN" in os.environ:
            args.login = os.environ["GITHUB_LOGIN"]

    if not args.organization and "SPECIFICATION_ORGANIZATION" in os.environ:
        args.organization = os.environ["SPECIFICATION_ORGANIZATION"]

    if not args.repository and "SPECIFICATION_REPOSITORY" in os.environ:
        args.repository = os.environ["SPECIFICATION_REPOSITORY"]

    # Additional validation
    if not args.api_url:
        args.api_url = raw_input('Enter your Github API URL: ')

    if not args.login and not args.token :
        args.login = raw_input('Enter your Github login: ')

    if not args.organization:
        args.organization = raw_input('Enter your Github organization: ')

    if not args.repository:
        args.repository = raw_input('Enter your Github repository: ')
    # Ask for password
    if args.login:
        password = getpass.getpass(prompt='Enter your Github password for %s: ' % args.login)
        login_or_token = args.login
    else:
        password = None
        login_or_token = args.token

    from monolithe.generators import VSDKGenerator, VSPKGenerator, VSPKDocumentationGenerator

    # Generate VSDK
    for version in args.versions:
        vsdk_generator = VSDKGenerator(api_url=args.api_url, \
                                       login_or_token=login_or_token, \
                                       password=password, \
                                       organization=args.organization, \
                                       repository=args.repository, \
                                       version=version, \
                                       output_path=args.output_path, \
                                       force_removal=args.force_removal)
        vsdk_generator.run()

    # Packaging a VSPK
    vspk_generator = VSPKGenerator(versions=args.versions)
    vspk_generator.run()

    # Generate VSPK and VSDK documentation
    if args.generate_doc:
        doc_generator = VSPKDocumentationGenerator()
        doc_generator.run()


if __name__ == '__main__':
    main()
