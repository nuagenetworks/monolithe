# -*- coding: utf-8 -*-
"""
Copyright 2014 Alcatel-Lucent USA Inc.
NUVSDSession
"""

from bambou import NURESTLoginController, NURESTSession
from nurestuser import NURESTUser
from .utils import vsdk_logger


class NUVSDSession(NURESTSession):

    def create_rest_user(self):
        return NURESTUser()
