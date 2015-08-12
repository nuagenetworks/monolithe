# -*- coding: utf-8 -*-
{% set classnames = [] %}
{% for filename, classname in filenames.iteritems() %}
{% do classnames.append('"NU' + classname + 'Fetcher"') %}from .{{filename[:-3]}} import NU{{classname}}Fetcher{% endfor %}

__all__ = [{{ ', '.join(classnames)}}]