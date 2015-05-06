#!/usr/bin/env python

import os
import sys
import argparse
from pprint import pprint

from specsvalidator.validator import Validator


def main(argv=sys.argv):

    parser = argparse.ArgumentParser(description="API Spec Validator.")

    parser.add_argument('-s', "--specification",
                        dest="specification_path",
                        help="file or folder containing the API specification",
                        required=True,
                        type=str)

    parser.add_argument('-c', "--candidate",
                        dest="candidate_path",
                        help="file of folder containing the API candidate",
                        required=True,
                        type=str)

    args = parser.parse_args()


    validator = Validator(args.specification_path, args.candidate_path)
    validator.run()
    validator.print_console_report()

if __name__ == '__main__':
    main()
