# -*- coding: utf-8 -*-
from .autogenerates import NUL2Domain as AutoGenerate


class NUL2Domain(AutoGenerate):
    """ Represents a L2Domain object """

    def get_type(self):
        """ Returns domain type """

        return u'L2DOMAIN'
