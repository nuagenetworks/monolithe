# -*- coding: utf-8 -*-

from monolithe.courgette.lib import CourgetteTestsRunner
from .result import CourgetteResult


class Courgette(object):
    """ Validates API by launching specification-generated tests

    """
    def __init__(self, url, username, password, enterprise, apiversion, sdk_identifier, monolithe_config):
        """ Initializes Courgette

            Args:
                url (string): the url of the server with its port
                username (string): the username to launch tests
                password (string): the password to connect to the server
                enterprise (string): the name of the enterprise to connect to the server
                apiversion (float): the version of the API to connect
                sdk (string): the full name of the SDK to use
        """

        self.url = url
        self.username = username
        self.password = password
        self.enterprise = enterprise
        self.apiversion = apiversion
        self.monolithe_config = monolithe_config
        self.sdk_identifier = sdk_identifier

    def run(self, configurations):
        """ Run all tests

            Returns:
                A dictionnary containing tests' results.

        """

        result = CourgetteResult()

        for configuration in configurations:

            runner = CourgetteTestsRunner(  url=self.url,
                                            username=self.username,
                                            password=self.password,
                                            enterprise=self.enterprise,
                                            version=self.apiversion,
                                            model=configuration.specification,
                                            sdk_identifier=self.sdk_identifier,
                                            monolithe_config=self.monolithe_config,
                                            parent_resource=configuration.parent_resource_name,
                                            parent_id=configuration.parent_id,
                                            **configuration.default_values)
            result.add_report(configuration.specification.remote_name + ".spec", runner.run())

        return result


