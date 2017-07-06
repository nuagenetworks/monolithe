{%- for enum in enum_list %}
{%- set export_str %}export { default as {{ class_prefix }}{{ enum }} } from './{{ class_prefix }}{{ enum }}';{%- endset %}
{{ export_str|wordwrap(96,false,'\n    ')}}
{%- endfor %}

