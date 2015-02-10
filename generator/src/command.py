# -*- coding: utf-8 -*-

__all__ = ['Command']

from .lib import SwaggerParser
from .lib import Printer
from .lib import SDKWriter, DocWriter, CourgetteWriter
from .lib import ModelsProcessor
from .lib import GitManager
from .lib import Utils

CODEGEN_DIRECTORY = './codegen'
DOCS_DIRECTORY = './docgen'

API_URL = 'web/docs/api/'


class Command(object):
    """ Command

    """
    @classmethod
    def generate_sdk(cls, vsdurl, path, apiversion, revision, git_repository, output_path=None, push=False):
        """ Generate the Python SDK according to given parameters

            It will generate a new SDK from vanilla/vsdk sources or update the targeted repository.

            Args:
                vsdurl: the url to the vsd api
                apiversion: the version of the vsd api in a dotted notation (ex: 3.0)
                revision: the revision number
                git_repository: the GIT repository URL from where to start
                output_path: the path to the output directory
                push: boolean to ask for the push or not

        """
        path = Utils.remove_slash(path)
        url = cls._get_api_url(vsdurl)

        if url is None and path is None:
            Printer.raiseError("Please provide a vsd url or a path to swagger json file")

        # Read Swagger
        swagger_parser = SwaggerParser.factory(url=url, path=path, apiversion=apiversion)
        resources = swagger_parser.grab_all()

        # Processed Swagger models
        processed_resources = ModelsProcessor.process(resources=resources)

        # Compute output directory according to the version
        if apiversion is None:
            apiversion = swagger_parser.apiversion

        if output_path:
            directory = '%s/%s' % (output_path, apiversion)
        else:
            directory = '%s/%s' % (CODEGEN_DIRECTORY, apiversion)

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
        path = Utils.remove_slash(path)
        url = cls._get_api_url(vsdurl)

        # Read Swagger
        swagger_parser = SwaggerParser.factory(url=url, apiversion=apiversion, path=path)
        resources = swagger_parser.grab_all()

        # Processed Swagger models
        processed_resources = ModelsProcessor.process(resources=resources)

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

        path = Utils.remove_slash(path)
        url = cls._get_api_url(vsdurl)

        # Read Swagger
        swagger_parser = SwaggerParser.factory(url=url, apiversion=apiversion, path=path)
        resources = swagger_parser.grab_all()

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
        url = Utils.remove_slash(vsdurl)

        if url:
            return '%s/%s' % (vsdurl, API_URL)

        return None
