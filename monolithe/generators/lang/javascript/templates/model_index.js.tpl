export { default as {{ class_prefix }}AbstractNamedEntity } from './abstract/{{ class_prefix }}AbstractNamedEntity';
{%- for model in model_list %}
{%- set export_str %}export { default as {{ model }} } from './{{ model }}';{%- endset %}
{{ export_str|wordwrap(96,false,'\n    ')}}
{%- endfor %}

