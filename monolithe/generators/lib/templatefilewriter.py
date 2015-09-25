# -*- coding: utf-8 -*-

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

        self.env = Environment(loader=PackageLoader(package, "templates"), extensions=["jinja2.ext.do"])

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
