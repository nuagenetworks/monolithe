# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import os


class MonolitheConfig(object):

    config = None
    mapping = None
    sdk_vanilla_path = None
    apidoc_vanilla_path = None
    sdkdoc_vanilla_path = None


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
        mapping_path = cls.get_config("mapping_path")
        cls._check_path_exists(mapping_path)
        cls.mapping = ConfigParser()
        cls.mapping.read(mapping_path)

        # vanilla
        cls.sdk_vanilla_path = cls.get_config("sdk_vanilla_path")
        cls.apidoc_vanilla_path = cls.get_config("apidoc_vanilla_path")
        cls.sdkdoc_vanilla_path = cls.get_config("sdkdoc_vanilla_path")


    @classmethod
    def get_config(cls, option, section="monolithe"):
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

