# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUVirtualIP(NURESTObject):
    """ Represents a VirtualIP object """

    def __init__(self):
        """ Initializing object """

        super(NUVirtualIP, self).__init__()

        # Read/Write Attributes
        
        self.virtual_ip = None
        
        self.expose_attribute(local_name=u"virtual_ip", remote_name=u"virtualIP", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"virtualip"

    # REST methods
    