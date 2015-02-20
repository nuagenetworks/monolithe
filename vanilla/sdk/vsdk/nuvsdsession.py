# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.

from bambou import NURESTLoginController
from nurestuser import NURESTUser
from .utils import *


class NUVSDSession(object):
    """ VSD User Session

        Session can be started and stopped whenever its needed
    """

    def __init__(self, username, password, enterprise, api_url):
        """ Initializes a new user sesssion on the VSD

            Notes:
                This session will enable to access the VSD Api using
                its user. Use session.user to retrieve the user that is currently
                logged in.

            Args:
                username (str): username to login to the VSD
                password (str): username associated password
                enterprise (str): name of the enterprise
                api_url (str): API Url of the VSD

            Example:
                >>> session = NUVSDSession(username=u'john', password=u'doe', enterprise=u'My Company', api_url=u'https://.../nuage/api/v3_1')
        """

        self._username = username
        self._password = password
        self._enterprise = enterprise
        self._api_url = api_url
        self._user = None

    def _get_user(self):
        """ Get the user for the current session

            Returns:
                vsdk.NURESTUser: the user
        """
        return self._user

    user = property(_get_user, None)

    def start(self):
        """ Start the VSD Session with the given user

            Notes:
                Authenticate the user and set the API Key that will be
                used for HTTP/s requests.

                All calls between start() and stop() will be made with the
                current user.

            Examples:
                >>> session.start()
                >>> # session.user is the active user
                >>> session.stop()

        """

        controller = NURESTLoginController()

        if controller.api_key is not None:
            vsdk_logger.warn("[NUVSDSession] Previous session has not been terminated.\
                            Please call stop() on your previous VSD Session to stop it properly")

        if self._user is None:
            # User has never been retrieved.
            # Start the controller and log in with the user
            # Set up the API Key
            controller.reset()  # Force cleaning previous session
            controller.user = self._username
            controller.password = self._password
            controller.enterprise = self._enterprise
            controller.url = self._api_url

            self._user = NURESTUser()
            self._user.fetch()

        controller.api_key = self._user.api_key
        vsdk_logger.debug("[NUVSDSession] Started session with username %s in enterprise %s (key=%s)" % (self._username, self._password, self._user.api_key))

    def stop(self):
        """ Stop the VSD Session

            Notes:
                Release the API Key for the next session.
                Stop is automatically called when starting a new session.
        """

        controller = NURESTLoginController()
        controller.api_key = None
        vsdk_logger.debug("[NUVSDSession] Session with username %s in enterprise %s terminated." % (self._username, self._password))
