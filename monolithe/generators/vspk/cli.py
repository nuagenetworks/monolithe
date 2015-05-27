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
                        dest="swagger_path",
                        help="Path to a repository containing swagger api-docs file ",
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

    # Generate VSDK
    if args.apiversions:
        for version in args.apiversions:
            vsdk_generator = VSDKGenerator(vsdurl=args.vsdurl, swagger_path=args.swagger_path, apiversion=version, output_path=args.dest, revision=args.revision, force_removal=args.force_removal, specifications_path=args.specifications_path)
            vsdk_generator.run()
    else:
        vsdk_generator = VSDKGenerator(vsdurl=args.vsdurl, swagger_path=args.swagger_path, apiversion=None, output_path=args.dest, revision=args.revision, force_removal=args.force_removal, specifications_path=args.specifications_path)
        vsdk_generator.run()

    # Packaging a VSPK
    vspk_generator = VSPKGenerator(versions=args.apiversions)
    vspk_generator.run()

    # Generate VSPK and VSDK documentation
    if args.generate_doc:
        doc_generator = VSPKDocumentationGenerator()
        doc_generator.run()

if __name__ == '__main__':
    main()
