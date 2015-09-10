#!/usr/bin/env python

import argparse
import sys
import os


def main(argv=sys.argv):
    """

    """
    parser = argparse.ArgumentParser(description="VSP SDK Generator.")

    parser.add_argument('-g', "--github",
                        dest="github_api_url",
                        help="Github API URL",
                        type=str)

    parser.add_argument('-t', "--token",
                        dest="github_token",
                        help="Github Token to connect",
                        type=str)

    parser.add_argument('-o', "--organization",
                        dest="specification_organization",
                        help="Github organization name",
                        type=str)

    parser.add_argument('-r', "--r",
                        dest="github_specifications_repository",
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
    if not args.github_api_url and "GITHUB_API_URL" in os.environ:
        args.github_api_url = os.environ["GITHUB_API_URL"]

    if not args.github_token and "GITHUB_TOKEN" in os.environ:
        args.github_token = os.environ["GITHUB_TOKEN"]

    if not args.specification_organization and "GITHUB_ORGANIZATION" in os.environ:
        args.specification_organization = os.environ["GITHUB_ORGANIZATION"]

    if not args.github_specifications_repository and "GITHUB_REPOSITORY" in os.environ:
        args.github_specifications_repository = os.environ["GITHUB_REPOSITORY"]

    # Additional validation
    if not args.github_api_url:
        parser.error('Please specify a Github API URL using -g or `GITHUB_API_URL` environment variable')

    if not args.github_token:
        parser.error('Please specify a Github Token using -t or `GITHUB_TOKEN` environment variable')

    if not args.specification_organization:
        parser.error('Please specify a Github Organization name using -o or `GITHUB_ORGANIZATION` environment variable')

    if not args.github_specifications_repository:
        parser.error('Please specify a Github Repository name using -r or `GITHUB_REPOSITORY` environment variable')

    from monolithe.generators import VSDKGenerator, VSPKGenerator, VSPKDocumentationGenerator

    # Generate VSDK
    for version in args.versions:
        vsdk_generator = VSDKGenerator(github_api_url=args.github_api_url, github_token=args.github_token, specification_organization=args.specification_organization, github_specifications_repository=args.github_specifications_repository, version=version, output_path=args.output_path, force_removal=args.force_removal)
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
