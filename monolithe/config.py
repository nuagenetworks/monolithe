# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import os


class MonolitheConfig(object):

    @classmethod
    def config_with_path(cls, path):
        """
        """
        return MonolitheConfig(path)

    def __init__(self, path):
        """
        """
        self.config = None
        self.mapping = None
        self.sdk_user_vanilla = None
        self.apidoc_user_vanilla = None
        self.sdkdoc_user_vanilla = None

        self.set_config_path(path)

    def _check_path_exists(self, path):
        """
        """
        if not os.path.exists(path):
            raise Exception("Couldn't find path %s" % path)

    def set_config_path(self, path):
        """
        """
        self._check_path_exists(path)
        self.config = ConfigParser()
        self.config.read(path)

        # mapping
        mapping_path = self.get_option("mapping_path")
        self._check_path_exists(mapping_path)
        self.mapping = ConfigParser()
        self.mapping.read(mapping_path)

        # vanilla
        self.sdk_user_vanilla = self.get_option("sdk_user_vanilla", "sdk")
        self.apidoc_user_vanilla = self.get_option("apidoc_user_vanilla", "apidoc")
        self.sdkdoc_user_vanilla = self.get_option("sdkdoc_user_vanilla", "sdkdoc")

    def get_sdk_config(self):
        """
        """
        return {
            "sdk_name" : self.get_option("sdk_name", "sdk"),
            "sdk_output" : self.get_option("sdk_output", "sdk"),
            "sdk_user_vanilla" : self.get_option("sdk_user_vanilla", "sdk"),
            "sdk_output" : self.get_option("sdk_output", "sdk"),
            "sdk_user_vanilla" : self.get_option("sdk_user_vanilla", "sdk"),
            "sdk_name" : self.get_option("sdk_name", "sdk"),
            "sdk_version" : self.get_option("sdk_version", "sdk"),
            "sdk_revision_number" : self.get_option("sdk_revision_number", "sdk"),
            "sdk_url" : self.get_option("sdk_url", "sdk"),
            "sdk_author" : self.get_option("sdk_author", "sdk"),
            "sdk_email" : self.get_option("sdk_email", "sdk"),
            "sdk_description" : self.get_option("sdk_description", "sdk"),
            "sdk_license_name" : self.get_option("sdk_license_name", "sdk")
        }

    def get_option(self, option, section="monolithe"):
        """
        """
        return self.config.get(section, option)


    def map_attribute(self, remote_name, attribute_name):
        """
        """
        if not self.mapping.has_section(remote_name) or not self.mapping.has_option(remote_name, attribute_name):
            return attribute_name

        return self.mapping.get(remote_name, attribute_name)

