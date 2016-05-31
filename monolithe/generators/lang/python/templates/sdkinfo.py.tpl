# -*- coding: utf-8 -*-
{{ header }}

from .{{ class_prefix|lower }}{{ product_accronym|lower }}session import {{ class_prefix }}{{ product_accronym }}Session
from .{{ class_prefix|lower }}{{ root_api|lower }} import {{ class_prefix }}{{ root_api|capitalize }}

class SDKInfo (object):

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
        return "{{ api_prefix }}"

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
    def class_prefix(cls):
        """
            Returns the api prefix
        """
        return "{{ class_prefix }}"

    @classmethod
    def name(cls):
        """
            Returns the sdk name
        """
        return "{{ name }}"

    @classmethod
    def root_object_class(cls):
        """
            Returns the root object class
        """
        return {{ class_prefix }}{{ root_api|capitalize }}

    @classmethod
    def session_class(cls):
        """
            Returns the session object class
        """
        return {{ class_prefix }}{{ product_accronym }}Session
