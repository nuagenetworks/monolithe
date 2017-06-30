import { Enum } from 'enumify';

class {{ class_prefix }}{{ enum_name }} extends Enum {}
{{ class_prefix }}{{ enum_name }}.initEnum([{% for choice in allowed_choices %}{% if loop.index0 > 0 %}, {% endif %}'{{choice}}'{% endfor %}]);

export default {{ class_prefix }}{{ enum_name }};

