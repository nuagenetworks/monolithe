# -*- coding: utf-8 -*-
from .autogenerates import NUGatewayTemplate as AutoGenerate
from constants import GatewayPersonality


class NUGatewayTemplate(AutoGenerate):
    """ Represents a GatewayTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUGatewayTemplate, self).__init__()

        self.personality = GatewayPersonality.VRSG
