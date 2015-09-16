# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import os


class MonolitheConfig(object):

    config = None
    mapping = None
    sdk_user_vanilla = None
    apidoc_user_vanilla = None
    sdkdoc_user_vanilla = None


    @classmethod
    def _check_path_exists(self, path):
        """
        """
        if not os.path.exists(path):
            raise Exception("Couldn't find path %s" % path)

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

