# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#

__all__ = ['GATDLSession', 'GAList', 'GAMetadata', 'GARoot', 'GATask', 'GAUser']

from .galist import GAList
from .gametadata import GAMetadata
from .garoot import GARoot
from .gatask import GATask
from .gauser import GAUser
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
    NURESTModelController.register_model(GAMetadata)
    NURESTModelController.register_model(GARoot)
    NURESTModelController.register_model(GATask)
    NURESTModelController.register_model(GAUser)
    

__setup_bambou()