# -*- coding: utf-8 -*-
{{ header }}

from {{ sdk_class_prefix|lower }}{{ product_accronym|lower }}session import {{ sdk_class_prefix }}{{ product_accronym }}Session
from .{{ sdk_class_prefix|lower }}{{ sdk_root_api|lower }} import {{ sdk_class_prefix }}{{ sdk_root_api|capitalize }}

class SDKInformation (object)

    @classmethod
    def api_version(cls):
        """
            Returns the api version
        """
        return {{ version }}

    @classmethod
    def api_prefix(cls):
        """
            Returns the api prefix
        """
        return "{{ sdk_api_prefix }}"

    @classmethod
    def product_accronym(cls):
        """
            Returns the product accronym
        """
        return "{{ product_accronym }}"

    @classmethod
    def product_name(cls):
        """
            Returns the product name
        """
        return "{{ product_name }}"

    @classmethod
    def sdk_class_prefix(cls):
        """
            Returns the api prefix
        """
        return "{{ sdk_class_prefix }}"

    @classmethod
    def sdk_name(cls):
        """
            Returns the sdk name
        """
        return "{{ sdk_name }}"

    @classmethod
    def root_object_class(cls):
        """
            Returns the root object class
        """
        return {{ sdk_class_prefix }}{{ sdk_root_api|capitalize }}

    @classmethod
    def session_class(cls):
        """
            Returns the session object class
        """
        return {{ sdk_class_prefix }}{{ product_accronym }}Session
