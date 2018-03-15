import { Enum } from 'enumify';

class {{ class_prefix }}{{ enum_name }} extends Enum {

    static getClassName() {
        return '{{ class_prefix }}{{ enum_name }}';
    }

    getClassName() {
        return {{ class_prefix }}{{ enum_name }}.getClassName();
    }
}
{% set init_str %}{{ class_prefix }}{{ enum_name }}.initEnum([{% for choice in allowed_choices %}{% if loop.index0 > 0 %}, {% endif %}'{{choice}}'{% endfor %}]);{%- endset %}
{{ init_str|wordwrap(96,false,'\n    ')}}

export default {{ class_prefix }}{{ enum_name }};

