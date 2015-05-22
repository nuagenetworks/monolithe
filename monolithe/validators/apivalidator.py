# -*- coding: utf-8 -*-

from monolithe.lib.utils.printer import Printer

from monolithe.lib.parsers import SwaggerParser
from monolithe.lib.transformers import SpecificationTransformer, SwaggerTransformer
from monolithe.lib.bladerunner import TestsRunner


class APIValidator(object):
    """ Validates API by launching specification-generated tests

    """
    def __init__(self, vsdurl, swagger_path, username, password, enterprise, apiversion, data):
        """ Initializes a VSDKGenerator

            Can be used to generate a vsdk from a remote vsdurl or a local swagger_path.

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
        self.rest_name = None
        self.specification = None
        self.vsdurl = vsdurl
        self.swagger_path = swagger_path
        self.username = username
        self.password = password
        self.enterprise = enterprise
        self.apiversion = apiversion

        if self.vsdurl is None and self.path is None:
            Printer.raiseError("Please provide a vsd url or a path to swagger json file")

        # Verify Parent information
        if 'parentObject' not in data:
            Printer.raiseError('No parentObject information provided')
        elif 'resourceName' not in data['parentObject']:
            Printer.raiseError('No parent resourceName information provided')
        elif 'id' not in data['parentObject']:
            Printer.raiseError('No parent id information provided')

        self.parent_id = data['parentObject']['id']
        self.parent_resource = data['parentObject']['resourceName']

        # Verify default values
        if 'defaultValues' not in data:
            Printer.raiseError('No defaultValues information provided')

        self.default_values = data['defaultValues']

        if 'spec' in data:
            self.specifications = data['spec']

        if self.specification is None or len(self.specification) == 0:
            if 'RESTName' not in data:
                Printer.raiseError('No RESTName information provided')

            self.specification = self.get_specification(rest_name=data['RESTName'])
            self.rest_name = self.specification['model']['RESTName']

    def run(self):
        """ Run all tests

            Returns:
                A dictionnary containing tests' results.

        """
        processed_spec = SpecificationTransformer.get_objects(specifications={self.rest_name: self.specification})
        model = processed_spec[self.rest_name]

        runner = TestsRunner(vsdurl=self.vsdurl, username=self.username, password=self.password, enterprise=self.enterprise, version=self.apiversion, model=model, parent_resource=self.parent_resource, parent_id=self.parent_id, **self.default_values)

        return runner.run()

    def get_specification(self, rest_name):
        """ Retrieve a specification by its RESTName

        """
        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=self.vsdurl, path=self.swagger_path, apiversion=self.apiversion)
        swagger_resources = swagger_parser.run(filters=[rest_name])

        # Convert Swagger models
        specifications = SwaggerTransformer.get_specifications(resources=swagger_resources, filters=[rest_name])

        if rest_name in specifications:
            return specifications[rest_name]

        return None
