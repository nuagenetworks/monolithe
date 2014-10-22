# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUInfrastructurePortProfile(NURESTObject):
    """ Represents a InfrastructurePortProfile object """

    def __init__(self):
        """ Initializing object """

        super(NUInfrastructurePortProfile, self).__init__()

        # Read/Write Attributes

        self.dhclient = None
        self.duplex = None
        self.vlans = None
        self.ip_address = None
        self.mtu = None
        self.port = None
        self.speed = None
        self.description = None
        self.enterprise_id = None
        self.name = None

        self.expose_attribute(local_name=u"dhclient", remote_name=u"dhclient", attribute_type=bool)
        self.expose_attribute(local_name=u"duplex", remote_name=u"duplex", attribute_type=str)
        self.expose_attribute(local_name=u"vlans", remote_name=u"vlans", attribute_type=str)
        self.expose_attribute(local_name=u"ip_address", remote_name=u"ipAddress", attribute_type=str)
        self.expose_attribute(local_name=u"mtu", remote_name=u"mtu", attribute_type=int)
        self.expose_attribute(local_name=u"port", remote_name=u"port", attribute_type=str)
        self.expose_attribute(local_name=u"speed", remote_name=u"speed", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"infrastructureportprofile"

    # REST methods
