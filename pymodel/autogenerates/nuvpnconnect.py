# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUVPNConnect(NURESTObject):
    """ Represents a VPNConnect object """

    def __init__(self):
        """ Initializing object """

        super(NUVPNConnect, self).__init__()

        # Read/Write Attributes
        
        self.associated_wan_service_id = None
        self.description = None
        self.name = None
        
        self.expose_attribute(local_name=u"associated_wan_service_id", remote_name=u"associatedWANServiceID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vpnconnection"

    # REST methods
    