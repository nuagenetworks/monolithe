# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.

from bambou import NURESTSession
from .nurestuser import NURESTUser


class NUVSDSession(NURESTSession):
    """ VSD User Session

        Session can be started and stopped whenever its needed
    """

    def create_rest_user(self):
        """ Creates a new user

        """
        return NURESTUser()
