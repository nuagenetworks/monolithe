# -*- coding: utf-8 -*-
from .autogenerates import NUDomainTemplate as AutoGenerate


class NUDomainTemplate(AutoGenerate):
    """ Represents a DomainTemplate object """

    def get_type(self):
        """ Returns domain type """

        return u'DOMAIN'
