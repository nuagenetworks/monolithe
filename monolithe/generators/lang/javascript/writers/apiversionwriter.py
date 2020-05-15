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
        
        self.locale_on = monolithe_config.get_option("locale", "transformer", fallback=True)
        self.model_directory = "%s/javascript/%s/models" % (output, api_info["version"])
        self.abstract_directory =  "%s/abstract" % self.model_directory
        self.enum_directory =  "%s/enums" % self.model_directory
        self.locale_directory = "%s/javascript/%s/locales/en" % (output, api_info["version"])

        if os.path.exists(self.model_directory):
            shutil.rmtree(self.model_directory)

        if os.path.exists(self.locale_directory):
            shutil.rmtree(self.locale_directory)

        self.api_root = api_info["root"]
        self._class_prefix = monolithe_config.get_option("class_prefix", "transformer")
        
        self._read_config()


    def _read_config(self):
        """ This method reads provided json config file.
        """
        
        this_dir = os.path.dirname(__file__)        
        config_file = os.path.abspath(os.path.join(this_dir, "..", "config", "config.json"))

        self.generic_enum_attrs = []
        self.base_attrs = []
        self.generic_enums = []
        self.named_entity_attrs = []
        self.overide_generic_enums = []
        self.enum_attrs_for_locale = {}
        self.generic_enum_attrs_for_locale = {}
        self.list_subtypes_generic = []
        
        Printer.log("Configuration file: %s" % (config_file))

        if (os.path.isfile(config_file)):
            with open(config_file, 'r') as input_json:
                json_config_data = json.load(input_json) 
                
            self.base_attrs = json_config_data['base_attrs']
            self.generic_enums =  json_config_data['generic_enums']
            self.named_entity_attrs = json_config_data['named_entity_attrs']
            self.overide_generic_enums = json_config_data['overide_generic_enums']
            self.list_subtypes_generic = json_config_data['list_subtypes_generic']

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
        self.enum_list = []
        self.model_list = []
        self.job_commands = filter(lambda attr: attr.name == 'command', specifications.get("job").attributes)[0].allowed_choices
        #Printer.log("job_commands: %s" % (self.job_commands))
            
        self._write_abstract_named_entity()
        
        self.entity_names = [specification.entity_name for rest_name, specification in specifications.iteritems()]

        for rest_name, specification in specifications.iteritems():
            self._write_model(specification=specification)

        #self._write_generic_enums()
        
        self.write(destination = self.model_directory,
            filename="index.js",
            template_name="model_index.js.tpl",
            class_prefix = self._class_prefix,
            model_list = sorted(self.model_list))
            
        self.write(destination = self.enum_directory,
                    filename="index.js",
                    template_name="enum_index.js.tpl",
                    class_prefix = self._class_prefix,
                    enum_list = sorted(self.enum_list))
                    
        self._write_locales(specifications)            

    def _write_locales(self, specifications):
        if self.locale_on:
            self.locales_list = []
            for rest_name, specification in specifications.items():
                self._format_description_text(specification)            
                filename = "%s.json" % (rest_name)
                self.locales_list.append(rest_name)
                self.write(destination = self.locale_directory,
                    filename=filename,
                    template_name="locale_entity.json.tpl",
                    specification = specification,
                    enum_attrs = {})
                    
            self.write(destination = self.locale_directory,
                filename="index.js",
                template_name="locales_index.js.tpl",
                locales_list = sorted(self.locales_list))
            
    def _format_description_text(self, specification):
        if specification.description:
            specification.description = specification.description.replace('"', "'")  
            
        for attribute in specification.attributes:
            if attribute.description:
                attribute.description = attribute.description.replace('"', "'")

    def _write_abstract_named_entity(self):
        """ This method generates AbstractNamedEntity class js file.
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
        
        if specification.allowed_job_commands and not (set(specification.allowed_job_commands).issubset(self.job_commands)):
            raise Exception("Invalid allowed_job_commands %s specified in entity %s" % (specification.allowed_job_commands, specification.entity_name))
            
        specification.supportsAlarms = len(filter(lambda child_api : child_api.rest_name == "alarm", specification.child_apis)) == 1
        
        specification.supportsPermissions = len(filter(lambda child_api : child_api.rest_name == "enterprisepermission" or child_api.rest_name == "permission", specification.child_apis)) > 0

        specification.supportsDeploymentFailures = len(filter(lambda child_api : child_api.rest_name == "deploymentfailure", specification.child_apis)) == 1

        filename = "%s%s.js" % (self._class_prefix, specification.entity_name)

        self.model_list.append("%s%s" %(self._class_prefix, specification.entity_name))
        
        isNamedEntity = self._isNamedEntity(attributes=specification.attributes) if specification.rest_name else False
                
        superclass_name = "RootEntity" if specification.rest_name == self.api_root else "AbstractNamedEntity" if isNamedEntity  else "AbstractModel" if not specification.rest_name else "Entity"
        # write will write a file using a template.
        # mandatory params: destination directory, destination file name, template file name
        # optional params: whatever that is needed from inside the Jinja template

        specification.attributes_modified = [attribute for attribute in specification.attributes if (attribute.name not in self.base_attrs and (not isNamedEntity or attribute.name not in self.named_entity_attrs))]

        enum_attributes=[attribute for attribute in specification.attributes_modified if attribute.allowed_choices]
                
        enum_attrs_to_import = enum_attributes[:]
        generic_enum_attrs_in_entity = {}
        generic_enum_attributes_to_import = []

        for attr in enum_attributes:
            if attr.local_type == "list" and attr.subtype == "enum" and attr.default_value:
                attr.default_value = attr.default_value.translate({ord(i): None for i in ' []"'}).split(",")
                if not all(defval in attr.allowed_choices for defval in attr.default_value):
                    raise Exception("Invalid default value specified for attribute %s in entity %s" % (attr.name, specification.entity_name))
                                        
            if specification.rest_name in self.overide_generic_enums and  attr.name in self.overide_generic_enums[specification.rest_name]:
                continue
            for generic_enum_attr in self.generic_enum_attrs:
                if set(attr.allowed_choices) & set(generic_enum_attr.allowed_choices):
                    generic_enum_attrs_in_entity[attr.name] = generic_enum_attr
                    enum_attrs_to_import.remove(attr)
                    generic_enum_attributes_to_import.append(generic_enum_attr.name)

        
        self._write_enums(entity_name=specification.entity_name, attributes=enum_attrs_to_import)

        self.generic_enum_attrs_for_locale[specification.entity_name] = generic_enum_attrs_in_entity.values()
        
        object_subtypes = set([attribute.subtype for attribute in specification.attributes if (attribute.local_type == "object"  and attribute.subtype and attribute.subtype not in self.list_subtypes_generic)])

        invalid_object_attributes=[attribute.name for attribute in specification.attributes_modified if (attribute.local_type == "object" and not attribute.subtype in self.entity_names)]

        if invalid_object_attributes:
            Printer.log("Spec: %s: Attributes %s use invalid subtypes %s" % (filename, invalid_object_attributes, object_subtypes))

        list_subtypes = set([attribute.subtype for attribute in specification.attributes if (attribute.local_type == "list" and attribute.subtype not in self.list_subtypes_generic)])

        invalid_list_attributes=[attribute.name for attribute in specification.attributes_modified if (attribute.local_type == "list" and not attribute.subtype in self.entity_names and not attribute.subtype in self.list_subtypes_generic)]

        if invalid_list_attributes:
            Printer.log("Spec: %s: Attributes %s use invalid list subtypes %s" % (filename, invalid_list_attributes, list_subtypes))

        if 'object' in list_subtypes:
            list_subtypes.remove('object')
        if 'entity' in list_subtypes:
            list_subtypes.remove('entity')

        self.write(destination = self.model_directory,
                    filename = filename,
                    template_name = "entity.js.tpl",
                    class_prefix = self._class_prefix,
                    specification = specification,
                    superclass_name = superclass_name,
                    enum_attrs_to_import = enum_attrs_to_import,
                    generic_enum_attributes = generic_enum_attrs_in_entity,
                    generic_enum_attributes_to_import = set(generic_enum_attributes_to_import),
                    subtypes_for_import = object_subtypes.union(list_subtypes))

    def _isNamedEntity(self, attributes):
        attr_names = [attr.name for attr in attributes]
        named_attrs_applicable = len(self.named_entity_attrs) > 0 and set(self.named_entity_attrs).issubset(attr_names)
        if (named_attrs_applicable):
            name_attr = filter(lambda attr: attr.name == 'name', attributes)[0]
            if ((not name_attr.required) or (not name_attr.filterable)):
                return False
            desc_attr = filter(lambda attr: attr.name == 'description', attributes)[0]
            if (desc_attr.required or (not desc_attr.filterable)):
                return False
            return True
        return False
    
    def _write_enums(self, entity_name, attributes):
        """ This method writes the ouput for a particular specification.
        """
        
        self.enum_attrs_for_locale[entity_name] = attributes;

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
