{   
    "en": { {% for enum_name, allowed_choices in enum_attrs_for_locale_template.iteritems() %}
        "{{ enum_name }}": { {% for choice in allowed_choices %}
            "{{ choice }}": "{{ choice }}"{% if not loop.last %},{% endif %}{% endfor %}
        }{% if not loop.last %},{% endif %}{% endfor %}
    }
}

