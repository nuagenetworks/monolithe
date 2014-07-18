# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUFloatingIp(NURESTObject):
    """ Represents a FloatingIp object """

    def __init__(self):
        """ Initializing object """

        super(NUFloatingIp, self).__init__()

        # Read/Write Attributes
        
        self.address = None
        self.assigned = None
        self.associated_shared_network_resource_id = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"assigned", remote_name=u"assigned", attribute_type=bool)
        self.expose_attribute(local_name=u"associated_shared_network_resource_id", remote_name=u"associatedSharedNetworkResourceID", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"floatingip"

    # REST methods
    