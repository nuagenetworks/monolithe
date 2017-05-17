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
import sys

from monolithe.specifications.directory_manager import FolderManager, RepositoryManager
from monolithe.generators import SDKGenerator


def main(argv=sys.argv):
    """

    """
    parser = argparse.ArgumentParser(description="Generates a SDK according from a specification set")

    parser.add_argument("-b", "--branches",
                        dest="branches",
                        metavar="branches",
                        help="The branches of the specifications to use to generate the documentation (examples: \"master 3.2\")",
                        nargs="*",
                        type=str)

    parser.add_argument("-f", "--folder",
                        dest="folder",
                        metavar="folder",
                        required=True,
                        help="Path of the specifications folder. If set, all other attributes will be ignored",
                        type=str)

    parser.add_argument("-c", "--config",
                        dest="config_path",
                        metavar="config_path",
                        help="Path the monolithe configuration file",
                        type=str)

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

    if args.branches:
        directory_manager = RepositoryManager(
            args.folder, config_path=args.config_path)
    else:
        directory_manager = FolderManager(
            args.folder, config_path=args.config_path)

    monolithe_config = directory_manager.monolithe_config

    if monolithe_config and args.vanilla_prefix:
        monolithe_config.set_option("user_vanilla", "%s/%s" % (args.vanilla_prefix, monolithe_config.get_option("user_vanilla", "transformer")), "transformer")

    if monolithe_config and args.generation_version:
        monolithe_config.set_option("version", args.generation_version, "transformer")

    if monolithe_config:
        monolithe_config.language = args.language

    generator = SDKGenerator(directory_manager, args.branches)
    generator.run(args.branches)


if __name__ == "__main__":
    main()
