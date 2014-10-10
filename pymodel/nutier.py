# -*- coding: utf-8 -*-
from .autogenerates import NUTier as AutoGenerate
from constants import TierType


class NUTier(AutoGenerate):
    """ Represents a Tier object """

    def __init__(self):
        """ Initializing object """

        super(NUTier, self).__init__()

        self.type = TierType.STANDARD
