# -*- coding: utf-8 -*-

import os
import sys
import shutil

from monolithe import MonolitheConfig
from monolithe.lib import Printer
from monolithe.specifications import RepositoryManager
from monolithe.generators.sdk.lib import SDKAPIVersionWriter

RepositoryManager


class SDKAPIVersionGenerator(object):
    """ Generate SDK

    """
    def __init__(self, monolithe_config):
        """
        """
        self.monolithe_config = monolithe_config
        self.repository_manager = None

        self._sdk_name = self.monolithe_config.get_option("sdk_name", "sdk")

    def generate(self, specification_info, apiversion):
        """
        """
        for apiversion, specifications in specification_info.iteritems():
            writer = SDKAPIVersionWriter(monolithe_config=self.monolithe_config)
            writer.write(specifications=specifications, apiversion=apiversion)

