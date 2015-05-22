# -*- coding: utf-8 -*-

__all__ = ['Command']


from .lib import SwaggerParser
from .lib import SpecificationTransformer
from .lib import SwaggerTransformer
from .lib.bladerunner import TestsRunner

from monolithe.lib.utils.printer import Printer


class Command(object):
    """ Command

    """
    @classmethod
    def run_tests(cls, vsdurl, username, password, enterprise, version, data):
        """ Run all tests according to the given data

            `data` contains information:
                `spec`: the specification
                `parent`: the parent information
                `default_values`: the default values for the object

            Args:
                data (dict):

        """
        rest_name = None

        if 'RESTName' in data:
            Printer.log('******* %s' % data['RESTName'])
            rest_name = data['RESTName']

        parent_object = data['parentObject']
        default_values = data['defaultValues']

        spec = data['spec']

        if spec is None or len(spec) == 0:
            spec = Command.get_spec(vsdurl=vsdurl, apiversion=version, rest_name=rest_name)

        processed_spec = SpecificationTransformer.get_objects(specifications={spec['model']['RESTName']: spec})
        model = processed_spec[spec['model']['RESTName']]

        runner = TestsRunner(vsdurl=vsdurl, username=username, password=password, enterprise=enterprise, version=version, model=model, parent_resource=parent_object['resourceName'], parent_id=parent_object['id'], **default_values)

        return runner.run()

    @classmethod
    def get_spec(cls, vsdurl, apiversion, rest_name, path=None):
        """

        """
        if vsdurl is None and path is None:
            Printer.raiseError("Please provide a vsd url or a path to swagger json file")

        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=vsdurl, path=path, apiversion=apiversion)
        resources = swagger_parser.run(filters=[rest_name])

        # Convert Swagger models
        specs = SwaggerTransformer.get_specifications(resources=resources, filters=[rest_name])

        if rest_name in specs:
            return specs[rest_name]

        return None
