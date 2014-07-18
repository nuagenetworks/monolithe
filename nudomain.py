# -*- coding: utf-8 -*-
from .autogenerates import NUDomain as AutoGenerate
from constants import ApplicationDeploymentPolicy, DomainTunnelType, MaintenanceMode

class NUDomain(AutoGenerate):
    """ Represents a Domain object """

    def __init__(self):
        """ Initializing object """

        super(NUDomain, self).__init__()

        self.application_deployment_policy = ApplicationDeploymentPolicy.NONE
        self.maintenance_mode = MaintenanceMode.DISABLED
        self.tunnel_type = DomainTunnelType.DEFAULT

    def get_type(self):
        """ Returns domain type """

        return u'DOMAIN'
