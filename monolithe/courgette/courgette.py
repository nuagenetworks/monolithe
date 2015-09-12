# -*- coding: utf-8 -*-

from monolithe.lib import Printer

from monolithe.courgette.lib import TestsRunner


class Courgette(object):
    """ Validates API by launching specification-generated tests

    """
    def __init__(self, vsdurl, username, password, enterprise, apiversion, configuration):
        """ Initializes Courgette

            Args:
                vsdurl (string): the url of the vsd with its port
                username (string): the username to launch tests
                password (string): the password to connect to the vsd
                enterprise (string): the name of the enterprise to connect to the vsd
                version (float): the version of the API to connect
                data (dict): a dictionary containing following information:

                    spec (dict): the specification
                    parent (dict): the parent information (resourceName and ID)
                    default_values: the default values for the object
                    RESTName (string): Optionnally to avoid to provide the specification

        """
        self.configuration = configuration
        self.vsdurl = vsdurl
        self.username = username
        self.password = password
        self.enterprise = enterprise
        self.apiversion = apiversion

    def run(self):
        """ Run all tests

            Returns:
                A dictionnary containing tests' results.

        """
        runner = TestsRunner(vsdurl=self.vsdurl,
                             username=self.username,
                             password=self.password,
                             enterprise=self.enterprise,
                             version=self.apiversion,
                             model=self.configuration.specification,
                             parent_resource=self.configuration.parent_resource_name,
                             parent_id=self.configuration.parent_id,
                             **self.configuration.default_values)

        return runner.run()
