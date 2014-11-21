# -*- coding: utf-8 -*-

import os
import logging
from pprint import pprint

from colorama import init
init()
from colorama import Fore, Style

class Printer(object):
    """ Print output for VSD-CLI
    """

    @classmethod
    def colorprint(cls, message, color=''):
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
        raise Exception('\033[91m[Error] %s\033[0m' % message)


    @classmethod
    def success(cls, message):
        """ Print a succcess message

            Args:
                message: the message to print
        """

        cls.colorprint('[Success] %s' % message, Fore.GREEN)

    @classmethod
    def warn(cls, message):
        """ Print a warning message

            Args:
                message: the message to print
        """

        cls.colorprint('[WARNING] %s' % message, Fore.YELLOW)

    @classmethod
    def log(cls, message):
        """ Print a log message

            Args:
                message: the message to print
        """

        cls.colorprint('[LOG] %s' % message, Fore.CYAN)

    @classmethod
    def json(cls, message):
        """ Print a nice JSON output

            Args:
                message: the message to print
        """

        pprint(message)
