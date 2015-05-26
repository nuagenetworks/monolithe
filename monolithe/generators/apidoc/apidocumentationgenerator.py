# -*- coding: utf-8 -*-

from monolithe.lib.utils.printer import Printer
from monolithe.lib.utils.constants import Constants

from monolithe.lib.parsers import SwaggerParser
from monolithe.lib.transformers import SpecificationTransformer, SwaggerTransformer
from monolithe.generators.apidoc.lib import APIDocWriter


class APIDocumentationGenerator(object):
    """ Generate VSD API Documentation

    """
    def __init__(self, vsdurl, swagger_path, apiversion, output_path=None):
        """ Initializes a VSDKGenerator

            Can be used to generate a vsdk from a remote vsdurl or a local swagger_path.

            Args:
                vsdurl (string): the url of the vsd with its port
                swagger_path (string): the path to swagger description files
                apiversion (float): the api version
                output_path (string): the output path to put generated python files

        """
        self.vsdurl = vsdurl
        self.swagger_path = swagger_path
        self.apiversion = apiversion
        self.output_path = output_path

        if self.vsdurl is None and self.swagger_path is None:
            Printer.raiseError("Please provide a vsd url or a path to swagger json file")

    def run(self):
        """ Start generation ofthe API Documentation

        """
        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=self.vsdurl, path=self.swagger_path, apiversion=self.apiversion)
        swagger_resources = swagger_parser.run()

        # Convert Swagger models
        specifications = SwaggerTransformer.get_specifications(resources=swagger_resources)

        # Process Swagger models
        processed_resources = SpecificationTransformer.get_objects(specifications=specifications)

        # Compute output directory according to the version
        if self.apiversion is None:
            self.apiversion = swagger_parser.apiversion

        if self.output_path:
            directory = '%s/%s' % (self.output_path, self.apiversion)
        else:
            directory = '%s/%s' % (Constants.DOCS_DIRECTORY, self.apiversion)

        # Write Python sources
        writer = APIDocWriter(directory=directory)
        writer.write(resources=processed_resources, apiversion=self.apiversion)
