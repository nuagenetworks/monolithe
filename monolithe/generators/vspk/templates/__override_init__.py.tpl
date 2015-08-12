# -*- coding: utf-8 -*-
{% set classnames = [] %}
{% for filename, classname in filenames.iteritems() %}
{% do classnames.append('"NU' + classname + '"') %}from .{{filename[:-3]}} import NU{{classname}}{% endfor %}
from .utils import set_log_level
from .nuvsdsession import NUVSDSession

__all__ = [{{ ', '.join(classnames)}}, 'set_log_level', 'NUVSDSession']

import pkg_resources
from bambou import BambouConfig, NURESTModelController

default_attrs = pkg_resources.resource_filename(__name__, '/resources/attrs_defaults.ini')
BambouConfig.set_default_values_config_file(default_attrs)

{% for filename, classname in filenames.iteritems() %}NURESTModelController.register_model(NU{{classname}})
{% endfor %}