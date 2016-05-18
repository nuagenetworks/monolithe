# -*- coding: utf-8 -*-
{{ header }}

{% for api in specification.child_apis %}
{% set child_spec = specification_set[api.rest_name] %}
from .fetchers import {{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher
{% endfor %}
from bambou import {{ superclass_name }}


class {{ class_prefix }}{{ specification.entity_name }}({{ superclass_name }}):
    """ Represents a {{ specification.entity_name }} in the {{ product_accronym }}

        Notes:
            {{ specification.description }}
    """

    __rest_name__ = "{{ specification.rest_name }}"
    __resource_name__ = "{{ specification.resource_name }}"

    {% if constants|length %}
    ## Constants
    {% for name, constant_value in constants.items() %}
    {{ name }} = "{{ constant_value }}"
    {% endfor %}
    {% endif %}

    def __init__(self, **kwargs):
        """ Initializes a {{ specification.entity_name }} instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> {{ specification.entity_name.lower() }} = {{ class_prefix }}{{ specification.entity_name }}(id=u'xxxx-xxx-xxx-xxx', name=u'{{ specification.entity_name }}')
                >>> {{ specification.entity_name.lower() }} = {{ class_prefix }}{{ specification.entity_name }}(data=my_dict)
        """

        super({{ class_prefix }}{{ specification.entity_name }}, self).__init__()

        # Read/Write Attributes
        {% for attribute in specification.attributes %}
        self._{{ attribute.local_name|lower }} = None{% endfor %}
        {% for attribute in specification.attributes %}
        self.expose_attribute(local_name="{{ attribute.local_name|lower }}", remote_name="{{ attribute.name }}", attribute_type={{ attribute.local_type }}, is_required={{ attribute.required }}, is_unique={{ attribute.unique }}{% if attribute.allowed_choices and attribute.allowed_choices|length > 0  %}, choices={{ attribute.allowed_choices|sort|trim }}{% endif %}){% endfor %}
        {% if specification.child_apis|length > 0 %}

        # Fetchers
        {% for api in specification.child_apis %}
        {% set child_spec = specification_set[api.rest_name] %}
        self.{{ child_spec.instance_name_plural }} = {{ class_prefix }}{{ child_spec.entity_name_plural }}Fetcher.fetcher_with_object(parent_object=self, relationship="{{api.relationship}}")
        {% endfor %}{% endif %}

        self._compute_args(**kwargs)

    # Properties
    {% for attribute in specification.attributes %}
    @property
    def {{ attribute.local_name }}(self):
        """ Get {{ attribute.local_name }} value.

            Notes:
                {{ attribute.description }}

                {% if attribute.local_name != attribute.name %}
                This attribute is named `{{ attribute.name }}` in {{ product_accronym }} API.
                {% endif %}
        """
        return self._{{ attribute.local_name }}

    @{{ attribute.local_name }}.setter
    def {{ attribute.local_name }}(self, value):
        """ Set {{ attribute.local_name }} value.

            Notes:
                {{ attribute.description }}

                {% if attribute.local_name != attribute.name %}
                This attribute is named `{{ attribute.name }}` in {{ product_accronym }} API.
                {% endif %}
        """
        self._{{ attribute.local_name }} = value

    {% endfor %}

    {% if override_content %}
    ## Custom methods
    {{ override_content.replace('\n', '\n    ') }}
    {% endif %}
