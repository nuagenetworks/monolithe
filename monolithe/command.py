# -*- coding: utf-8 -*-

__all__ = ['Command']

import os
import shutil
import json

from .lib import SwaggerParser
from .lib import SDKWriter, DocWriter, CourgetteWriter
from .lib import ModelsProcessor
from .lib import GitManager
from .lib import SwaggerToSpecConverter
from .lib import SpecParser
from .lib import TestsRunner

from monolithe.utils.printer import Printer
from monolithe.utils.urls import URLUtils

CODEGEN_DIRECTORY = './codegen'
DOCS_DIRECTORY = './docgen'
SPECGEN_DIRECTORY = './specgen'


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

        processed_spec = ModelsProcessor.process(resources={spec['model']['RESTName']: spec})
        model = processed_spec[spec['model']['RESTName']]

        runner = TestsRunner(vsdurl=vsdurl, username=username, password=password, enterprise=enterprise, version=version, model=model, parent_resource=parent_object['resourceName'], parent_id=parent_object['id'], **default_values)

        return runner.run()

    @classmethod
    def get_spec(cls, vsdurl, apiversion, rest_name, path=None):
        """

        """
        path = URLUtils.remove_slash(path)
        url = cls._get_api_url(vsdurl)

        if url is None and path is None:
            Printer.raiseError("Please provide a vsd url or a path to swagger json file")

        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=url, path=path, apiversion=apiversion)
        resources = swagger_parser.run(filters=[rest_name])

        # Convert Swagger models
        specs = SwaggerToSpecConverter.convert(resources=resources, filters=[rest_name])

        if rest_name in specs:
            return specs[rest_name]

        return None

    @classmethod
    def generate_specs(cls, vsdurl, path, apiversion, output_path=None):
        """ Generate specs

        """
        path = URLUtils.remove_slash(path)
        url = cls._get_api_url(vsdurl)

        if url is None and path is None:
            Printer.raiseError("Please provide a vsd url or a path to swagger json file")

        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=url, path=path, apiversion=apiversion)
        resources = swagger_parser.run()

        # Convert Swagger models
        specs = SwaggerToSpecConverter.convert(resources=resources)

        if not output_path:
            output_path = SPECGEN_DIRECTORY

        output_path = '%s/%s' % (output_path, apiversion)

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        for name, spec in specs.iteritems():

            file_path = '%s/%s.spec' % (output_path, spec['model']['entityName'].lower())
            with open(file_path, 'wb') as file:
                json.dump(spec, file, indent=4, sort_keys=True)

    @classmethod
    def generate_sdk(cls, vsdurl, path, apiversion, revision, git_repository, output_path=None, push=False, force_removal=False, specs_path=None):
        """ Generate the Python SDK according to given parameters

            It will generate a new SDK from vanilla/vsdk sources or update the targeted repository.

            Args:
                vsdurl: the url to the vsd api
                apiversion: the version of the vsd api in a dotted notation (ex: 3.0)
                revision: the revision number
                git_repository: the GIT repository URL from where to start
                output_path: the path to the output directory
                push: boolean to ask for the push or not
                force: force removal of the existing codegen directory

        """
        path = URLUtils.remove_slash(path)
        url = cls._get_api_url(vsdurl)

        if url is None and path is None:
            Printer.raiseError("Please provide a vsd url or a path to swagger json file")

        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=url, path=path, apiversion=apiversion)
        resources = swagger_parser.run()

        # Convert Swagger models
        specs = SwaggerToSpecConverter.convert(resources=resources)

        if specs_path is not None:
            candidates = SpecParser.grab_all(specs_path)
            specs.update(candidates)

        # Process Swagger models
        processed_resources = ModelsProcessor.process(resources=specs)

        # Compute output directory according to the version
        if apiversion is None:
            apiversion = swagger_parser.apiversion

        if output_path:
            directory = '%s/%s' % (output_path, apiversion)
        else:
            directory = '%s/%s' % (CODEGEN_DIRECTORY, apiversion)

        if force_removal and os.path.exists(directory):
            shutil.rmtree(directory)

        # Grab existing sources
        git_manager = None

        if git_repository:
            git_manager = GitManager(url=git_repository, branch=apiversion, directory=directory)

        # Write Python sources
        sdk_writer = SDKWriter(directory=directory)
        sdk_writer.write(resources=processed_resources, apiversion=apiversion, revision=revision)

        if git_manager and push:
            nb_diffs = git_manager.commit(message="Update from API %s" % apiversion)
            Printer.log("Ready to push %s modification to branch %s of repistory %s" % (nb_diffs, apiversion, git_repository))
            git_manager.push()

    @classmethod
    def generate_doc(cls, vsdurl, path, apiversion, output_path=None):
        """ Generate the Python SDK according to given parameters

            It will generate a new SDK from vanilla/vsdk sources or update the targeted repository.

            Args:
                vsdurl: the url to the vsd api
                apiversion: the version of the vsd api in a dotted notation (ex: 3.0)
                output_path: the path to the output directory

        """
        path = URLUtils.remove_slash(path)
        url = cls._get_api_url(vsdurl)

        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=url, path=path, apiversion=apiversion)
        resources = swagger_parser.run()

        # Convert Swagger models
        specs = SwaggerToSpecConverter.convert(resources=resources)

        # Process Swagger models
        processed_resources = ModelsProcessor.process(resources=specs)

        # Compute output directory according to the version
        if apiversion is None:
            apiversion = swagger_parser.apiversion

        if output_path:
            directory = '%s/%s' % (output_path, apiversion)
        else:
            directory = '%s/%s' % (DOCS_DIRECTORY, apiversion)

        # Write Python sources
        doc_writer = DocWriter(directory=directory)
        doc_writer.write(resources=processed_resources, apiversion=apiversion)

    @classmethod
    def generate_courgette(cls, vsdurl, apiversion, output_path, path=None):
        """ Generate Courgette sources

            It will generate all the environments and tests for the Courgette Framework.

            Args:
                vsdurl: the url to the vsd api
                apiversion: the version of the vsd api in a dotted notation (ex: 3.0)
                output_path: the path to the output directory

        """
        directory = '%s' % output_path

        path = URLUtils.remove_slash(path)
        url = cls._get_api_url(vsdurl)

        # Read Swagger
        swagger_parser = SwaggerParser(vsdurl=url, path=path, apiversion=apiversion)
        resources = swagger_parser.run()

        # Processed Swagger models
        processed_resources = ModelsProcessor.process(resources=resources)

        writer = CourgetteWriter(directory=directory)
        writer.write(resources=processed_resources)

    @classmethod
    def _get_api_url(cls, vsdurl=None):
        """ Compute API Url according to vsdurl parameter

            Args:
                vsdurl: the vsd url given

        """
        url = URLUtils.remove_slash(vsdurl)

        if url:
            return '%s/%s' % (vsdurl, API_URL)

        return None
