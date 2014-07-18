# -*- coding: utf-8 -*-
from .autogenerates import NUService as AutoGenerate
from constants import ApplicationServiceDirection


class NUService(AutoGenerate):
    """ Represents a Service object """

    def __init__(self):
        """ Initializing object """

        super(NUService, self).__init__()

        self.direction = ApplicationServiceDirection.REFLEXIVE
