from monolithe.generators.lib import TemplateFileWriter
from monolithe.specifications import SpecificationAttribute
from monolithe.lib import Printer
import os
import shutil
import json


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
        
        self._read_config()


    def _read_config(self):
        """ This method reads provided json config file.
        """
        
        this_dir = os.path.dirname(__file__)        
        config_file = os.path.abspath(os.path.join(this_dir, "..", "..", "..", "..", "..", "config", "config.json"))

        self.generic_enum_attrs = []
        self.base_attrs = []
        self.generic_enums = []
        self.named_entity_attrs = []
        self.overide_generic_enums = []
        
        Printer.log("Configuration file: %s" % (config_file))

        if (os.path.isfile(config_file)):
            with open(config_file, 'r') as input_json:
                json_config_data = json.load(input_json) 
                
            self.base_attrs = json_config_data['base_attrs']
            self.generic_enums =  json_config_data['generic_enums']
            self.named_entity_attrs = json_config_data['named_entity_attrs']
            self.overide_generic_enums = json_config_data['overide_generic_enums']

            for enum_name, values in self.generic_enums.iteritems():
                enum_attr =  SpecificationAttribute()
                enum_attr.name = enum_name
                enum_attr.allowed_choices = values
                self.generic_enum_attrs.append(enum_attr)
        else:
            Printer.log("Configuration file missing: %s" % (config_file))
        
        
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

        specification.attributes = [attribute for attribute in specification.attributes if (attribute.name not in self.base_attrs and (not isNamedEntity or attribute.name not in self.named_entity_attrs))]

        enum_attributes=[attribute for attribute in specification.attributes if attribute.allowed_choices]
                
        enum_attrs_to_import = enum_attributes[:]
        generic_enum_attrs_in_entity = {}
        generic_enum_attributes_to_import = []

        for attr in enum_attributes:
            if specification.rest_name in self.overide_generic_enums and  attr.name in self.overide_generic_enums[specification.rest_name]:
                continue
            for generic_enum_attr in self.generic_enum_attrs:
                if set(attr.allowed_choices) & set(generic_enum_attr.allowed_choices):
                    generic_enum_attrs_in_entity[attr.name] = generic_enum_attr
                    enum_attrs_to_import.remove(attr)
                    generic_enum_attributes_to_import.append(generic_enum_attr.name)

        
        self._write_enums(entity_name=specification.entity_name, attributes=enum_attrs_to_import)

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
        attr_names = [attr.name for attr in attributes]
        return (len(self.named_entity_attrs) > 0 and set(self.named_entity_attrs).issubset(attr_names))
    
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

        self._write_enums(entity_name='', attributes=self.generic_enum_attrs)
