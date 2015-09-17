# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import os


class MonolitheConfig(object):

    config = None
    mapping = None
    sdk_user_vanilla = None
    apidoc_user_vanilla = None
    sdkdoc_user_vanilla = None
    is_configured = False

    @classmethod
    def _check_path_exists(self, path):
        """
        """
        if not os.path.exists(path):
            raise Exception("Couldn't find path %s" % path)

    @classmethod
    def ready(cls):
        """
        """
        return cls.is_configured

    @classmethod
    def set_config_path(cls, path):
        """
        """
        cls._check_path_exists(path)
        cls.config = ConfigParser()
        cls.config.read(path)

        # mapping
        mapping_path = cls.get_option("mapping_path")
        cls._check_path_exists(mapping_path)
        cls.mapping = ConfigParser()
        cls.mapping.read(mapping_path)

        # vanilla
        cls.sdk_user_vanilla = cls.get_option("sdk_user_vanilla", "sdk")
        cls.apidoc_user_vanilla = cls.get_option("apidoc_user_vanilla", "apidoc")
        cls.sdkdoc_user_vanilla = cls.get_option("sdkdoc_user_vanilla", "sdkdoc")

        is_configured = True

    @classmethod
    def get_sdk_config(self):
        """
        """
        return {
            "sdk_name" : cls.get_option("sdk_name", "sdk")
            "sdk_output" : cls.get_option("sdk_output", "sdk")
            "sdk_user_vanilla" : cls.get_option("sdk_user_vanilla", "sdk")
            "sdk_output" : cls.get_option("sdk_output", "sdk")
            "sdk_user_vanilla" : cls.get_option("sdk_user_vanilla", "sdk")
            "sdk_name" : cls.get_option("sdk_name", "sdk")
            "sdk_version" : cls.get_option("sdk_version", "sdk")
            "sdk_revision_number" : cls.get_option("sdk_revision_number", "sdk")
            "sdk_url" : cls.get_option("sdk_url", "sdk")
            "sdk_author" : cls.get_option("sdk_author", "sdk")
            "sdk_email" : cls.get_option("sdk_email", "sdk")
            "sdk_description" : cls.get_option("sdk_description", "sdk")
            "sdk_license_name" : cls.get_option("sdk_license_name", "sdk")
        }

    @classmethod
    def get_option(cls, option, section="monolithe"):
        """
        """
        return cls.config.get(section, option)


    @classmethod
    def map_attribute(cls, remote_name, attribute_name):
        """
        """
        if not cls.mapping.has_section(remote_name) or not cls.mapping.has_option(remote_name, attribute_name):
            return attribute_name

        return cls.mapping.get(remote_name, attribute_name)

