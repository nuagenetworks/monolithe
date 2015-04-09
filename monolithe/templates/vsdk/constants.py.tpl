# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.

{% for name, constant_values in constants.iteritems() %}
class {{ name }}(object):
    """ {{ name }} """

    {% for key, value in constant_values.iteritems() %}{{key.upper()}} = u"{{value.upper()}}"
    {% endfor %}
{% endfor %}