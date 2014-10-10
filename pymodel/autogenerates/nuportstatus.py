# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUPortStatus(NURESTObject):
    """ Represents a PortStatus object """

    def __init__(self):
        """ Initializing object """

        super(NUPortStatus, self).__init__()

        # Read/Write Attributes
        
        self.access = None
        self.description = None
        self.last_state_change = None
        self.name = None
        self.state = None
        self.uplink = None
        
        self.expose_attribute(local_name=u"access", remote_name=u"access", attribute_type=bool)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"last_state_change", remote_name=u"lastStateChange", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"state", remote_name=u"state", attribute_type=str)
        self.expose_attribute(local_name=u"uplink", remote_name=u"uplink", attribute_type=bool)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"monitoringport"

    # REST methods
    