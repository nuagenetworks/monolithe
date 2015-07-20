# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.

from bambou import NURESTSession
from .nurestuser import NURESTUser


class NUVSDSession(NURESTSession):
    """ VSD User Session

        Session can be started and stopped whenever its needed
    """

    def __init__(self, username, password, enterprise, api_url):
        """ Initializes a new sesssion

            Args:
                username (string): the username
                password (string): the password
                enterprise (string): the enterprise
                api_url (string): the url to the api

            Example:
                >>> session =  NUVSDSession(username="csproot", password="csproot", enterprise="csp", api_url="https://vsd:8443")
                >>> session.start()

        """
        super(NUVSDSession, self).__init__(username=username, password=password, enterprise=enterprise, api_url=api_url, version=str(self.version))

    def create_rest_user(self):
        """ Creates a new user

        """
        return NURESTUser()

    @property
    def version(self):
        """ Returns the current VSD version

        """
        return {{ version }}
