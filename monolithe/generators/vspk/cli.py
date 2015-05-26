#!/usr/bin/env python

import argparse
import sys


def main(argv=sys.argv):
    """ CLI main function

    """
    parser = argparse.ArgumentParser(description="VSPK Package Generator.")
    parser.add_argument('-v', "--versions", dest="versions", nargs='*', help="Specify all supported VSDK versions", required=True, type=str)

    args = parser.parse_args()

    from monolithe.generators.vspk import VSPKGenerator

    generator = VSPKGenerator(versions=args.versions)
    generator.run()


if __name__ == '__main__':
    main()
