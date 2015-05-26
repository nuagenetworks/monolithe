# -*- coding: utf-8 -*-

import os
import shutil

from monolithe.lib.utils.printer import Printer
from monolithe.lib.utils.constants import Constants

from monolithe.lib.parsers import SpecificationParser, SwaggerParser
from monolithe.lib.transformers import SpecificationTransformer, SwaggerTransformer
from monolithe.generators.vsdk.lib import SDKWriter


class VSDKGenerator(object):
    """ Generate VSDK

    """
    def __init__(self, vsdurl, swagger_path, apiversion, revision, output_path=None, force_removal=False, specifications_path=None):
        """ Initializes a VSDKGenerator

            Can be used to generate a vsdk from a remote vsdurl or a local swagger_path.

            Args:
                vsdurl (string): the url of the vsd with its port
                swagger_path (string): the path to swagger description files
                apiversion (float): the api version
                revision (float): the revision to generate
                output_path (string): the output path to put generated python files
                force_removal (bool): set to True to force previous vsdk files
                specifications_path (string): a path where to get additionnal specifications files

        """
        self.vsdurl = vsdurl
        self.swagger_path = swagger_path
        self.apiversion = apiversion
        self.revision = revision
        self.output_path = output_path
        self.force_removal = force_removal
        self.specifications_path = specifications_path

        if self.vsdurl is None and self.swagger_path is None:
            Printer.raiseError("Please provide a vsd url or a path to swagger json file")

    def run(self):
        """ Start the VSDK generation

        """
        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=self.vsdurl, path=self.swagger_path, apiversion=self.apiversion)
        swagger_resources = swagger_parser.run()

        # Convert Swagger models
        specifications = SwaggerTransformer.get_specifications(resources=swagger_resources)

        if self.specifications_path is not None:
            candidates = SpecificationParser.run(self.specifications_path)
            specifications.update(candidates)

        # Process Swagger models
        processed_resources = SpecificationTransformer.get_objects(specifications=specifications)

        # Compute output directory according to the version
        if self.apiversion is None:
            self.apiversion = swagger_parser.apiversion

        if self.output_path:
            directory = '%s/%s' % (self.output_path, self.apiversion)
        else:
            directory = '%s/%s' % (Constants.CODEGEN_DIRECTORY, self.apiversion)

        if self.force_removal and os.path.exists(directory):
            shutil.rmtree(directory)

        # Write Python sources
        writer = SDKWriter(directory=directory)
        writer.write(resources=processed_resources, apiversion=self.apiversion, revision=self.revision)
