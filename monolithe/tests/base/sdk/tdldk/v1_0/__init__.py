# -*- coding: utf-8 -*-
# TODO



from .galist import GAList
from .garoot import GARoot
from .gatask import GATask
from .gatdlsession import GATDLSession

__all__ = ["GAList", "GARoot", "GATask", 'GATDLSession']

import pkg_resources
from bambou import BambouConfig, NURESTModelController

default_attrs = pkg_resources.resource_filename(__name__, '/resources/attrs_defaults.ini')
BambouConfig.set_default_values_config_file(default_attrs)

NURESTModelController.register_model(GAList)
NURESTModelController.register_model(GARoot)
NURESTModelController.register_model(GATask)
