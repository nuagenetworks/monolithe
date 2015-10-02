# -*- coding: utf-8 -*-
{{ header }}

{% for name, constant_values in constants.iteritems() %}
class {{ name }}(object):
    """ {{ name }} """

    {% for key, value in constant_values.iteritems() %}{{ key.upper()}} = u"{{ value.upper()}}"
    {% endfor %}
{% endfor %}