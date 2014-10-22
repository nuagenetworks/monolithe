# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUStaticRoute(NURESTObject):
    """ Represents a StaticRoute object """

    def __init__(self):
        """ Initializing object """

        super(NUStaticRoute, self).__init__()

        # Read/Write Attributes

        self.address = None
        self.ip_type = None
        self.netmask = None
        self.next_hop_ip = None

        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)
        self.expose_attribute(local_name=u"next_hop_ip", remote_name=u"nextHopIp", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"staticroute"

    # REST methods
