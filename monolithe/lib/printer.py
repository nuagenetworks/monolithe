# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import unicode_literals
from __future__ import print_function
from builtins import object
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
        """
        """
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
