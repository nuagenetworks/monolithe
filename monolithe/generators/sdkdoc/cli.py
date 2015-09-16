#!/usr/bin/env python

import sys

from monolithe.generators import SDKDocGenerator


def main(argv=sys.argv):
    """ CLI main function

    """
    generator = SDKDocGenerator()
    generator.run()

if __name__ == '__main__':
    main()
