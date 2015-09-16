# -*- coding: utf-8 -*-

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.generators.lib.writers import TemplateFileWriter


class SDKWriter(object):
    """
    """

    def __init__(self, directory, apiversions):
        """
        """
        self.writer_directory = directory
        self.apiversions = apiversions


    def get_writer(self):
        """ Get a writer to write content

        """
        return _SDKFileWriter(directory=self.writer_directory)

    def write(self):
        """
        """
        writer = self.get_writer()
        writer.write_setup_file()
        writer.write_manifest_file(self.apiversions)
        writer.write_requirements_file()



class _SDKFileWriter(TemplateFileWriter):
    """
    """
    def __init__(self, directory):
        """
        """
        super(_SDKFileWriter, self).__init__(directory=directory, package='monolithe.generators.sdk')


    def write_setup_file(self):
        """
        """
        self.write( destination=self.directory, filename='setup.py', template_name='setup.py.tpl',
                    sdk_name=MonolitheConfig.get_option("sdk_name", "sdk"),
                    sdk_copyright=MonolitheConfig.get_option("sdk_copyright", "sdk"),
                    sdk_version=MonolitheConfig.get_option("sdk_version", "sdk"),
                    sdk_revision_number=MonolitheConfig.get_option("sdk_revision_number", "sdk"),
                    sdk_url=MonolitheConfig.get_option("sdk_url", "sdk"),
                    sdk_author=MonolitheConfig.get_option("sdk_author", "sdk"),
                    sdk_email=MonolitheConfig.get_option("sdk_email", "sdk"),
                    sdk_description=MonolitheConfig.get_option("sdk_description", "sdk"),
                    sdk_license_name=MonolitheConfig.get_option("sdk_license_name", "sdk"))

    def write_manifest_file(self, apiversions):
        """
        """
        self.write( destination=self.directory, filename='MANIFEST.in', template_name='MANIFEST.in.tpl',
                    sdk_name=MonolitheConfig.get_option("sdk_name"),
                    apiversions=[SDKUtils.get_string_version(version) for version in apiversions])

    def write_requirements_file(self):
        """
        """
        self.write( destination=self.directory, filename='requirements.txt', template_name='requirements.txt.tpl')
