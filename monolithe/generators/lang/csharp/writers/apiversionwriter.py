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

import os
from configparser import RawConfigParser
from monolithe.lib import SDKUtils, TaskManager
from monolithe.generators.lib import TemplateFileWriter

from future import standard_library
from urlparse import urlparse
standard_library.install_aliases()


class APIVersionWriter(TemplateFileWriter):
    """ Provide useful method to write CS files.

    """
    def __init__(self, monolithe_config, api_info):
        """ Initializes a _CSSDKAPIVersionFileWriter

        """
        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.csharp")

        self.api_version = api_info["version"]
        self._api_version_string = SDKUtils.get_string_version(self.api_version)
        self.api_root = api_info["root"]
        self.api_prefix = api_info["prefix"]

        self.monolithe_config = monolithe_config
        self._output = self.monolithe_config.get_option("output", "transformer")
        self._name = self.monolithe_config.get_option("name", "transformer")
        self._class_prefix = ""
        self._product_accronym = self.monolithe_config.get_option("product_accronym")
        self._product_name = self.monolithe_config.get_option("product_name")
        self._url = self.monolithe_config.get_option("url", "transformer")

        self._package_prefix = self._get_package_prefix(self._url)
        self._package_name = self._package_prefix + '.' + self._name + '.' + SDKUtils.get_string_version(self.api_version)
        self._package_subdir = self._package_name.replace('.', '/')

        self._base_output_directory = "%s/csharp" % (self._output)
        self.output_directory = "%s/vspk" % (self._base_output_directory)
        self.override_folder = os.path.normpath("%s/__overrides" % self._base_output_directory)
        self.fetchers_path = "/fetchers/"

        self.attrs_defaults = RawConfigParser()
        path = "%s/csharp/__attributes_defaults/attrs_defaults.ini" % self._output
        self.attrs_defaults.optionxform = str
        self.attrs_defaults.read(path)

        self.attrs_types = RawConfigParser()
        path = "%s/csharp/__attributes_defaults/attrs_types.ini" % self._output
        self.attrs_types.optionxform = str
        self.attrs_types.read(path)

        self.library_version = self.monolithe_config.get_option("version", "transformer")

        with open("%s/csharp/__code_header" % self._output, "r") as f:
            self.header_content = f.read()

    def perform(self, specifications):
        """
        """
        self._set_enum_list_local_type(specifications)
        self._write_sln()
        self._write_csproj(specifications=specifications)
        self._write_session()
        self._write_info()

        task_manager = TaskManager()
        for rest_name, specification in specifications.items():
            task_manager.start_task(method=self._write_model, specification=specification, specification_set=specifications)
            task_manager.start_task(method=self._write_fetcher, specification=specification, specification_set=specifications)
        task_manager.wait_until_exit()

    def _write_session(self):
        """ Write SDK session file

            Args:
                version (str): the version of the server

        """
        base_name = "%sSession" % self._product_accronym
        filename = "vspk/%s%s.cs" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=self.output_directory,
                   filename=filename,
                   template_name="session.cs.tpl",
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   name=self._name,
                   api_prefix=self.api_prefix,
                   override_content=override_content,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=self._package_name)

    def _write_info(self):
        """ Write API Info file
        """
        self.write(destination=self.output_directory,
                   filename="vspk/SdkInfo.cs",
                   template_name="sdkinfo.cs.tpl",
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   class_prefix=self._class_prefix,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._name,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=self._package_name)

    def _write_model(self, specification, specification_set):
        """ Write autogenerate specification file

        """
        filename = "vspk/%s%s.cs" % (self._class_prefix, specification.entity_name)

        override_content = self._extract_override_content(specification.entity_name)
        superclass_name = "RestObject"

        defaults = {}
        section = specification.entity_name
        if self.attrs_defaults.has_section(section):
            for attribute in self.attrs_defaults.options(section):
                defaults[attribute] = self.attrs_defaults.get(section, attribute)

        self.write(destination=self.output_directory,
                   filename=filename,
                   template_name="model.cs.tpl",
                   specification=specification,
                   specification_set=specification_set,
                   version=self.api_version,
                   name=self._name,
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   override_content=override_content,
                   superclass_name=superclass_name,
                   header=self.header_content,
                   version_string=self._api_version_string,
                   package_name=self._package_name,
                   attribute_defaults=defaults)

        return (filename, specification.entity_name)

    def _write_fetcher(self, specification, specification_set):
        """ Write fetcher

        """
        destination = "%s" % (self.output_directory)
        base_name = "%sFetcher" % specification.entity_name_plural
        filename = "vspk/%s%s.cs" % (self._class_prefix, base_name)
        override_content = self._extract_override_content(base_name)

        self.write(destination=destination,
                   filename=filename,
                   template_name="fetcher.cs.tpl",
                   specification=specification,
                   specification_set=specification_set,
                   class_prefix=self._class_prefix,
                   product_accronym=self._product_accronym,
                   override_content=override_content,
                   header=self.header_content,
                   name=self._name,
                   version_string=self._api_version_string,
                   package_name=self._package_name)

        return (filename, specification.entity_name_plural)

    def _write_csproj(self, specifications):
        """
        """
        self.write(destination=self.output_directory+"/vspk", filename="vspk.csproj", template_name="vspk.csproj.tpl",
                   version=self.api_version,
                   specifications=specifications,
                   product_accronym=self._product_accronym,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._name,
                   header=self.header_content)

        self.write(destination=self.output_directory+"/", filename="package.nuspec", template_name="package.nuspec.tpl",
                   version=self.api_version,
		   library_version=self.library_version,
                   specifications=specifications,
                   product_accronym=self._product_accronym,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._name,
                   header=self.header_content)

        self.write(destination=self.output_directory+"/vspk/Properties", filename="AssemblyInfo.cs", template_name="AssemblyInfo.cs.tpl",
                   version=self.api_version,
                   library_version=self.library_version,
                   specifications=specifications,
                   product_accronym=self._product_accronym,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._name,
                   header=self.header_content)

    def _write_sln(self):
        """
        """
        self.write(destination=self.output_directory, filename="vspk.sln", template_name="vspk.sln.tpl",
                   version=self.api_version,
                   product_accronym=self._product_accronym,
                   root_api=self.api_root,
                   api_prefix=self.api_prefix,
                   product_name=self._product_name,
                   name=self._name,
                   header=self.header_content)


    def _extract_override_content(self, name):
        """
        """
        # find override file
        specific_override_path = "%s/%s_%s%s.override.cs" % (self.override_folder, self.api_version, self._class_prefix, name.title())
        generic_override_path = "%s/%s%s.override.cs" % (self.override_folder, self._class_prefix, name.title())
        final_path = specific_override_path if os.path.exists(specific_override_path) else generic_override_path

        # Read override from file
        override_content = None
        if os.path.isfile(final_path):
            override_content = open(final_path).read()

        return override_content

    def _get_package_prefix(self, url):
        """
        """
        hostname_parts = self._get_hostname_parts(url)

        package_name = ""
        for index, hostname_part in enumerate(reversed(hostname_parts)):
            package_name = package_name + hostname_part
            if index < len(hostname_parts) - 1:
                package_name = package_name + '.'

        return package_name

    def _get_hostname_parts(self, url):
        """
        """
        if url.find("http://") != 0:
            url = "http://" + url

        hostname = urlparse(url).hostname
        hostname_parts = hostname.split('.')

        valid_hostname_parts = []
        for hostname_part in hostname_parts:
            if hostname_part != "www":
                valid_hostname_parts.append(hostname_part)

        return valid_hostname_parts

    def _set_enum_list_local_type(self, specifications):
        """ This method is needed until get_type_name() is enhanced to include specification subtype and local_name
        """
        for rest_name, specification in specifications.items():
            for attribute in specification.attributes:
                if attribute.type == "enum":
                    enum_type = attribute.local_name[0:1].upper() + attribute.local_name[1:]
                    attribute.local_type = enum_type
                elif attribute.type == "object":
                    attr_type = "Object"
                    if self.attrs_types.has_option(specification.entity_name, attribute.local_name):
                        type = self.attrs_types.get(specification.entity_name, attribute.local_name)
                        if type:
                            attr_type = type
                    attribute.local_type = attr_type
                elif attribute.type == "list":
                    if attribute.subtype == "enum":
                        enum_subtype = attribute.local_name[0:1].upper() + attribute.local_name[1:]
                        attribute.local_type = "System.Collections.Generic.List<E" + enum_subtype + ">"
                    elif attribute.subtype == "object":
                        attr_subtype = "JObject"
                        if self.attrs_types.has_option(specification.entity_name, attribute.local_name):
                            subtype = self.attrs_types.get(specification.entity_name, attribute.local_name)
                            if subtype:
                                attr_subtype = subtype
                        attribute.local_type = "System.Collections.Generic.List<" + attr_subtype + ">"
                    elif attribute.subtype == "entity":
                        attribute.local_type = "System.Collections.Generic.List<JObject>"
                    else:
                        attribute.local_type = "System.Collections.Generic.List<String>"
