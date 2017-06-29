import NUAttribute from '../service/NUAttribute';
import NUEntity from '../service/NUEntity';
import ServiceClassRegistry from '../service/ServiceClassRegistry';


/* Represents {{ specification.entity_name }} entity
   {{ specification.description }}
*/
export default class {{ class_prefix }}{{ specification.entity_name }} extends {{ superclass_name }} {
    constructor(...args) {
        super(...args);
        this.defineProperties({
        {%- for attribute in specification.attributes %}
            {{ attribute.name }}: {% if attribute.default_value %}{{ attribute.default_value }}{% else %}null{% endif %},
        {%- endfor %}
        });
    }

    static attributeDescriptors = {
        ...NUEntity.attributeDescriptors,
        {%- for attribute in specification.attributes %}
        {{ attribute.name }}: new NUAttribute({
            localName: '{{ attribute.name }}',
            attributeType: NUAttribute.ATTR_TYPE_{% if attribute.local_type == "str" %}STRING{% elif attribute.local_type == "bool" %}BOOLEAN{% else %}NUMBER{% endif %}{% if attribute.required %},
            isRequired: true{% endif %}{% if attribute.unique %},
            isUnique: true{% endif %}{% if attribute.creation_only %},
            isReadOnly: true{% endif %}{% if attribute.read_only %},
            isEditable: false{% endif %}{% if attribute.orderable %},
            canOrder: true{% endif %}{% if attribute.filterable %},
            canSearch: true{% endif %}{% if attribute.allowed_choices and attribute.allowed_choices|length > 0  %},
            choices: [{% for choice in attribute.allowed_choices %}{% if loop.index0 > 0 %}, {% endif %}'{{choice}}'{% endfor %}]{% endif %},
        }),
        {%- endfor %}
    }

    get RESTName() {
        return '{{ specification.resource_name }}';
    }
}

ServiceClassRegistry.register({{ class_prefix }}{{ specification.entity_name }});

