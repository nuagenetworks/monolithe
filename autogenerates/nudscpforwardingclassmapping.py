# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUDSCPForwardingClassMapping(NURESTObject):
    """ Represents a DSCPForwardingClassMapping object """

    def __init__(self):
        """ Initializing object """

        super(NUDSCPForwardingClassMapping, self).__init__()

        # Read/Write Attributes
        
        self.dscp = None
        self.forwarding_class = None
        
        self.expose_attribute(local_name=u"dscp", remote_name=u"DSCP", attribute_type=str)
        self.expose_attribute(local_name=u"forwarding_class", remote_name=u"forwardingClass", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"dscpforwardingclassmapping"

    # REST methods
    