# -*- coding: utf-8 -*-
{{ header }}

{% set classnames = [] %}
{% for filename, classname in filenames.iteritems() %}
{% do classnames.append('"' + sdk_class_prefix + classname + 'Fetcher"') %}from .{{ filename[:-3]}} import {{ sdk_class_prefix }}{{ classname }}Fetcher{% endfor %}

__all__ = [{{ ', '.join(classnames)}}]