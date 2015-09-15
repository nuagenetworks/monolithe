# -*- coding: utf-8 -*-

from monolithe import monolithe_config
from monolithe.lib import Printer

from monolithe.specifications import RepositoryManager
from monolithe.generators.apidoc.lib import APIDocWriter


class APIDocumentationGenerator(object):
    """ Generate VSD API Documentation

    """
    def __init__(self, api_url, login_or_token, password, organization, repository, version=u'master', output_path=None, force_removal=False):
        """
        """
        self.version = version
        self.output_path = output_path
        self.force_removal = force_removal

        self.repository_manager = RepositoryManager(api_url=api_url,
                                                    login_or_token=login_or_token,
                                                    password=password,
                                                    organization=organization,
                                                    repository=repository)

    def run(self):
        """ Start generation ofthe API Documentation

        """
        Printer.log("Starting API documentation generation from branch `%s` of repository `%s`" % (self.version, self.repository_manager.repository))

        specifications = self.repository_manager.get_all_specifications(branch=self.version)

        if self.output_path:
            directory = '%s/%s' % (self.output_path, self.version)
        else:
            directory = '%s/%s' % (monolithe_config.get('monolithe', 'docs_directory'), self.version)

        if self.force_removal and os.path.exists(directory):
            shutil.rmtree(directory)

        # Write Python sources
        writer = APIDocWriter(directory=directory)
        writer.write(resources=specifications, apiversion=self.version)

        Printer.success('Generated %s documentation files for API version %s' % (len(specifications), self.version))
