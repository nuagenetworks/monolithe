# -*- coding: utf-8 -*-

import os
import json

from monolithe.lib.utils.printer import Printer
from monolithe.lib.utils.constants import Constants

from monolithe.lib.parsers import SwaggerParser
from monolithe.lib.transformers import SwaggerTransformer


class SpecificationsGenerator(object):
    """ Generate Specification from swagger description files

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
        """ Start generation of all specifications

        """
        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=self.vsdurl, path=self.swagger_path, apiversion=self.apiversion)
        swagger_resources = swagger_parser.run()

        # Convert Swagger models
        specifications = SwaggerTransformer.get_specifications(resources=swagger_resources)

        if not self.output_path:
            self.output_path = Constants.SPECGEN_DIRECTORY

        if self.apiversion is None:
            self.apiversion = swagger_parser.apiversion

        destination = '%s/%s' % (self.output_path, self.apiversion)

        if not os.path.exists(destination):
            os.makedirs(destination)

        for name, specification in specifications.iteritems():

            file_path = '%s/%s.spec' % (destination, specification['model']['entityName'].lower())
            with open(file_path, 'wb') as file:
                json.dump(specification, file, indent=2, sort_keys=True)
