{%- for locale in locales_list %}
{%- set export_str %}export { default as {{ locale }} } from './{{ locale }}.json';{%- endset %}
{{ export_str|wordwrap(96,false,'\n    ')}}
{%- endfor %}