# -*- coding: utf-8 -*-
from .autogenerates import NUVPort as AutoGenerate
from constants import MulticastChannelMap, VPortAdressProofing, VPortOperationState, VPortType

class NUVPort(AutoGenerate):
    """ Represents a VPort object """

    def __init__(self):
        """ Initializing object """

        super(NUVPort, self).__init__()

        self.address_spoofing = VPortAdressProofing.INHERITED
        self.multicast = MulticastChannelMap.INHERITED;
        self.operational_state = VPortOperationState.INIT;
        self.type = VPortType.VM;