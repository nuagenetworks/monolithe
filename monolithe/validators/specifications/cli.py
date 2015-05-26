#!/usr/bin/env python

import argparse
import sys


def generate_labels(errors):
    labels = ""
    if "missing_declarations" in errors and len(errors["missing_declarations"]):
        labels = "%s%s " % (labels, c("[missing declaration]", "red"))

    if "extra_declarations" in errors and len(errors["extra_declarations"]):
        labels = "%s%s " % (labels, c("[extra declaration]", "blue"))

    if "mispelled_declarations" in errors and len(errors["mispelled_declarations"]):
        labels = "%s%s " % (labels, c("[mispelled declaration]", "orange"))

    if "characteristic_mismatches" in errors and len(errors["characteristic_mismatches"]):
        labels = "%s%s " % (labels, c("[characteristic mismatch]", "mauve"))

    if "missing_characteristics" in errors and len(errors["missing_characteristics"]):
        labels = "%s%s " % (labels, c("[missing characteristic]", "blue"))

    return labels

def c(text, color):
    colors = {"mauve": '\033[95m', "blue": '\033[94m', "green": '\033[92m', "grey": "\033[37m", "orange": '\033[93m', "red": '\033[91m', "end": '\033[0m', "bold": '\033[1m', "underline": '\033[4m'}
    return "%s%s%s" % (colors[color], text, colors["end"])

def print_line(char="=", color="grey"):
    line = "".join([char for i in range(0, 80)])
    print c("%s" % line, "grey")


def print_report(name, report):
    print
    print_line()
    print " %s" % c(c(name, "blue"), "bold")
    print_line()
    print

    for declaration_name, errors in report.iteritems():

        print
        print_line('-')
        print "%s %s" % (c(declaration_name, "bold"), generate_labels(errors))
        print_line('-')
        print
        if "missing_declarations" in errors and len(errors["missing_declarations"]):

            for error in errors["missing_declarations"]:
                print "  - %s is missing" % c(error.declaration_name, "bold")

        if "mispelled_declarations" in errors and len(errors["mispelled_declarations"]):

            for error in errors["mispelled_declarations"]:
                print " %s is missing but you declared the following very similar: \n" % c(error.declaration_name, "bold")

                for declaration in error.potential_declarations:
                    print "  - %s" % c(declaration, "bold")

        if "extra_declarations" in errors and len(errors["extra_declarations"]):

            for error in errors["extra_declarations"]:
                print " %s is not declared in specification." % c(error.declaration_name, "bold")

        if "missing_characteristics" in errors and len(errors["missing_characteristics"]):

            for error in errors["missing_characteristics"]:
                print " %s is missing." % c(error.characteristic_name, "bold")

        if "characteristic_mismatches" in errors and len(errors["characteristic_mismatches"]):

            for error in errors["characteristic_mismatches"]:
                print " %s is expected to be %s but it is %s" % (c(error.characteristic_name, "bold"), c(error.expected_value, "bold"), c(error.actual_value, "bold"))
        print

def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description="Specifications Validators.")

    # VSD
    parser.add_argument('-u', "--vsdurl",
                        dest="vsdurl",
                        help="URL of your VSD Server (example: 'https://vsd.com:8443')",
                        type=str)

    parser.add_argument('-v', "--apiversion",
                        dest="apiversion",
                        help="version the VSD API (example: '3.2')",
                        type=float)

    # Github
    parser.add_argument('-g', "--githubapiurl",
                        dest="githubapiurl",
                        help="URL for the Github API v3 (default: 'http://github.mv.usa.alcatel.com/api/v3')",
                        default="http://github.mv.usa.alcatel.com/api/v3",
                        type=str)

    parser.add_argument('-t', "--githubtoken",
                        dest="githubtoken",
                        help="Authentication Token for Github",
                        type=str)

    parser.add_argument('-o', "--githuborganization",
                        dest="githuborganization",
                        help="Organization name where to find the specifications repository",
                        default="Documentation",
                        type=str)

    parser.add_argument('-r', "--githubrepo",
                        dest="githubrepo",
                        help="Repository name of the specifications",
                        default="api-specifications",
                        type=str)

    # Specifications
    parser.add_argument('-b', "--branch",
                        dest="specifications_branch",
                        help="Branch to use to get specifications files (default: 'master')",
                        default="master",
                        type=str)

    parser.add_argument('-s', "--specifications",
                        dest="specification_files",
                        help="specifications to validate",
                        nargs="*",
                        type=str)

    # Commands
    parser.add_argument("--list-branches",
                        dest="command_list_branches",
                        help="Final. prints the list of available specification branches",
                        action="store_true")

    parser.add_argument("--list-specifications",
                        dest="command_list_specifications",
                        help="Final. prints the list of available specification files in given branch",
                        action="store_true")

    parser.add_argument("--run-validation",
                        dest="command_validate",
                        help="Final. print the valdation reports",
                        action="store_true")

    args = parser.parse_args()

    if not args.vsdurl and "VSD_URL" in os.environ: args.vsdurl = os.environ["VSD_URL"]
    if not args.apiversion and "VSD_API_VERSION" in os.environ: args.apiversion = os.environ["VSD_API_VERSION"]
    if not args.githubtoken and "GITHUB_TOKEN" in os.environ: args.githubtoken = os.environ["GITHUB_TOKEN"]


    from monolithe.validators.specifications import SpecificationsValidator

    validator = SpecificationsValidator(github_api_url=args.githubapiurl, github_token=args.githubtoken, specification_organization=args.githuborganization, github_specifications_repository=args.githubrepo)

    if args.command_list_branches:
        for version in validator.available_specification_versions():
            print " - %s" % version
        sys.exit(0)

    if args.command_list_specifications:
        for spec in validator.available_specification_files(args.specifications_branch):
            print " - %s" % spec.replace(".spec", "")
        sys.exit(0)

    if args.command_validate:
        result = validator.run_validation(specification_version=args.specifications_branch, specification_files=args.specification_files, vsd_server_url=args.vsdurl, vsd_api_version=args.apiversion)[0]

        import pprint
        # pprint.pprint(result)
        for report in result:
            print_report("Self API Validation Errors", report["contents"]["self_api_errors"])
            print_report("Parent API Validation Errors", report["contents"]["parent_api_errors"])
            print_report("Attributes Validation Errors", report["contents"]["attribute_errors"])

        sys.exit(0)

if __name__ == '__main__':
    main()
