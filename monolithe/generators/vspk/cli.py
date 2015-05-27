#!/usr/bin/env python

import argparse
import sys
import os


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description="VSP SDK Generator.")

    parser.add_argument('-u', "--vsdurl",
                        dest="vsdurl",
                        help="URL of your VSD API where to get the get JSON information without version (ex: https://host:port)",
                        type=str)

    parser.add_argument('-v', "--apiversions",
                        dest="apiversions",
                        help="versions of the SDK to generate (examples: 1.0 3.0 3.1)",
                        nargs="*",
                        type=float)

    parser.add_argument('-f', "--file",
                        dest="swagger_paths",
                        help="Paths to a repository containing swagger api-docs file ",
                        nargs="*",
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
                        dest='specifications_path',
                        help="Path to directory that contains .spec files",
                        type=str)

    parser.add_argument("--doc",
                        dest="generate_doc",
                        help="Flag to generate documentation of the VSPK",
                        action="store_true")

    args = parser.parse_args()

    if not args.vsdurl and "VSD_API_URL" in os.environ: args.vsdurl = os.environ["VSD_API_URL"]
    if not args.apiversions and "VSD_API_VERSION" in os.environ: args.apiversions = [os.environ["VSD_API_VERSION"]]

    from monolithe.generators import VSDKGenerator, VSPKGenerator, VSPKDocumentationGenerator

    versions = args.apiversions

    # Generate VSDK
    if args.vsdurl:
        for version in versions:
            vsdk_generator = VSDKGenerator(vsdurl=args.vsdurl, swagger_path=None, apiversion=version, output_path=args.dest, revision=args.revision, force_removal=args.force_removal, specifications_path=args.specifications_path)
            vsdk_generator.run()
    else:
        versions = []
        for swagger_path in args.swagger_paths:
            vsdk_generator = VSDKGenerator(vsdurl=None, swagger_path=swagger_path, apiversion=None, output_path=args.dest, revision=args.revision, force_removal=args.force_removal, specifications_path=args.specifications_path)
            vsdk_generator.run()
            versions.append(vsdk_generator.apiversion)

    # Packaging a VSPK
    vspk_generator = VSPKGenerator(versions=versions)
    vspk_generator.run()

    # Generate VSPK and VSDK documentation
    if args.generate_doc:
        doc_generator = VSPKDocumentationGenerator()
        doc_generator.run()

if __name__ == '__main__':
    main()
