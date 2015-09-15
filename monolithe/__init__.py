# -*- coding: utf-8 -*-

import requests
import requests.packages.urllib3.exceptions as exceptions
requests.packages.urllib3.disable_warnings(exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()


## Monkey patch to use PROTOCOL_TLSv1 by default in requests
from requests.packages.urllib3.poolmanager import PoolManager
import ssl
from functools import wraps


def sslwrap(func):
    @wraps(func)
    def bar(*args, **kw):
        kw['ssl_version'] = ssl.PROTOCOL_TLSv1
        return func(*args, **kw)
    return bar

PoolManager.__init__ = sslwrap(PoolManager.__init__)
## end of monkey patch

from ConfigParser import ConfigParser
import os

current_directory = os.path.dirname(os.path.realpath(__file__))
monolithe_config = ConfigParser()
monolithe_config.read('%s/../config.ini' % current_directory)

monolithe_mapping = ConfigParser()
monolithe_mapping.read('%s/../mappings.ini' % current_directory)
