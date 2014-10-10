# -*- coding: utf-8 -*-
from .autogenerates import NURedirectionTargetTemplate as AutoGenerate

from constants import RedirectionTargetEndPointType


class NURedirectionTargetTemplate(AutoGenerate):
    """ Represents a RedirectionTargetTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NURedirectionTargetTemplate, self).__init__()

        self.end_point_type = RedirectionTargetEndPointType.L3
