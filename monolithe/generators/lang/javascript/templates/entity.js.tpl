{% set new_line = "\n"  -%}
{% if specification.attributes_modified -%}import {{ class_prefix }}Attribute from 'service/{{ class_prefix }}Attribute';{{ new_line }}{%- endif -%}
{% if specification.rest_name -%}import ServiceClassRegistry from 'service/ServiceClassRegistry';{{ new_line }}{% endif -%}
import {{ class_prefix }}{{ superclass_name}} from '{% if superclass_name == "AbstractNamedEntity" %}./abstract/{% else %}service/{% endif %}{{ class_prefix }}{{ superclass_name }}';
{%- if enum_attrs_to_import and enum_attrs_to_import|length > 0  %}
{%- set import_str %}import { {% for attribute in enum_attrs_to_import %}{% if loop.index0 > 0 %}, {% endif %}{{ class_prefix }}{{ specification.entity_name }}{{ attribute.name[0].upper() + attribute.name[1:] }}Enum{% endfor %} } from './enums';{%- endset %}
{{ import_str|wordwrap(96,false,'\n    ')}}
{%- endif %}
{%- if generic_enum_attributes_to_import and generic_enum_attributes_to_import|length > 0 %}
{%- set import_str %}import { {% for attr in generic_enum_attributes_to_import %}{% if loop.index0 > 0 %}, {% endif %}{{ class_prefix }}{{ attr[0].upper() + attr[1:] }}Enum{% endfor %} } from '@/enums';{%- endset %}
{{ import_str|wordwrap(96,false,'\n    ')}}
{%- endif %}
{%- if specification.allowed_job_commands %}
import { {{ class_prefix }}JobCommandEnum } from './enums';
{%- endif %}
{%- for subtype in subtypes_for_import %}
import {{ class_prefix }}{{ subtype }} from './{{ class_prefix }}{{ subtype }}';
{%- endfor %}


/* Represents {{ specification.entity_name }} entity
{% if specification.description %}   {{ specification.description|wordwrap(97,false,'\n   ')}}{{'\n'}}{% endif -%}
*/
export default class {{ class_prefix }}{{ specification.entity_name }} extends {{ class_prefix }}{{ superclass_name }} {
    constructor(...args) {
        super(...args);
        this.defineProperties({
        {%- if specification.template %}
            isTemplate: true,{% endif -%}
        {%- if specification.supportsDeploymentFailures %}
            hasDeploymentFailures: undefined,{% endif -%}
        {%- for attribute in specification.attributes_modified %}
            {% set is_enum = attribute.allowed_choices and attribute.allowed_choices|length > 0  -%}
            {% set is_enum_list = is_enum and attribute.local_type == "list" and attribute.default_value -%}
            {% set default_choices_str %}{% if is_enum_list %}[{% for defval in attribute.default_value %}{% if loop.index0 > 0 %}, {% endif %}{{ class_prefix }}{% set attr_name %}{% if attribute.name not in  generic_enum_attributes%}{{ attribute.name }}{% else %}{{ generic_enum_attributes[attribute.name].name }}{% endif %}{% endset %}{% if attribute.name not in  generic_enum_attributes%}{{ specification.entity_name }}{% endif %}{{ attr_name[0].upper() + attr_name[1:] }}Enum.{{defval}}.name{% endfor %}]{% else %}undefined{% endif %}{% endset -%}
            {{ attribute.name }}: {% if attribute.default_value and not attribute.read_only %}{% if attribute.local_type == "string" %}'{{ attribute.default_value }}'{% elif is_enum_list %}{{ default_choices_str }}{% else %}{% if is_enum  %}{{ class_prefix }}{% set attr_name %}{% if attribute.name not in  generic_enum_attributes%}{{ attribute.name }}{% else %}{{ generic_enum_attributes[attribute.name].name }}{% endif %}{% endset %}{% if attribute.name not in  generic_enum_attributes%}{{ specification.entity_name }}{% endif %}{{ attr_name[0].upper() + attr_name[1:] }}Enum.{% endif %}{{ attribute.default_value }}{% if is_enum  %}.name{% endif %}{% endif %}{% else %}undefined{% endif %},
        {%- endfor %}
        });
    }

    static entityDescriptor = {
        description: `{{ specification.description }}`,
        userlabel: `{{ specification.userlabel}}`,
    }

    static attributeDescriptors = {
        {%- if specification.rest_name -%}{{ new_line }}        ...{{ class_prefix }}{{ superclass_name}}.attributeDescriptors,{% endif -%}
        {%- for attribute in specification.attributes_modified %}
        {% set type_object_or_list_with_subtype = ((attribute.local_type == "object" and attribute.subtype  and attribute.subtype != "JSON") or (attribute.local_type == "list" and attribute.subtype and attribute.subtype in subtypes_for_import)) -%}
        {{ attribute.name }}: new {{ class_prefix }}Attribute({
            localName: '{{ attribute.name }}',
            attributeType: {{ class_prefix }}Attribute.ATTR_TYPE_{% if attribute.local_type == "time" %}TIMESTAMP{% elif attribute.local_type == "integer" %}INTEGER{% elif attribute.local_type == "object" %}OBJECT{% elif attribute.local_type == "float" %}FLOAT{% elif attribute.local_type == "list" %}LIST{% elif attribute.local_type == "boolean" %}BOOLEAN{% elif attribute.local_type == "enum" and attribute.allowed_choices and attribute.allowed_choices|length > 0 %}ENUM{% else %}STRING{% endif %}{% if attribute.description %},
            description: `{{ attribute.description }}`{% endif %}{% if attribute.required %},
            isRequired: true{% endif %}{% if attribute.unique %},
            isUnique: true{% endif %}{% if attribute.creation_only %},
            isCreateOnly: true{% endif %}{% if attribute.read_only %},
            isReadOnly: true{% endif %}{% if attribute.orderable %},
            canOrder: true{% endif %}{% if attribute.filterable %},
            canSearch: true{% endif %}{% if attribute.allowed_choices and attribute.allowed_choices|length > 0  %},
            {%- set choices_str %}[{% for choice in attribute.allowed_choices %}{% if loop.index0 > 0 %}, {% endif %}{{ class_prefix }}{% set attr_name %}{% if attribute.name not in  generic_enum_attributes%}{{ attribute.name }}{% else %}{{ generic_enum_attributes[attribute.name].name }}{% endif %}{% endset %}{% if attribute.name not in  generic_enum_attributes%}{{ specification.entity_name }}{% endif %}{{ attr_name[0].upper() + attr_name[1:] }}Enum.{{choice}}{% endfor %}]{%- endset %}
            choices: {{choices_str|wordwrap(80,false,'\n                ')}}{% endif %},{% if attribute.subtype != None %}
            subType: {{ class_prefix }}{% if type_object_or_list_with_subtype %}{{ attribute.subtype }},{% else %}Attribute.ATTR_TYPE_{% if attribute.subtype == "integer" %}INTEGER{% elif attribute.subtype == "JSON" %}OBJECT{% elif attribute.subtype == "long" %}LONG{% elif attribute.subtype == "float" %}FLOAT{% elif attribute.subtype == "boolean" %}BOOLEAN{% elif attribute.subtype == "enum" and attribute.allowed_choices and attribute.allowed_choices|length > 0 %}ENUM{% else %}STRING{% endif %},{% endif %}{% endif %}
            userlabel: `{{ attribute.userlabel }}`,
        }),
        {%- endfor %}
    }

    static getClassName() {
        return '{{ class_prefix }}{{ specification.entity_name }}';
    }
    
    {% if specification.rest_name -%}
    static getAllowedJobCommands() {
        {%- set commands_str %}{% if specification.allowed_job_commands %}[{% for command in specification.allowed_job_commands %}{% if loop.index0 > 0 %}, {% endif %}{{ class_prefix }}JobCommandEnum.{{command}}{% endfor %}]{% else %}[]{% endif %};{%- endset %}
        return {{commands_str|wordwrap(80,false,'\n                ')}}
    }
    
    static supportsAlarms() {
        return {% if specification.supportsAlarms %}true{% else %}false{% endif %};
    }
    
    {% if specification.supportsPermissions -%}
    static supportsPermissions() {
        return true;
    }
    
    {% endif -%}

    {% if specification.supportsDeploymentFailures -%}
    static supportsDeploymentFailures() {
        return true;
    }

    {% endif -%}

    static getInstanceFromID(ID) {
        const instance = new {{ class_prefix }}{{ specification.entity_name }}();
        instance.ID = ID;
        return instance;
    }
    
    get RESTName() {
        return '{{ specification.rest_name }}';
    }
    
    {% endif -%}
    
    {% if specification.resource_name -%}
    get resourceName() {
        return '{{ specification.resource_name }}';
    }
    
    {% endif -%}
    
    getClassName() {
        return {{ class_prefix }}{{ specification.entity_name }}.getClassName();
    }{{ new_line }}
    {%- if specification.rest_name %}
    getAllowedJobCommands() {
        return {{ class_prefix }}{{ specification.entity_name }}.getAllowedJobCommands();
    }{{ new_line }}{% endif -%}
}

{% if specification.rest_name -%}
ServiceClassRegistry.register({{ class_prefix }}{{ specification.entity_name }});
{% endif -%}