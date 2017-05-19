{{ header }}

package {{ package_name }};

import net.nuagenetworks.vro.model.BaseConstants;

public interface Constants extends BaseConstants {
    String PLUGIN_NAME = "{{ name | upper }}";
    String PLUGIN_DESCRIPTION = "{{ name | upper }} Plug-in for vRealize Orchestrator";
    String PLUGIN_ROOT = "{{ name | upper }}";
    String PLUGIN_CONFIG_FILENAME = "{{ name | lower }}";
    
    {% for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
    String {{ specification.entity_name | upper }} = "{{ specification.entity_name }}";
    {% if not specification.entity_name_plural == specification.entity_name -%}
    String {{ specification.entity_name_plural | upper }} = "{{ specification.entity_name_plural }}";
    {%- endif %}
    {%- endfor %}

    {% for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
    String {{ specification.entity_name_plural | upper }}_FETCHER = "{{ specification.entity_name_plural }}Fetcher";
    {%- endfor %}

    {% for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
    {% for attribute in specification.attributes | sort(attribute='local_name', case_sensitive=True) -%}
    {% if attribute.type == "enum" or attribute.subtype == "enum" -%}
    {%- set field_name = attribute.local_name[0:1].upper() + attribute.local_name[1:] %}
    String {{ specification.entity_name | upper }}_{{ attribute.local_name | upper }}_ENUM = "{{ specification.entity_name }}{{ field_name }}";
    {%- endif %}
    {%- endfor %}
    {%- endfor %}
    
    {% for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
    String {{ specification.entity_name | upper }}_IMAGE_FILENAME = "images/icon-{{ specification.entity_name | lower }}.png";
    {%- endfor %}
    String FOLDER_IMAGE_FILENAME = "images/icon-folder.png";

    {% for specification in specifications | sort(attribute='rest_name', case_sensitive=True) %}
    String {{ specification.entity_name | upper }}_ENTITY_TYPE = "{{ specification.rest_name }}";
    {%- endfor -%}
}