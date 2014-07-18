# -*- coding: utf-8 -*-
from .autogenerates import NUGateway as AutoGenerate
from constants import GatewayPersonality


class NUGateway(AutoGenerate):
    """ Represents a Gateway object """

    def __init__(self):
        """ Initializing object """

        super(NUGateway, self).__init__()

        self.personality = GatewayPersonality.VRSG
