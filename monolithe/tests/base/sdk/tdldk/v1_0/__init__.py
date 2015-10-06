# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#


__all__ = ['GAList', 'GARoot', 'GATask', 'GATDLSession']

from .galist import GAList
from .garoot import GARoot
from .gatask import GATask
from .gatdlsession import GATDLSession
from .sdkinfo import SDKInfo

def __setup_bambou():
    """ Avoid having bad behavior when using importlib.import_module method
    """
    import pkg_resources
    from bambou import BambouConfig, NURESTModelController

    default_attrs = pkg_resources.resource_filename(__name__, '/resources/attrs_defaults.ini')
    BambouConfig.set_default_values_config_file(default_attrs)

    NURESTModelController.register_model(GAList)
    NURESTModelController.register_model(GARoot)
    NURESTModelController.register_model(GATask)
    

__setup_bambou()