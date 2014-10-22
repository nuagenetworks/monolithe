# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUInfrastructureGatewayProfile(NURESTObject):
    """ Represents a InfrastructureGatewayProfile object """

    def __init__(self):
        """ Initializing object """

        super(NUInfrastructureGatewayProfile, self).__init__()

        # Read/Write Attributes

        self.active_controller = None
        self.gateway = None
        self.haproxy_ip = None
        self.ports = None
        self.standby_controller = None
        self.use_two_factor = None
        self.description = None
        self.enterprise_id = None
        self.name = None

        self.expose_attribute(local_name=u"active_controller", remote_name=u"activeController", attribute_type=str)
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)
        self.expose_attribute(local_name=u"haproxy_ip", remote_name=u"haproxyIP", attribute_type=str)
        self.expose_attribute(local_name=u"ports", remote_name=u"ports", attribute_type=str)
        self.expose_attribute(local_name=u"standby_controller", remote_name=u"standbyController", attribute_type=str)
        self.expose_attribute(local_name=u"use_two_factor", remote_name=u"useTwoFactor", attribute_type=bool)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"infrastructuregatewayprofile"

    # REST methods
