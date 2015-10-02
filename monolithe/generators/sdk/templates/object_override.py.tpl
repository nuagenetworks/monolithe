# -*- coding: utf-8 -*-
{{ header }}

from .autogenerates import {{ sdk_class_prefix }}{{ specification.name }} as AutoGenerate


class {{ sdk_class_prefix }}{{ specification.name }}(AutoGenerate):
    """ Represents a {{ sdk_class_prefix }}{{ specification.name }} object in the {{ product_accronym }}

        See:
            {{ sdk_name }}.autogenerates.{{ sdk_class_prefix }}{{ specification.name }}
    """

    def __init__(self, **kwargs):
        """ Initializes a {{ sdk_class_prefix }}{{ specification.name }} instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> {{ specification.name.lower() }} = {{ sdk_class_prefix }}{{ specification.name }}(id=u'xxxx-xxx-xxx-xxx', name=u'{{ specification.name }}')
                >>> {{ specification.name.lower() }} = {{ sdk_class_prefix }}{{ specification.name }}(data=my_dict)
        """

        super({{ sdk_class_prefix }}{{ specification.name }}, self).__init__(**kwargs)
{% if override_content %}
    {{ override_content.replace('\n', '\n    ') }}
{% endif %}
