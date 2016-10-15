{%- set entity_param_name = specification.instance_name[0:1].lower() + specification.instance_name[1:] + "Obj" -%}
{%- set entity_type_name = name.upper() + ':' + specification.entity_name -%}
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<dunes-script-module name="{{ action_name }}" result-type="{{ attribute.workflow_type }}" api-version="6.0.0"  id="{{ action_id }}"  version="{{ workflow_version }}"  allowed-operations="vef" ><param n="{{ entity_param_name }}" t="{{ entity_type_name }}"></param><script encoded='false'><![CDATA[return {{ entity_param_name }}.{{ attribute.local_name }};]]></script>
</dunes-script-module>