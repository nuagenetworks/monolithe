{%- set entity_param_name = specification.instance_name[0:1].lower() + specification.instance_name[1:] + "Obj" -%}
{%- set entity_type_name = name.upper() + ':' + specification.entity_name -%}
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workflow xmlns="http://vmware.com/vco/workflow" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://vmware.com/vco/workflow http://vmware.com/vco/workflow/Workflow-v4.xsd" root-name="item1" object-name="workflow:name=generic" id="{{ workflow_id }}"  version="{{ workflow_version }}" api-version="6.0.0" allowed-operations="vef" restartMode="1" resumeFromFailedMode="0" >
<display-name><![CDATA[{{ workflow_name }}]]></display-name>
<ref-types><![CDATA[({{ entity_type_name }})]]></ref-types>
<position x='100.0' y='50.0'/>
<input><param name='{{ entity_param_name }}' type='{{ entity_type_name }}' >
</param>
{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) -%}
{%- if (attribute.required or attribute.local_name in attrs_includes) and (not attribute.local_name in attrs_excludes) %}
<param name='{{ attribute.local_name }}' type='{{ attribute.workflow_type }}' >
</param>
{% endif -%}
{% endfor %}
</input><workflow-item name='item0' type='end' end-mode='0' >
<position x='384.5' y='45.40909090909091'/>
</workflow-item>
<workflow-item name='item1' out-name='item0' type='task' >
<display-name><![CDATA[Scriptable task]]></display-name>
<script encoded='false'><![CDATA[var session = {{ entity_param_name }}.session;

{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) -%}
{% if (attribute.required or attribute.local_name in attrs_includes) and (not attribute.local_name in attrs_excludes) -%}
{% if (attribute.workflow_type == "string") -%}
if ({{ attribute.local_name }}) {
   {{ entity_param_name }}.{{ attribute.local_name }} = {{ attribute.local_name }};
} else if ({{ entity_param_name }}.{{ attribute.local_name }}) {
   {{ entity_param_name }}.{{ attribute.local_name }} = "";
}
{% else -%}
{{ entity_param_name }}.{{ attribute.local_name }} = {{ attribute.local_name }};
{% endif -%}
{% endif -%}
{% endfor -%}

{{ entity_param_name }}.save(session, 1);]]></script>
<in-binding><bind name='{{ entity_param_name }}' type='{{ entity_type_name }}' export-name="{{ entity_param_name }}" ></bind>
{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) -%}
{%- if (attribute.required or attribute.local_name in attrs_includes) and (not attribute.local_name in attrs_excludes) %}
<bind name='{{ attribute.local_name }}' type='{{ attribute.workflow_type }}' export-name="{{ attribute.local_name }}" ></bind>
{% endif -%}
{% endfor %}
</in-binding><out-binding></out-binding><position x='204.5' y='55.40909090909091'/>
</workflow-item>
<presentation>
<p-param name="{{ entity_param_name }}"><desc><![CDATA[{{ entity_param_name }}]]></desc>
<p-qual name="contextualParameter" type="void" ><![CDATA[__NULL__]]></p-qual></p-param>
{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) -%}
{%- if (attribute.required or attribute.local_name in attrs_includes) and (not attribute.local_name in attrs_excludes) %}
<p-param name="{{ attribute.local_name }}"><desc><![CDATA[{{ attribute.local_name }}]]></desc>
<p-qual kind="ognl" name="defaultValue" type="{{ attribute.workflow_type }}" ><![CDATA[
{%- if attribute.type == "enum" or attribute.type == "list" -%}
GetAction("{{ package_name }}","get{{ specification.entity_name }}{{ attribute.local_name[0:1].upper() + attribute.local_name[1:] }}").call( #{{ entity_param_name }} )
{%- else -%}
#{{ entity_param_name }}.{{ attribute.local_name }}
{%- endif -%}
]]></p-qual></p-param>
{% endif -%}
{% endfor %}
</presentation></workflow>