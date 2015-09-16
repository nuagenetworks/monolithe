# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import os


class MonolitheConfig(object):

    config = None
    mapping = None
    vanilla = None

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

    @classmethod
    def set_mapping_path(cls, path):
        """

        """
        cls._check_path_exists(path)
        cls.mapping = ConfigParser()
        cls.mapping.read(path)

    @classmethod
    def set_vanilla_path(cls, path):
        """

        """
        cls._check_path_exists(path)
        cls.vanilla = path


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

