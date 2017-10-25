{{ header }}

using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json.Converters;
using net.nuagenetworks.bambou;

using {{ package_name }}.fetchers;

namespace {{ package_name }}
{

public class {{ class_prefix }}{{ specification.entity_name }}: {{ superclass_name }} {

   private const long serialVersionUID = 1L;

   {% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) -%}
   {% if attribute.type == "enum" or attribute.subtype == "enum" %}
   {%- set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] %}
   public enum E{{ field_name }} { {%- for choice in attribute.allowed_choices %}{{ choice }}{% if not loop.last %},{% endif %}{% endfor %} };
   {%- endif %}
   {%- endfor %}

   {% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}
   {%- if attribute.type == "enum" %}[JsonConverter(typeof(StringEnumConverter))]{%- endif %}
   [JsonProperty("{{ attribute.name }}")]   
   {%- set field_name = attribute.local_type %}
   {%- if attribute.type == "enum" %}{%- set field_name="E"+attribute.local_type+"?" %}{%- endif %}
   {%- if attribute.local_type == "long" %}{%- set field_name=attribute.local_type+"?" %}{%- endif %}
   protected {{ field_name }} _{{ attribute.local_name }};
   {% endfor %}

   {% if specification.child_apis|length > 0 -%}
   {% for api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
   {%- set child_spec = specification_set[api.rest_name] %}
   [JsonIgnore]
   private {{ class_prefix }}{{ child_spec.instance_name_plural }}Fetcher _{{ child_spec.instance_name_plural[0:1].lower() + child_spec.instance_name_plural[1:] }};
   {% endfor %}
   {%- endif %}

{%- set add_warning = {} %}
{%- for attribute, value in attribute_defaults.iteritems() %}{% if value.startswith(attribute + '.') %}{% set _ = add_warning.update({'enabled' : True}) %}{% endif %}{% endfor %}
   public {{ class_prefix }}{{ specification.entity_name }}() {
      {% for attribute, value in attribute_defaults.iteritems() -%}
      _{{attribute}} = {{value}};
      {% endfor -%}

      {% if specification.child_apis|length > 0 -%}   
      {% for api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
      {%- set child_spec = specification_set[api.rest_name] %}
      _{{ child_spec.instance_name_plural[0:1].lower() + child_spec.instance_name_plural[1:] }} = new {{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher(this);
      {% endfor %}
      {%- endif %}
   }

   {% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %}
   {%- set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] -%}
   {%- set field_type = attribute.local_type %}
   {%- if attribute.type == "enum" %}{%- set field_type="E"+field_name+"?" %}{%- endif %}
   {%- if field_type == "long" %}{%- set field_type=field_type+"?" %}{%- endif %}
   [JsonIgnore]
   public {{ field_type }} NU{{ field_name }} {
      get {
         return _{{ attribute.local_name }};
      }
      set {
         this._{{ attribute.local_name }} = value;
      }
   }

   {% endfor %}

   {% if specification.child_apis|length > 0 -%}
   {% for api in specification.child_apis | sort(attribute='rest_name', case_sensitive=True) %}
   {%- set child_spec = specification_set[api.rest_name] %}
   public {{ class_prefix }}{{ child_spec.instance_name_plural }}Fetcher get{{ child_spec.entity_name_plural }}() {
      return _{{ child_spec.entity_name_plural[0:1].lower() + child_spec.entity_name_plural[1:] }};
   }
   {% endfor %}
   {%- endif %}

   public String toString() {
      return "{{ class_prefix }}{{ specification.entity_name }} ["{% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) %} + "{% if not loop.first %}, {% endif %}{{ attribute.local_name }}=" + _{{ attribute.local_name }}{% endfor %} + ", id=" + NUId + ", parentId=" + NUParentId + ", parentType=" + NUParentType + ", creationDate=" + NUCreationDate + ", lastUpdatedDate="
              + NULastUpdatedDate + ", owner=" + NUOwner {% if superclass_name == "RestRootObject" %} + ", apiKey=" + apiKey {% endif %} + "]";
   }
   
   {% if override_content -%}
   {{ override_content.replace('\n', '\n   ') }}
   {%- endif %}

   public static String getResourceName()
   {
	return "{{ specification.resource_name }}";
   }

   public static String getRestName()
   {
	return "{{ specification.rest_name }}";
   }
}
}
