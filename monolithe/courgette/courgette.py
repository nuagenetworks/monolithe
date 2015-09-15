# -*- coding: utf-8 -*-

from monolithe.courgette.lib import TestsRunner
from .courgetteresult import CourgetteResult


class Courgette(object):
    """ Validates API by launching specification-generated tests

    """
    def __init__(self, vsdurl, username, password, enterprise, apiversion, sdk_identifier):
        """ Initializes Courgette

            Args:
                vsdurl (string): the url of the vsd with its port
                username (string): the username to launch tests
                password (string): the password to connect to the vsd
                enterprise (string): the name of the enterprise to connect to the vsd
                apiversion (float): the version of the API to connect
                sdk (string): the full name of the SDK to use
        """

        self.vsdurl = vsdurl
        self.username = username
        self.password = password
        self.enterprise = enterprise
        self.apiversion = apiversion
        self.sdk_identifier = sdk_identifier

    def run(self, configurations):
        """ Run all tests

            Returns:
                A dictionnary containing tests' results.

        """

        result = CourgetteResult()

        for configuration in configurations:

            runner = TestsRunner(vsdurl=self.vsdurl,
                                 username=self.username,
                                 password=self.password,
                                 enterprise=self.enterprise,
                                 version=self.apiversion,
                                 model=configuration.specification,
                                 parent_resource=configuration.parent_resource_name,
                                 parent_id=configuration.parent_id,
                                 sdk_identifier=self.sdk_identifier,
                                 **configuration.default_values)

            result.add_report(configuration.specification.remote_name + ".spec", runner.run())

        return result


