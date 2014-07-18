# -*- coding: utf-8 -*-
from .autogenerates import NUL2DomainTemplate as AutoGenerate


class NUL2DomainTemplate(AutoGenerate):
    """ Represents a L2DomainTemplate object """

    def get_type(self):
        """ Returns domain type """

        return u'L2DOMAIN'
