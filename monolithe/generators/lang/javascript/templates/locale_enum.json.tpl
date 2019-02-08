{
    "{{ class_prefix }}{{ enum_name }}": {
        {%- for choice in allowed_choices %}
        "{{ choice }}": "{{ choice }}"{% if not loop.last %},{% endif %}{% endfor %}
    }
}

