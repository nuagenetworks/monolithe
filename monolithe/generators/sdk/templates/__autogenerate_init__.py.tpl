# -*- coding: utf-8 -*-
{{ header }}

{% set classnames = [] %}
{% for filename, classname in filenames.iteritems() %}
{% do classnames.append('"' + sdk_class_prefix + classname + '"') %}from .{{ filename[:-3]}} import {{ sdk_class_prefix }}{{ classname }}{% endfor %}

__all__ = [{{ ', '.join(classnames)}}]