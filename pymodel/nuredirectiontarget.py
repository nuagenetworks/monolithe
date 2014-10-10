# -*- coding: utf-8 -*-
from .autogenerates import NURedirectionTarget as AutoGenerate

from constants import RedirectionTargetEndPointType


class NURedirectionTarget(AutoGenerate):
    """ Represents a RedirectionTarget object """

    def __init__(self):
        """ Initializing object """

        super(NURedirectionTarget, self).__init__()

        self.end_point_type = RedirectionTargetEndPointType.L3
