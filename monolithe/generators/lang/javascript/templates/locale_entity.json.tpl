{
  {% if specification.rest_name %}  "{{ specification.rest_name }}"{% else %}  "{{ specification.entity_name|lower }}"{% endif %}: {
        "entity": {
            "title": "{{ specification.userlabel }}",
            "description": "{{ specification.description}}"
        }{% if specification.attributes %},{% endif %}
        {%- for attribute in specification.attributes %}
        "{{ attribute.name }}":{
           "label": "{{ attribute.userlabel }}",
           "tooltip": "{{ attribute.description }}"
        }{% if not loop.last %},{% endif %}{% endfor %}{% if enum_attrs %},{% endif %}{% for enum_name, allowed_choices in enum_attrs.iteritems() %}
        "{{ enum_name }}": { {% for choice in allowed_choices %}
            "{{ choice }}": "{{ choice }}"{% if not loop.last %},{% endif %}{% endfor %}
        }{% if not loop.last %},{% endif %}{% endfor %}
    }
}
