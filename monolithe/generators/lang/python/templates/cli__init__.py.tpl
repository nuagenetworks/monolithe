# -*- coding: utf-8 -*-
{{ header }}

import requests
import requests.packages.urllib3.exceptions as exceptions
requests.packages.urllib3.disable_warnings(exceptions.InsecureRequestWarning)
requests.packages.urllib3.disable_warnings()
