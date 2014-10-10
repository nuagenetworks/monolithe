# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUDHCPOption(NURESTObject):
    """ Represents a DHCPOption object """

    def __init__(self):
        """ Initializing object """

        super(NUDHCPOption, self).__init__()

        # Read/Write Attributes
        
        self.length = None
        self.type = None
        self.value = None
        
        self.expose_attribute(local_name=u"length", remote_name=u"length", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)
        self.expose_attribute(local_name=u"value", remote_name=u"value", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"dhcpoption"

    # REST methods
    