# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.
# NU{{ model.name }}
# {{ model.description }}

from .autogenerates import NU{{ model.name }} as AutoGenerate


class NU{{ model.name }}(AutoGenerate):
    """ Represents a NU{{ model.name }} object in the VSD

        See:
            vsdk.autogenerates.NU{{ model.name }}
    """

    def __init__(self, **kwargs):
        """ Initializes a NU{{ model.name }} instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> {{ model.name.lower() }} = NU{{ model.name }}(id=u'xxxx-xxx-xxx-xxx', name=u'{{ model.name }}')
                >>> {{ model.name.lower() }} = NU{{ model.name }}(data=my_dict)
        """

        super(NU{{ model.name }}, self).__init__(**kwargs)
{% if override_content %}
    {{ override_content.replace('\n', '\n    ') }}
{% endif %}
