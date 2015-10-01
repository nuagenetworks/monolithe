# -*- coding: utf-8 -*-

import json
import os

from .specification import Specification
from monolithe.lib import merge_dict

class FolderManager (object):
    """ RepositoryManager is an object that allows to manipulate the API specification repository
    """

    def __init__(self, folder, monolithe_config):
        """
        """
        self._monolithe_config = monolithe_config
        self._folder = folder;

    def get_available_specifications(self):
        """ Returns the list of available specification files

            Args:
                branch: the branch where to find files (default: "master")

            Returns:
                list of all available specification files in the given branch
        """
        ret = []
        for filename in os.listdir(self._folder):
            if os.path.splitext(filename)[1] != ".spec" or filename.startswith("@"):
                continue
            ret.append(filename)
        return ret

    def get_api_info(self):
        """
        """
        with open("%s/api.info" % self._folder, "r") as f:
            try:
                return json.loads(f.read())
            except Exception as e:
                raise Exception("could not parse api.info", e)

    def get_all_specifications(self):
        """
        """
        specifications = []
        for name in self.get_available_specifications():
            specifications.append(self.get_specification(name))
        return specifications

    def get_specification_data(self, name):
        """
        """
        data = {}
        with open("%s/%s" % (self._folder, name), "r") as f:
            try:
                data = json.loads(f.read())
                if "model" in data and "extends" in data["model"]:
                    for extension in data["model"]["extends"]:
                        data = merge_dict(data, self.get_specification_data(name="%s.spec" % extension))
            except Exception as e:
                raise Exception("Could not parse %s" % name, e)
        return data

    def get_specification(self, name):
        """
        """
        return Specification(data=self.get_specification_data(name), monolithe_config=self._monolithe_config)

    def get_specifications(self, names, callback=None):
        """
        """
        specifications = []
        for name in names:
            specification.append(Specification(data=self.get_specification_data(name=name)))
        return specifications