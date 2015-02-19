# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.
# NU{{ model.name }}
# {{ model.description }}

from .autogenerates import NU{{ model.name }} as AutoGenerate


class NU{{ model.name }}(AutoGenerate):
    """ Represents a NU{{ model.name }} object in the VSD
        {{ model.description }}

        This object should contain all NU{{ model.name }} specific methods

    """

    def __init__(self, **kwargs):
        """ Initializing a NU{{ model.name }} """

        super(NU{{ model.name }}, self).__init__(**kwargs)

