# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUService(NURESTObject):
    """ Represents a Service object """

    def __init__(self):
        """ Initializing object """

        super(NUService, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.destination_port = None
        self.direction = None
        self.dscp = None
        self.ether_type = None
        self.name = None
        self.protocol = None
        self.source_port = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"destination_port", remote_name=u"destinationPort", attribute_type=str)
        self.expose_attribute(local_name=u"direction", remote_name=u"direction", attribute_type=str)
        self.expose_attribute(local_name=u"dscp", remote_name=u"DSCP", attribute_type=str)
        self.expose_attribute(local_name=u"ether_type", remote_name=u"etherType", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"protocol", remote_name=u"protocol", attribute_type=str)
        self.expose_attribute(local_name=u"source_port", remote_name=u"sourcePort", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"applicationservice"

    # REST methods
    