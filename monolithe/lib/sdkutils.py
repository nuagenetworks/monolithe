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
from builtins import object

import importlib
from .utils import load_language_plugins


class SDKUtils(object):
    """ SDK Utilities

    """

    idiomatic_methods_cache = {}
    type_methods_cache = {}

    @classmethod
    def massage_type_name(cls, type_name):
        """ Returns a readable type according to a java type

        """
        if type_name.lower() in ("enum", "enumeration"):
            return "enum"

        if type_name.lower() in ("str", "string"):
            return "string"

        if type_name.lower() in ("boolean", "bool"):
            return "boolean"

        if type_name.lower() in ("int", "integer"):
            return "integer"

        if type_name.lower() in ("date", "datetime", "time"):
            return "time"

        if type_name.lower() in ("double", "float", "long"):
            return "float"

        if type_name.lower() in ("list", "array"):
            return "list"

        if type_name.lower() in ("object", "dict"):
            return "object"

        if "array" in type_name.lower():
            return "list"

        return "string"

    @classmethod
    def get_plural(cls, singular_name):
        """ Returns the plural name of the singular name

            Certain words are invariant.

            Args:
                singular_name (string): the singular name to pluralize

            Returns:
                The pluralized version of the singular name

        """
        if singular_name[-1] == "y" and singular_name[-2] not in ["a", "e", "i", "o", "u", "y"]:
            return singular_name[:-1] + "ies"

        if singular_name[-1] != "s":
            return singular_name + "s"

        return singular_name

    @classmethod
    def get_string_version(cls, version):
        """ Get the sdk version according to the given version

            Args:
                version (float): the version

            Returns:
                version as string

            Example:
                get_string_version(3.1)
                >>> v3_1

        """
        if version == "master":
            return version

        return ("v%s" % version).replace(".", "_")

    @classmethod
    def get_float_version(cls, string_version):
        """ Get the sdk version as float according to the given string version

            Args:
                string_version (stirng): the version

            Returns:
                version as float

            Example:
                get_float_version("v3_1")
                >>> 3.1

        """
        if string_version == "master":
            return string_version

        return float(string_version.replace("v", "").replace("_", "."))

    # Commons language conversion

    @classmethod
    def get_idiomatic_name_in_language(cls, name, language):
        """ Get the name for the given language

            Args:
                name (str): the name to convert
                language (str): the language to use

            Returns:
                a name in the given language

            Example:
                get_idiomatic_name_in_language("EnterpriseNetwork", "python")
                >>> enterprise_network
        """
        if language in cls.idiomatic_methods_cache:
            m = cls.idiomatic_methods_cache[language]
            if not m:
                return name
            return m(name)

        found, method = load_language_plugins(language, 'get_idiomatic_name')
        if found:
            cls.idiomatic_methods_cache[language] = method
            if method:
                return method(name)
            else:
                return name

        module = importlib.import_module('.lang.%s' % language, package="monolithe.generators")

        if not hasattr(module, 'get_idiomatic_name'):
            cls.idiomatic_methods_cache[language] = None
            return name

        method = getattr(module, 'get_idiomatic_name')
        cls.idiomatic_methods_cache[language] = method
        return method(name)

    @classmethod
    def get_type_name_in_language(cls, type_name, sub_type, language):
        """ Get the type for the given language

            Args:
                type_name (str): the type to convert
                language (str): the language to use

            Returns:
                a type name in the given language

            Example:
                get_type_name_in_language("Varchar", "python")
                >>> str
        """
        if language in cls.type_methods_cache:
            m = cls.type_methods_cache[language]
            if not m:
                return type_name
            return m(type_name)

        found, method = load_language_plugins(language, 'get_type_name')
        if found:
            cls.type_methods_cache[language] = method
            if method:
                return method(type_name, sub_type)
            else:
                return type_name

        module = importlib.import_module('.lang.%s' % language, package="monolithe.generators")

        if not hasattr(module, 'get_type_name'):
            cls.type_methods_cache[language] = None
            return type_name

        method = getattr(module, 'get_type_name')
        cls.type_methods_cache[language] = method
        return method(type_name, sub_type)
