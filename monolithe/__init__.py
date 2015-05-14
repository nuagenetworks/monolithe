# -*- coding: utf-8 -*-

__all__ = ['Command', 'APIValidator']

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

from .command import Command
from .specsvalidator.apivalidator import APIValidator
