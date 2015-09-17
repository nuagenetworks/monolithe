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

    monolithe_config = MonolitheConfig.config_with_path(args.config_path)

    generator = SDKDocGenerator(monolithe_config=monolithe_config)
    generator.run()

if __name__ == '__main__':
    main()
