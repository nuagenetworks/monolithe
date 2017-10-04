from monolithe.generators.lib import TemplateFileWriter
from monolithe.specifications import SpecificationAttribute
import os
import shutil

base_attrs = ['entityScope', 'externalID', 'lastUpdatedBy']
named_entity_attrs = ['name', 'description']

iptype_enum_attr = SpecificationAttribute()
iptype_enum_attr.name = 'IPType'
iptype_enum_attr.allowed_choices = ['IPv4', 'IPv6', 'DUALSTACK', 'IPv4Network', 'IPv6Network']

enabled_enum_attr = SpecificationAttribute()
enabled_enum_attr.name = 'enabled'
enabled_enum_attr.allowed_choices = ['DISABLED', 'ENABLED', 'INHERITED', 'ENABLED_INHERITED']

permittedaction_enum_attr = SpecificationAttribute()
permittedaction_enum_attr.name = 'permittedAction'
permittedaction_enum_attr.allowed_choices = ['ALL', 'EXTEND', 'DEPLOY', 'READ', 'INSTANTIATE', 'USE']

generic_enum_attrs = [iptype_enum_attr, enabled_enum_attr, permittedaction_enum_attr]

class APIVersionWriter(TemplateFileWriter):
    """ This class is reponsible to write files for a particular api version. """

    def __init__(self, monolithe_config, api_info):

        super(APIVersionWriter, self).__init__(package="monolithe.generators.lang.javascript")

        output = monolithe_config.get_option("output", "transformer")

        self.model_directory = "%s/javascript/%s/models" % (output, api_info["version"])
        self.abstract_directory =  "%s/abstract" % self.model_directory
        self.enum_directory =  "%s/enums" % self.model_directory

        if os.path.exists(self.model_directory):
            shutil.rmtree(self.model_directory)

        self.api_root = api_info["root"]
        self._class_prefix = monolithe_config.get_option("class_prefix", "transformer")


    def perform(self, specifications):
        """ This method is the entry point of javascript code writer. Monolithe will call it when
        the javascript plugin is to generate code.
        """
        self.enum_list = [];
        self.model_list = [];

        self._write_abstract_named_entity()
        
        for rest_name, specification in specifications.iteritems():
            self._write_model(specification=specification)

        self._write_generic_enums()
        
        self.write(destination = self.model_directory,
            filename="index.js",
            template_name="model_index.js.tpl",
            class_prefix = self._class_prefix,
            model_list = self.model_list)
            
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

        self.model_list.append("%s%s" %(self._class_prefix, specification.entity_name))
        
        isNamedEntity = self._isNamedEntity(attributes=specification.attributes)
                
        superclass_name = "RootEntity" if specification.rest_name == self.api_root else "AbstractNamedEntity" if isNamedEntity  else "Entity"
        # write will write a file using a template.
        # mandatory params: destination directory, destination file name, template file name
        # optional params: whatever that is needed from inside the Jinja template

        specification.attributes = [attribute for attribute in specification.attributes if (attribute.name not in base_attrs and (not isNamedEntity or attribute.name not in named_entity_attrs))]

        enum_attributes=[attribute for attribute in specification.attributes if attribute.allowed_choices]
        
        self._write_enums(entity_name=specification.entity_name, attributes=enum_attributes)
        
        enum_attrs_to_import = enum_attributes[:]
        generic_enum_attrs_in_entity = {}
        generic_enum_attributes_to_import = []

        for attr in enum_attributes:
            for generic_enum_attr in generic_enum_attrs:
                if set(attr.allowed_choices) & set(generic_enum_attr.allowed_choices):
                    generic_enum_attrs_in_entity[attr.name] = generic_enum_attr
                    enum_attrs_to_import.remove(attr)
                    generic_enum_attributes_to_import.append(generic_enum_attr.name)
        
        self.write(destination = self.model_directory,
                    filename = filename,
                    template_name = "entity.js.tpl",
                    class_prefix = self._class_prefix,
                    specification = specification,
                    superclass_name = superclass_name,
                    enum_attrs_to_import = enum_attrs_to_import,
                    generic_enum_attributes = generic_enum_attrs_in_entity,
                    generic_enum_attributes_to_import = set(generic_enum_attributes_to_import))

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
                        allowed_choices = set(attribute.allowed_choices))

    def _write_generic_enums(self):
        """ This method generates generic enum classes.
        """

        self._write_enums(entity_name='', attributes=generic_enum_attrs)
