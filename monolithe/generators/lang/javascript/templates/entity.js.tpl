import {{ class_prefix }}Attribute from 'service/{{ class_prefix }}Attribute';
import ServiceClassRegistry from 'service/ServiceClassRegistry';
import {{ class_prefix }}{{ superclass_name}} from '{% if superclass_name == "AbstractNamedEntity" %}./abstract/{% else %}service/{% endif %}{{ class_prefix }}{{ superclass_name }}';
{%- if enum_attrs_to_import and enum_attrs_to_import|length > 0  %}
{%- set import_str %}import { {% for attribute in enum_attrs_to_import %}{% if loop.index0 > 0 %}, {% endif %}{{ class_prefix }}{{ specification.entity_name }}{{ attribute.name[0].upper() + attribute.name[1:] }}Enum{% endfor %} } from './enums';{%- endset %}
{{ import_str|wordwrap(96,false,'\n    ')}}
{%- endif %}
{%- if generic_enum_attributes_to_import and generic_enum_attributes_to_import|length > 0 %}
{%- set import_str %}import { {% for attr in generic_enum_attributes_to_import %}{% if loop.index0 > 0 %}, {% endif %}{{ class_prefix }}{{ attr[0].upper() + attr[1:] }}Enum{% endfor %} } from './enums';{%- endset %}
{{ import_str|wordwrap(96,false,'\n    ')}}
{%- endif %}


/* Represents {{ specification.entity_name }} entity
{% if specification.description %}   {{ specification.description|wordwrap(97,false,'\n   ')}}{{'\n'}}{% endif -%}
*/
export default class {{ class_prefix }}{{ specification.entity_name }} extends {{ class_prefix }}{{ superclass_name }} {
    constructor(...args) {
        super(...args);
        this.defineProperties({
        {%- for attribute in specification.attributes %}
            {% set is_enum = attribute.allowed_choices and attribute.allowed_choices|length > 0  -%}
            {{ attribute.name }}: {% if attribute.default_value %}{% if attribute.local_type == "string" %}'{{ attribute.default_value }}'{% else %}{% if is_enum  %}{{ class_prefix }}{% set attr_name %}{% if attribute.name not in  generic_enum_attributes%}{{ attribute.name }}{% else %}{{ generic_enum_attributes[attribute.name].name }}{% endif %}{% endset %}{% if attribute.name not in  generic_enum_attributes%}{{ specification.entity_name }}{% endif %}{{ attr_name[0].upper() + attr_name[1:] }}Enum.{% endif %}{{ attribute.default_value }}{% if is_enum  %}.name{% endif %}{% endif %}{% else %}null{% endif %},
        {%- endfor %}
        });
    }

    static attributeDescriptors = {
        ...{{ class_prefix }}{{ superclass_name}}.attributeDescriptors,
        {%- for attribute in specification.attributes %}
        {{ attribute.name }}: new {{ class_prefix }}Attribute({
            localName: '{{ attribute.name }}',
            attributeType: {{ class_prefix }}Attribute.ATTR_TYPE_{% if attribute.local_type == "integer" %}INTEGER{% elif attribute.local_type == "float" %}FLOAT{% elif attribute.local_type == "list" %}LIST{% elif attribute.local_type == "boolean" %}BOOLEAN{% elif attribute.local_type == "enum" and attribute.allowed_choices and attribute.allowed_choices|length > 0 %}ENUM{% else %}STRING{% endif %}{% if attribute.required %},
            isRequired: true{% endif %}{% if attribute.unique %},
            isUnique: true{% endif %}{% if attribute.creation_only %},
            isReadOnly: true{% endif %}{% if attribute.read_only %},
            isEditable: false{% endif %}{% if attribute.orderable %},
            canOrder: true{% endif %}{% if attribute.filterable %},
            canSearch: true{% endif %}{% if attribute.allowed_choices and attribute.allowed_choices|length > 0  %},
            {%- set choices_str %}[{% for choice in attribute.allowed_choices %}{% if loop.index0 > 0 %}, {% endif %}{{ class_prefix }}{% set attr_name %}{% if attribute.name not in  generic_enum_attributes%}{{ attribute.name }}{% else %}{{ generic_enum_attributes[attribute.name].name }}{% endif %}{% endset %}{% if attribute.name not in  generic_enum_attributes%}{{ specification.entity_name }}{% endif %}{{ attr_name[0].upper() + attr_name[1:] }}Enum.{{choice}}{% endfor %}]{%- endset %}
            choices: {{choices_str|wordwrap(80,false,'\n                ')}}{% endif %},{% if attribute.local_type == "list" %}
            subType: {{ class_prefix }}Attribute.ATTR_TYPE_{% if attribute.subtype == "integer" %}INTEGER{% elif attribute.subtype == "float" %}FLOAT{% elif attribute.subtype == "boolean" %}BOOLEAN{% elif attribute.subtype == "enum" and attribute.allowed_choices and attribute.allowed_choices|length > 0 %}ENUM{% else %}STRING{% endif %},{% endif %}
            userlabel: '{{ attribute.userlabel }}',
        }),
        {%- endfor %}
    }

    get RESTName() {
        return '{{ specification.resource_name }}';
    }
}

ServiceClassRegistry.register({{ class_prefix }}{{ specification.entity_name }});

