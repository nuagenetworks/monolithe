# -*- coding: utf-8 -*-

from monolithe import MonolitheConfig
from monolithe.lib import SDKUtils
from monolithe.generators.lib import TemplateFileWriter


class SDKWriter(object):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        self.writer = None

        self.monolithe_config = monolithe_config


    def write(self, apiversions):
        """
        """
        self.writer = _SDKFileWriter(monolithe_config=self.monolithe_config)
        self.writer.write_setup()
        self.writer.write_root_init()
        self.writer.write_utils()
        self.writer.write_manifest(apiversions)
        self.writer.write_requirements()



class _SDKFileWriter(TemplateFileWriter):
    """
    """

    def __init__(self, monolithe_config):
        """
        """
        super(_SDKFileWriter, self).__init__(package="monolithe.generators.sdk")

        self.monolithe_config = monolithe_config
        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")
        self._sdk_version = self.monolithe_config.get_option("sdk_version", "sdk")
        self._sdk_revision_number = self.monolithe_config.get_option("sdk_revision_number", "sdk")
        self._sdk_url = self.monolithe_config.get_option("sdk_url", "sdk")
        self._sdk_author = self.monolithe_config.get_option("sdk_author", "sdk")
        self._sdk_email = self.monolithe_config.get_option("sdk_email", "sdk")
        self._sdk_description = self.monolithe_config.get_option("sdk_description", "sdk")
        self._sdk_license_name = self.monolithe_config.get_option("sdk_license_name", "sdk")
        self._sdk_bambou_version = self.monolithe_config.get_option("sdk_bambou_version", "sdk")
        self._copyright = self.monolithe_config.get_option("copyright")
        self.output_directory = self.monolithe_config.get_option("sdk_output", "sdk")

        with open("%s/__coder_header" % self.output_directory, "r") as f:
            self.header_content = f.read()

    def write_setup(self):
        """
        """
        self.write( destination=self.output_directory, filename="setup.py", template_name="setup.py.tpl",
                    sdk_name=self._sdk_name,
                    sdk_version=self._sdk_version,
                    sdk_revision_number=self._sdk_revision_number,
                    sdk_url=self._sdk_url,
                    sdk_author=self._sdk_author,
                    sdk_email=self._sdk_email,
                    sdk_description=self._sdk_description,
                    sdk_license_name=self._sdk_license_name,
                    copyright=self._copyright,
                    header=self.header_content)

    def write_manifest(self, apiversions):
        """
        """
        self.write( destination=self.output_directory, filename="MANIFEST.in", template_name="MANIFEST.in.tpl",
                    sdk_name=self._sdk_name,
                    apiversions=[SDKUtils.get_string_version(version) for version in apiversions])

    def write_requirements(self):
        """
        """
        self.write( destination=self.output_directory, filename="requirements.txt", template_name="requirements.txt.tpl",
                    sdk_bambou_version=self._sdk_bambou_version)

    def write_root_init(self):
        """
        """
        destination = "%s/%s" % (self.output_directory, self._sdk_name)
        self.write(destination=destination, filename="__init__.py", template_name="__root_init__.py.tpl",
            header=self.header_content)

    def write_utils(self):
        """
        """
        destination = "%s/%s" % (self.output_directory, self._sdk_name)
        self.write(destination=destination, filename="utils.py", template_name="utils.py.tpl",
                    sdk_name=self._sdk_name,
                    header=self.header_content)
