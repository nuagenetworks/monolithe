# -*- coding: utf-8 -*-

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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
