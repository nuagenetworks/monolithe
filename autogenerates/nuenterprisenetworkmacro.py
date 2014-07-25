# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUEnterpriseNetworkMacro(NURESTObject):
    """ Represents a EnterpriseNetworkMacro object """

    def __init__(self):
        """ Initializing object """

        super(NUEnterpriseNetworkMacro, self).__init__()

        # Read/Write Attributes
        
        self.address = None
        self.ip_type = None
        self.name = None
        self.netmask = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"ip_type", remote_name=u"IPType", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"netmask", remote_name=u"netmask", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"enterprisenetwork"

    # REST methods
    