#!/usr/bin/env python

import argparse
import getpass
import os
import sys


def main(argv=sys.argv):
    """

    """
    parser = argparse.ArgumentParser(description="Generates a SDK according from a specification set")

    parser.add_argument("-g", "--github",
                        dest="api_url",
                        help="The Github API URL. Can be given by setting the environment variable \"MONOLITHE_GITHUB_API_URL\"",
                        type=str)

    parser.add_argument("-l", "--login",
                        dest="login",
                        help="The Github Login (if set, you will be prompted for your password). Can be given by setting the environment variable \"MONOLITHE_GITHUB_LOGIN\"",
                        type=str)

    parser.add_argument("-t", "--token",
                        dest="token",
                        help="The Github Token (if set, --login will be ignored). To generate a token, go here https://github.com/settings/tokens. Can be given by setting the environment variable \"$MONOLITHE_GITHUB_TOKEN\"",
                        type=str)

    parser.add_argument("-o", "--organization",
                        dest="organization",
                        help="The Github Organization. Can be given by setting the environment variable \"MONOLITHE_GITHUB_ORGANIZATION\"",
                        type=str)

    parser.add_argument("-r", "--repository",
                        dest="repository",
                        help="The Github Repository. Can be given by setting the environment variable \"MONOLITHE_GITHUB_REPOSITORY\"",
                        type=str)

    parser.add_argument("-b", "--branches",
                        dest="branches",
                        help="The branches of the specifications to use to generate the documentation (examples: \"master 3.2\")",
                        nargs="*",
                        type=str,
                        required=True)

    parser.add_argument("-c", "--config",
                        dest="config_path",
                        help="Path the monolithe configuration file",
                        type=str)

    parser.add_argument("-d", "--doc",
                        dest="generate_doc",
                        help="generate documentation of the SDK",
                        action="store_true")

    args = parser.parse_args()

    # Use environment variable if necessary
    if not args.api_url and "MONOLITHE_GITHUB_API_URL" in os.environ:
        args.api_url = os.environ["MONOLITHE_GITHUB_API_URL"]

    if not args.token and not args.login:

        if "MONOLITHE_GITHUB_TOKEN" in os.environ:
            args.token = os.environ["MONOLITHE_GITHUB_TOKEN"]

        elif "MONOLITHE_GITHUB_LOGIN" in os.environ:
            args.login = os.environ["MONOLITHE_GITHUB_LOGIN"]

    if not args.organization and "MONOLITHE_GITHUB_ORGANIZATION" in os.environ:
        args.organization = os.environ["MONOLITHE_GITHUB_ORGANIZATION"]

    if not args.repository and "MONOLITHE_GITHUB_REPOSITORY" in os.environ:
        args.repository = os.environ["MONOLITHE_GITHUB_REPOSITORY"]

    if not args.config_path and "MONOLITHE_CONFIG_PATH" in os.environ:
        args.config_path = os.environ["MONOLITHE_CONFIG_PATH"]

    # Additional validation
    if not args.api_url:
        args.api_url = raw_input("Enter your Github API URL: ")

    if not args.login and not args.token :
        args.login = raw_input("Enter your Github login: ")

    if not args.organization:
        args.organization = raw_input("Enter your Github organization: ")

    if not args.repository:
        args.repository = raw_input("Enter your Github repository: ")

    if not args.config_path:
        args.config_path = raw_input("Enter the path of the monolithe config file: ")

    # Ask for password
    if args.login:
        password = getpass.getpass(prompt="Enter your Github password for %s: " % args.login)
        login_or_token = args.login
    else:
        password = None
        login_or_token = args.token

    from monolithe import MonolitheConfig
    from monolithe.generators import SDKGenerator, SDKDocGenerator

    monolithe_config = MonolitheConfig.config_with_path(args.config_path)

    # Generate SDK
    generator = SDKGenerator(monolithe_config=monolithe_config)
    generator.generate(api_url=args.api_url, login_or_token=login_or_token, password=password, organization=args.organization, repository=args.repository, branches=args.branches)

    # Generate SDK documentation
    if args.generate_doc:
        doc_generator = SDKDocGenerator(monolithe_config=monolithe_config)
        doc_generator.generate()


if __name__ == "__main__":
    main()
