{%- for enum in enum_list %}
export { default as {{ class_prefix }}{{ enum }} } from './{{ class_prefix }}{{ enum }}';
{%- endfor %}

