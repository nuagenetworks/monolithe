# -*- coding: utf-8 -*-

import sys

from collections import OrderedDict
from pprint import pprint

from colorama import init
init()
from colorama import Fore, Style


class Printer(object):
    """ Print output

    """

    __raise_exception__ = False

    @classmethod
    def should_raise_exception(cls, should_raise=True):
        """"""
        cls.__raise_exception__ = should_raise

    @classmethod
    def colorprint(cls, message, color=""):
        """ Print a messsage in a specific color

            Args:
                color: the color of the message
                message: the message to print
        """

        print(color + message + Style.RESET_ALL)

    @classmethod
    def raiseError(cls, message):
        """ Print an error message

            Args:
                message: the message to print
        """
        error_message = "[error] %s" % message
        if cls.__raise_exception__:
            raise Exception(error_message)

        cls.colorprint(error_message, Fore.RED)
        sys.exit(1)

    @classmethod
    def success(cls, message):
        """ Print a succcess message

            Args:
                message: the message to print
        """

        cls.colorprint("[success] %s" % message, Fore.GREEN)

    @classmethod
    def warn(cls, message):
        """ Print a warning message

            Args:
                message: the message to print
        """

        cls.colorprint("[warning] %s" % message, Fore.YELLOW)

    @classmethod
    def log(cls, message):
        """ Print a log message

            Args:
                message: the message to print
        """

        cls.colorprint("[log] %s" % message, Fore.CYAN)

    @classmethod
    def json(cls, message):
        """ Print a nice JSON output

            Args:
                message: the message to print
        """

        if type(message) is OrderedDict:
            pprint(dict(message))
        else:
            pprint(message)
