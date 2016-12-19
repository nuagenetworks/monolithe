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
import os

from jinja2 import Environment, PackageLoader


class _FileWriter(object):
    """ Writer a file content

    """
    def write(self, destination, filename, content):
        """ Write a file at the specific destination with the content.

            Args:
                destination (string): the destination location
                filename (string): the filename that will be written
                content (string): the content of the filename

        """
        if not os.path.exists(destination):
            try:
                os.makedirs(destination)
            except:  # The directory can be created while creating it.
                pass

        filepath = "%s/%s" % (destination, filename)

        f = open(filepath, "w+")
        f.write(content)
        f.close()


class TemplateFileWriter(_FileWriter):
    """ Write a template file

    """

    def __init__(self, package):
        """ Initializes a FileWriter

        """
        super(TemplateFileWriter, self).__init__()

        templates = "templates"

        self.env = Environment(loader=PackageLoader(package, templates), extensions=["jinja2.ext.do"])

    def write(self, destination, filename, template_name, **kwargs):
        """ Write a file according to the template name

            Args:
                destination (string): the destination location
                filename (string): the filename that will be written
                template_name (string): the name of the template
                kwargs (dict): all attribute that will be passed to the template
        """
        template = self.env.get_template(template_name)
        content = template.render(kwargs)
        super(TemplateFileWriter, self).write(destination=destination, filename=filename, content=content)
