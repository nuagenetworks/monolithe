# -*- coding: utf-8 -*-
from ConfigParser import ConfigParser
import os
import StringIO

class MonolitheConfig(object):

    @classmethod
    def config_with_path(cls, path):
        """
        """
        return MonolitheConfig(path)

    def __init__(self, path=None):
        """
        """
        self.path = path
        self.config = None
        self.mapping = None

        if self.path:
            self._check_path_exists(path)
            config = ConfigParser()
            config.read(path)
            self.set_config(config)

    def copy(self):
        """
        """
        # duplicate the config parser
        conf_data = StringIO.StringIO()
        self.config.write(conf_data)
        conf_data.seek(0)
        new_config_parser = ConfigParser()
        new_config_parser.readfp(conf_data)

        # create a new MonolitheConfig and give it the duplicate config parser
        monolithe_config_copy = MonolitheConfig(path=self.path)
        monolithe_config_copy.set_config(new_config_parser)

        return monolithe_config_copy

    def _check_path_exists(self, path):
        """
        """
        if not os.path.exists(path):
            raise Exception("Could not find path %s" % path)

    def set_config(self, config):
        """
        """
        self.config = config

        # vanilla
        self.sdk_user_vanilla = self.get_option("sdk_user_vanilla", "sdk")
        self.apidoc_user_vanilla = self.get_option("apidoc_user_vanilla", "apidoc")
        self.sdkdoc_user_vanilla = self.get_option("sdkdoc_user_vanilla", "sdkdoc")

        # mapping
        mapping_path = "%s/mapping.ini" % os.path.dirname(self.path)

        if not os.path.exists(self.path):
            return

        self.mapping = ConfigParser()
        self.mapping.read(mapping_path)

    def get_option(self, option, section="monolithe"):
        """
        """
        return self.config.get(section, option)

    def set_option(self, option, value, section="monolithe"):
        """
        """
        return self.config.set(section, option, value)


    def map_attribute(self, remote_name, attribute_name):
        """
        """
        if self.mapping is None or not self.mapping.has_section(remote_name) or not self.mapping.has_option(remote_name, attribute_name):
            return attribute_name

        return self.mapping.get(remote_name, attribute_name)

