# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUNetworkLayout(NURESTObject):
    """ Represents a NetworkLayout object """

    def __init__(self):
        """ Initializing object """

        super(NUNetworkLayout, self).__init__()

        # Read/Write Attributes

        self.autonomous_system_num = None
        self.route_reflector_ip = None
        self.service_type = None

        self.expose_attribute(local_name=u"autonomous_system_num", remote_name=u"autonomousSystemNum", attribute_type=int)
        self.expose_attribute(local_name=u"route_reflector_ip", remote_name=u"routeReflectorIP", attribute_type=str)
        self.expose_attribute(local_name=u"service_type", remote_name=u"serviceType", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"networklayou"

    # REST methods
