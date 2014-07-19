# -*- coding: utf-8 -*-
from .autogenerates import NUFlowSecurityPolicy as AutoGenerate
from constants import NUFlowSecurityPolicyAction


class NUFlowSecurityPolicy(AutoGenerate):
    """ Represents a FlowSecurityPolicy object """

    def __init__(self):
        """ Initializing object """

        super(NUFlowSecurityPolicy, self).__init__()

        self.action = NUFlowSecurityPolicyAction.FORWARD
