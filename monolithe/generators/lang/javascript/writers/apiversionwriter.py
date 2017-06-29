from monolithe.generators.lib import TemplateFileWriter
import os
import shutil

baseAttrs = ['entityScope', 'externalID', 'lastUpdatedBy'];

class APIVersionWriter(TemplateFileWriter):
    """ This class is reponsible to write files for a particular api version. """

    def __init__(self, monolithe_config, api_info):

        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.javascript")

        output = monolithe_config.get_option("output", "transformer")

        self.output_directory = "%s/javascript/%s" % (output, api_info["version"])
        if os.path.exists(self.output_directory):
            shutil.rmtree(self.output_directory)

        self.api_root = api_info["root"]
        self._class_prefix = monolithe_config.get_option("class_prefix", "transformer")


    def perform(self, specifications):
        """ This method is the entry point of javascript code writer. Monolithe will call it when
        the javascript plugin is to generate code.
        """
        for rest_name, specification in specifications.iteritems():
            self._write_model(specification=specification)

    def _write_model(self, specification):
        """ This method writes the ouput for a particular specification.
        """
        filename = 'NU%s.js' % specification.entity_name

        superclass_name = "NURootEntity" if specification.rest_name == self.api_root else "NUEntity"
        # write will write a file using a template.
        # mandatory params: destination directory, destination file name, template file name
        # optional params: whatever that is needed from inside the Jinja template

        specification.attributes = [attribute for attribute in specification.attributes if attribute.name not in baseAttrs]

        self.write(destination=self.output_directory, filename=filename, template_name="entity.js.tpl",
                   class_prefix=self._class_prefix,
                   specification=specification,
                   superclass_name = superclass_name)
