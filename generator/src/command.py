# -*- coding: utf-8 -*-

__all__ = ['Command']

from lib import SwaggerParser
from lib import Printer
from lib import SDKWriter
from lib import ModelsProcessor
from lib import GitManager

CODEGEN_DIRECTORY = './codegen'


class Command(object):
    """ Command

    """
    @classmethod
    def run(self, vsdurl, apiversion, revision, git_repository, output_path=None, push=False):
        """ Run the command with following arguments

            It will generate a new SDK from vanilla/vsdk sources or update the targeted repository.

            Args:
                vsdurl: the url to the vsd api
                apiversion: the version of the vsd api in a dotted notation (ex: 3.0)
                revision: the revision number
                git_repository: the GIT repository URL from where to start
                output_path: the path to the output directory
                push: boolean to ask for the push or not

        """
        if output_path:
            directory = '%s/%s' % (output_path, apiversion)
        else:
            directory = '%s/%s' % (CODEGEN_DIRECTORY, apiversion)

        git_manager = None

        if (git_repository):
            git_manager = GitManager(url=git_repository, branch=apiversion, directory=directory)

        # Read Swagger
        swagger_parser = SwaggerParser()
        resources = swagger_parser.grab_all(url=vsdurl, apiversion=apiversion)

        # Processed Swagger models
        processed_resources = ModelsProcessor.process(resources=resources)

        # Write Python sources
        sdk_writer = SDKWriter(directory=directory)
        sdk_writer.write_sdk(resources=processed_resources, apiversion=apiversion, revision=revision)

        if git_manager and push:
            nb_diffs = git_manager.commit(message="Update from API %s" % apiversion)
            Printer.log("Ready to push %s modification to branch %s of repistory %s" % (nb_diffs, apiversion, git_repository))
            git_manager.push()
            git_manager.remove_directory()
