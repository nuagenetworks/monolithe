# -*- coding: utf-8 -*-
"""

NUVSDSession

Author Christophe Serafin <christophe.serafin@alcatel-lucent.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""

from bambou import NURESTLoginController
from nurestuser import NURESTUser
from .utils import *


class NUVSDSession(object):
    """ VSD User Session

        Session can be started and stopped whenever its needed
    """

    def __init__(self, username, password, enterprise, api_url):
        """ Initializes a new connection to the VSD

            Connection will enable to access the VSD Api using
            specific objects

            Args:
                username: the name of the user to connect with
                password: the password associated with the username
                enterprise: the name of the enterprise
                api_url: the API endpoint
        """

        self._username = username
        self._password = password
        self._enterprise = enterprise
        self._api_url = api_url
        self._user = None

    def _get_user(self):
        """ Returns the current user of the session

            Returns:
                A user represented as a NURESTUser
        """
        return self._user

    user = property(_get_user, None)

    def start(self):
        """ Start the current VSD Session

            Authenticate the user and set the API Key that will be
            used for HTTP/s requests
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
        """ Stop the current VSD Session

            Release the API Key for the next session
        """

        controller = NURESTLoginController()
        controller.api_key = None
        vsdk_logger.debug("[NUVSDSession] Session with username %s in enterprise %s terminated." % (self._username, self._password))
