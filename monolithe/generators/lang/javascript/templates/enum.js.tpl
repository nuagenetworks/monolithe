import { Enum } from 'enumify';

class {{ class_prefix }}{{ enum_name }} extends Enum {}
{%- set init_str %}{{ class_prefix }}{{ enum_name }}.initEnum([{% for choice in allowed_choices %}{% if loop.index0 > 0 %}, {% endif %}'{{choice}}'{% endfor %}]);{%- endset %}
{{ init_str|wordwrap(96,false,'\n    ')}}

export default {{ class_prefix }}{{ enum_name }};

