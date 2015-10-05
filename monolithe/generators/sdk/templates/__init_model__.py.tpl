# -*- coding: utf-8 -*-
{{ header }}

{% set classnames = [] %}
{% for filename, classname in filenames.iteritems() | sort %}
{% do classnames.append('"' + sdk_class_prefix + classname + '"') %}from .{{ filename[:-3]}} import {{ sdk_class_prefix }}{{ classname }}{% endfor %}
from .{{ sdk_class_prefix|lower }}{{ product_accronym|lower }}session import {{ sdk_class_prefix }}{{ product_accronym }}Session

__all__ = [{{ ', '.join(classnames)}}, '{{ sdk_class_prefix }}{{ product_accronym }}Session']

import pkg_resources
from bambou import BambouConfig, NURESTModelController

default_attrs = pkg_resources.resource_filename(__name__, '/resources/attrs_defaults.ini')
BambouConfig.set_default_values_config_file(default_attrs)

{% for filename, classname in filenames.iteritems()|sort %}NURESTModelController.register_model({{ sdk_class_prefix }}{{ classname }})
{% endfor %}