# -*- coding: utf-8 -*-

import importlib

from .sdkutils import SDKUtils
from bambou import NURESTModelController


class SDKLoader(object):
    """
    """

    def __init__(self, version, sdk_identifier):
        """
        """
        self._sdk_identifier = sdk_identifier
        self._version = SDKUtils.get_string_version(version)
        self._sdk_module = importlib.import_module("%s.%s" % (self._sdk_identifier, self._version))
        self._sdk_utils_module = importlib.import_module("%s.utils" % self._sdk_identifier)

        self._load_sdk()
        self._load_sdk_utils()

    @property
    def sdk(self):
        return self._sdk_module

    @property
    def sdk_utils(self):
        return self._sdk_utils_module

    @property
    def version(self):
        return self._version

    @property
    def sdk_identifier(self):
        return self._sdk_identifier

    def class_from_rest_name(self, rest_name):
        """
        """
        return NURESTModelController.get_first_model(rest_name=rest_name)

    def get_instance_from_rest_name(self, rest_name):
        """
        """
        klass = self.class_from_rest_name(rest_name)

        if klass:
            return klass()

        return None