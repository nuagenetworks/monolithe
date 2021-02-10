# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#

from builtins import str
from bambou import NURESTSession
from bambou.exceptions import InternalConsitencyError
from .garoot import GARoot


class GATDLSession(NURESTSession):
    """ TDL User Session

        Session can be started and stopped whenever its needed
    """

    def __init__(self, username, enterprise, api_url, password=None, certificate=None):
        """ Initializes a new sesssion

            Args:
                username (string): the username
                password (string): the password
                enterprise (string): the enterprise
                api_url (string): the url to the api

            Example:
                >>> session =  GAtdlSession(username="csproot", password="csproot", enterprise="csp", api_url="https://TDL:8443")
                >>> session.start()

        """

        if certificate is None and password is None:
            raise InternalConsitencyError('GAtdlSession needs either a password or a certificate')

        super(GATDLSession, self).__init__(username=username, password=password, enterprise=enterprise, api_url=api_url, api_prefix="api", version=str(self.version), certificate=certificate)

    @property
    def version(self):
        """ Returns the current TDL version

        """
        return 1.0

    @property
    def root(self):
        """ Returns the root object

        """
        return self.root_object

    @classmethod
    def create_root_object(self):
        """ Returns a new instance

        """
        return GARoot()

    
    ## Custom methods
    @property
    def supercalifragilisticexpialidocious(self):
        """
            For obvious simplicity, you can use this property to get
            the root object
        """
        return self.root_object()
    