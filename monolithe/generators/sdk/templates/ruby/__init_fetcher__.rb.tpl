# -*- coding: utf-8 -*-
# Ruby
{{ header }}

__all__ = {{ filenames.values() }}
{% for filename, classname in filenames.iteritems() %}
from .{{ filename }} import {{ classname }}{% endfor %}

