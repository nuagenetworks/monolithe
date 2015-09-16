# -*- coding: utf-8 -*-

from monolithe import MonolitheConfig
from monolithe.generators.lib.writers import TemplateFileWriter


class SDKWriter(object):
    """
    """

    def __init__(self, directory):
        """
        """
        self.writer_directory = directory


    def get_writer(self):
        """ Get a writer to write content

        """
        return _SDKFileWriter(directory=self.writer_directory)

    def write(self):
        """
        """
        writer = self.get_writer()
        writer.write_setup_file()



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
                    sdk_name=MonolitheConfig.get_option("sdk_name"),
                    sdk_copyright=MonolitheConfig.get_option("sdk_copyright"),
                    sdk_version=MonolitheConfig.get_option("sdk_version"),
                    sdk_revision_number=MonolitheConfig.get_option("sdk_revision_number"),
                    sdk_url=MonolitheConfig.get_option("sdk_url"),
                    sdk_author=MonolitheConfig.get_option("sdk_author"),
                    sdk_email=MonolitheConfig.get_option("sdk_email"),
                    sdk_description=MonolitheConfig.get_option("sdk_description"),
                    sdk_license_name=MonolitheConfig.get_option("sdk_license_name"))
