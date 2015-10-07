#!/usr/bin/env python
{{ header }}

import argparse
import sys

sys.path.append("../")

class _HelpAction(argparse._HelpAction):

    def __call__(self, parser, namespace, values, option_string=None):
        parser.print_help()

        subparsers_actions = [
            action for action in parser._actions
            if isinstance(action, argparse._SubParsersAction)]

        for subparsers_action in subparsers_actions:

            for choice, subparser in subparsers_action.choices.items():
                print("\n{}:\n{}".format(choice.upper(), "-" * (len(choice) + 1)))
                print(subparser.format_help())

        parser.exit()


def main(argv=sys.argv):

    default_parser = argparse.ArgumentParser(description="CLI for {{ product_name }}", add_help=False)
    default_parser.add_argument("-v", "--verbose", help="Activate verbose mode", action="store_true")
    default_parser.add_argument("--username", help="Username to get an api key or set '{{ product_accronym }}_USERNAME' in your variable environment")
    default_parser.add_argument("--password", help="Password to get an api key or set '{{ product_accronym }}_PASSWORD' in your variable environment")
    default_parser.add_argument("--api", help="URL of the API endpoint or set '{{ product_accronym }}_API_URL' in your variable environment")
    default_parser.add_argument("--version", help="Version of the API or set '{{ product_accronym }}_API_VERSION' in your variable environment")
    default_parser.add_argument("--enterprise", help="Name of the enterprise to connect or set '{{ product_accronym }}_ENTERPRISE' in your variable environment")
    default_parser.add_argument("--json", help="Add this option get a JSON output or set {{ product_accronym }}_JSON_OUTPUT=True", action="store_true")

    parser = argparse.ArgumentParser(description="CLI for {{ product_accronym }} Software Development Kit", add_help=False)
    parser.add_argument("-h", "--help", action=_HelpAction, help="help for help if you need some help")

    subparsers = parser.add_subparsers(dest="command",
                                       title="All available commands")

    # List Command
    list_parser = subparsers.add_parser("list", description="List all objects", parents=[default_parser])
    list_parser.add_argument("list", help="Name of the object (See command 'objects' to list all objects name)")
    list_parser.add_argument("--in", dest="parent_infos", nargs=2, help="Specify the PARENT_NAME and PARENT_UUID")
    list_parser.add_argument("-f", "--filter", dest="filter", help="Specify a filter predicate")
    list_parser.add_argument("-x", "--fields", dest="fields", help="Specify output fields", nargs="+", type=str)

    # Count Command
    list_parser = subparsers.add_parser("count", description="Count all objects", parents=[default_parser])
    list_parser.add_argument("count", help="Name of the object (See command 'objects' to list all objects name)")
    list_parser.add_argument("--in", dest="parent_infos", nargs=2, help="Specify the parent name and its uuid")
    list_parser.add_argument("-f", "--filter", dest="filter", help="Specify a filter predicate")
    list_parser.add_argument("-x", "--fields", dest="fields", help="Specify output fields", nargs="+", type=str)

    # Show Command
    show_parser = subparsers.add_parser("show", description="Show a specific object", parents=[default_parser])
    show_parser.add_argument("show", help="Name of the object to show (See command 'objects' to list all objects name)")
    show_parser.add_argument("-i", "--id", dest="id", help="Identifier of the object to show", required=True)
    show_parser.add_argument("-x", "--fields", dest="fields", help="Specify output fields", nargs="+", type=str)

    # Create Command
    create_parser = subparsers.add_parser("create", description="Create a new object", parents=[default_parser])
    create_parser.add_argument("create", help="Name of the object to create (See command 'objects' to list all objects name)")
    create_parser.add_argument("--in", dest="parent_infos", nargs=2, help="Specify the parent name and its uuid")
    create_parser.add_argument("-p", "--params", dest="params", nargs="*", help="List of Key=Value parameters", required=True)

    # Update Command
    update_parser = subparsers.add_parser("update", description="Update an existing object", parents=[default_parser])
    update_parser.add_argument("update", help="Name of the object to update (See command 'objects' to list all objects name)")
    update_parser.add_argument("-i", "--id", dest="id", help="Identifier of the object to show", required=True)
    update_parser.add_argument("-p", "--params", dest="params", nargs="*", help="List of Key=Value parameters", required=True)

    # Delete Command
    delete_parser = subparsers.add_parser("delete", description="Delete an existing object", parents=[default_parser])
    delete_parser.add_argument("delete", help="Name of the object to update (See command 'objects' to list all objects name)")
    delete_parser.add_argument("-i", "--id", dest="id", help="Identifier of the object to show", required=True)

    # Resources Command
    objects_parser = subparsers.add_parser("objects", description="Explore all objects", parents=[default_parser])
    objects_parser.add_argument("-f", "--filter", dest="filter", help="Filter by name (ex: -f nsg)")
    objects_parser.add_argument("-p", "--parent", dest="parent", help="Filter by parent (ex -p enterprise)")
    objects_parser.add_argument("-c", "--child", dest="child", help="Filter by children (ex: -c domain)")

    args = parser.parse_args()

    from commands import CLICommand
    CLICommand.execute(args)


if __name__ == "__main__":
    main()
