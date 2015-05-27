#!/usr/bin/env python

import sys

from monolithe.generators import VSPKDocumentationGenerator


def main(argv=sys.argv):
    """ CLI main function

    """
    generator = VSPKDocumentationGenerator()
    generator.run()

if __name__ == '__main__':
    main()
