#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function
import argparse
import getpass
import os
import sys

from monolithe import MonolitheConfig
from monolithe.generators import SDKGenerator


def main(argv=sys.argv):
    """

    """
    parser = argparse.ArgumentParser(description="Generates a SDK according from a specification set")

    parser.add_argument("-g", "--github",
                        dest="api_url",
                        metavar="github_api_url",
                        help="The GitHub API URL. Can be given by setting the environment variable \"MONOLITHE_GITHUB_API_URL\"",
                        type=str)

    parser.add_argument("-l", "--login",
                        dest="login",
                        metavar="login_login",
                        help="The GitHub Login (if set, you will be prompted for your password). Can be given by setting the environment variable \"MONOLITHE_GITHUB_LOGIN\"",
                        type=str)

    parser.add_argument("-t", "--token",
                        dest="token",
                        metavar="github_token",
                        help="The GitHub Token (if set, --login will be ignored). To generate a token, go here https://github.com/settings/tokens. Can be given by setting the environment variable \"$MONOLITHE_GITHUB_TOKEN\"",
                        type=str)

    parser.add_argument("-o", "--organization",
                        dest="organization",
                        metavar="github_organization",
                        help="The GitHub Organization. Can be given by setting the environment variable \"MONOLITHE_GITHUB_ORGANIZATION\"",
                        type=str)

    parser.add_argument("-r", "--repository",
                        dest="repository",
                        metavar="github_repository",
                        help="The GitHub Repository. Can be given by setting the environment variable \"MONOLITHE_GITHUB_REPOSITORY\"",
                        type=str)

    parser.add_argument("-b", "--branches",
                        dest="branches",
                        metavar="branches",
                        help="The branches of the specifications to use to generate the documentation (examples: \"master 3.2\")",
                        nargs="*",
                        type=str)

    parser.add_argument("-p", "--path",
                        dest="repository_path",
                        metavar="path",
                        help="The relative repository path of the specification folder. Can be given by setting the environment variable \"MONOLITHE_GITHUB_REPOSITORY_PATH\"",
                        type=str)

    parser.add_argument("-f", "--folder",
                        dest="folder",
                        metavar="folder",
                        help="Path of the specifications folder. If set, all other attributes will be ignored",
                        type=str)

    parser.add_argument("-c", "--config",
                        dest="config_path",
                        metavar="config_path",
                        help="Path the monolithe configuration file",
                        type=str)

    parser.add_argument("-d", "--doc",
                        dest="generate_doc",
                        help="generate documentation of the SDK",
                        action="store_true")

    parser.add_argument("--vanilla-prefix",
                        dest="vanilla_prefix",
                        help="Prefix added to all vanilla path declared in the monolithe configuration file",
                        required=False,
                        type=str)

    parser.add_argument("--generation-version",
                        dest="generation_version",
                        help="Overwrite the sdk version given in monolithe.conf",
                        required=False,
                        type=str)

    parser.add_argument("-L", "--language",
                        dest="language",
                        help="Choose the output language of the SDK. Default is python",
                        default='python',
                        type=str)

    args = parser.parse_args()

    monolithe_config = None
    if args.config_path:
        monolithe_config = MonolitheConfig.config_with_path(args.config_path)

    if monolithe_config and args.vanilla_prefix:
        monolithe_config.set_option("user_vanilla", "%s/%s" % (args.vanilla_prefix, monolithe_config.get_option("user_vanilla", "transformer")), "transformer")

    if monolithe_config and args.generation_version:
        monolithe_config.set_option("version", args.generation_version, "transformer")

    if monolithe_config:
        monolithe_config.language = args.language

    generator = SDKGenerator(monolithe_config=monolithe_config)

    if args.folder:
        generator.initialize_folder_manager(folder=args.folder)
        if not monolithe_config:
            monolithe_config = generator.retrieve_monolithe_config_from_folder(language=args.language)
        generator.generate_from_folder()

    else:
        if not args.branches:
            print("You must provide the --branches options. Use --help for help.")
            sys.exit(1)

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

        if not args.repository_path and "MONOLITHE_GITHUB_REPOSITORY_PATH" in os.environ:
            args.repository_path = os.environ["MONOLITHE_GITHUB_REPOSITORY_PATH"]

        if not args.config_path and "MONOLITHE_CONFIG_PATH" in os.environ:
            args.config_path = os.environ["MONOLITHE_CONFIG_PATH"]

        if not args.repository_path:
            args.repository_path = "/"

        login_or_token = None
        password = None
        if args.token:
            password = None
            login_or_token = args.token
        elif args.login:
            login_or_token = args.login
            password = getpass.getpass(prompt="Enter your GitHub password for %s: " % args.login)

        generator.initialize_repository_manager(api_url=args.api_url,
                                                login_or_token=login_or_token,
                                                password=password,
                                                organization=args.organization,
                                                repository=args.repository,
                                                repository_path=args.repository_path)
        if not monolithe_config:
            monolithe_config = generator.retrieve_monolithe_config_from_repo(branch=args.branches[0], language=args.language)

        generator.generate_from_repo(branches=args.branches)

    # Generate SDK documentation
    if args.generate_doc:
        generator.generate_documentation()

if __name__ == "__main__":
    main()
