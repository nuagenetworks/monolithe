{   
    "en": { {% for rest_name, specification in specifications.items() %}
        "{{ specification.rest_name }}": {
            "entity": {
                "title": "{{ specification.userlabel }}",
                "description": "{{ specification.description}}"
            }{% if specification.attributes %},{% endif %}
       {%- for attribute in specification.attributes %}
            "{{ attribute.name }}":{
               "label": "{{ attribute.userlabel }}",
               "tooltip": "{{ attribute.description }}"
            }{% if not loop.last %},{% endif %}{% endfor %}
        }{% if not loop.last %},{% endif %}{% endfor %}
    }
}

