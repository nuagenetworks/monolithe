#!/usr/bin/env python

import sys
import argparse

from monolithe import MonolitheConfig
from monolithe.generators import SDKDocGenerator


def main(argv=sys.argv):
    """
    """

    parser = argparse.ArgumentParser(description="SDK Documentation Generator")

    parser.add_argument("--config",
                        dest="config_path",
                        help="Path the monolithe configuration file",
                        type=str)

    args = parser.parse_args()

    MonolitheConfig.set_config_path(args.config_path)
    generator = SDKDocGenerator()
    generator.run()

if __name__ == '__main__':
    main()
