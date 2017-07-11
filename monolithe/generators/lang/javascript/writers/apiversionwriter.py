from monolithe.generators.lib import TemplateFileWriter
import os
import shutil

base_attrs = ['entityScope', 'externalID', 'lastUpdatedBy'];
named_entity_attrs = ['name', 'description'];


class APIVersionWriter(TemplateFileWriter):
    """ This class is reponsible to write files for a particular api version. """

    def __init__(self, monolithe_config, api_info):

        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.javascript")

        output = monolithe_config.get_option("output", "transformer")

        self.output_directory = "%s/javascript/%s" % (output, api_info["version"])
        self.abstract_directory =  "%s/abstract" % self.output_directory
        self.enum_directory =  "%s/enums" % self.output_directory

        if os.path.exists(self.output_directory):
            shutil.rmtree(self.output_directory)

        self.api_root = api_info["root"]
        self._class_prefix = monolithe_config.get_option("class_prefix", "transformer")


    def perform(self, specifications):
        """ This method is the entry point of javascript code writer. Monolithe will call it when
        the javascript plugin is to generate code.
        """
        self.enum_list = [];

        self._write_abstract_named_entity()
        
        for rest_name, specification in specifications.iteritems():
            self._write_model(specification=specification)

        self.write(destination = self.enum_directory,
                    filename="index.js",
                    template_name="enum_index.js.tpl",
                    class_prefix = self._class_prefix,
                    enum_list = self.enum_list)

    def _write_abstract_named_entity(self):
        """ This method generated AbstractNamedEntity class js file.
        """
        filename = "%sAbstractNamedEntity.js" % (self._class_prefix)
                
        superclass_name = "%sEntity" % (self._class_prefix)
        
        # write will write a file using a template.
        # mandatory params: destination directory, destination file name, template file name
        # optional params: whatever that is needed from inside the Jinja template

        self.write(destination = self.abstract_directory,
                    filename = filename,
                    template_name = "abstract_named_entity.js.tpl",
                    class_prefix = self._class_prefix,
                    superclass_name = superclass_name)
                    
    def _write_model(self, specification):
        """ This method writes the ouput for a particular specification.
        """
        filename = "%s%s.js" % (self._class_prefix, specification.entity_name)

        isNamedEntity = self._isNamedEntity(attributes=specification.attributes)
                
        superclass_name = "RootEntity" if specification.rest_name == self.api_root else "AbstractNamedEntity" if isNamedEntity  else "Entity"
        # write will write a file using a template.
        # mandatory params: destination directory, destination file name, template file name
        # optional params: whatever that is needed from inside the Jinja template

        specification.attributes = [attribute for attribute in specification.attributes if (attribute.name not in base_attrs and (not isNamedEntity or attribute.name not in named_entity_attrs))]

        enum_attributes=[attribute for attribute in specification.attributes if attribute.allowed_choices]
            
        self._write_enums(entity_name=specification.entity_name, attributes=enum_attributes)
        
        self.write(destination = self.output_directory,
                    filename = filename,
                    template_name = "entity.js.tpl",
                    class_prefix = self._class_prefix,
                    specification = specification,
                    superclass_name = superclass_name,
                    enum_attrs_to_import = enum_attributes)

    def _isNamedEntity(self, attributes):
        hasName = False
        hasDescription = False
        for attribute in attributes:
            if attribute.name == "name":
                hasName = True
            elif attribute.name == "description":
                hasDescription = True        
        return hasName and hasDescription
    
    def _write_enums(self, entity_name, attributes):
        """ This method writes the ouput for a particular specification.
        """

        for attribute in attributes:
            enum_name = "%s%sEnum" % (entity_name, attribute.name[0].upper() + attribute.name[1:])
            self.enum_list.append(enum_name)
            filename = "%s%s.js" % (self._class_prefix, enum_name)
            self.write(destination = self.enum_directory,
                        filename=filename,
                        template_name="enum.js.tpl",
                        class_prefix = self._class_prefix,
                        enum_name = enum_name,
                        allowed_choices = attribute.allowed_choices)
