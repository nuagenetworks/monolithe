# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUIPBinding(NURESTObject):
    """ Represents a IPBinding object """

    def __init__(self):
        """ Initializing object """

        super(NUIPBinding, self).__init__()

        # Read/Write Attributes

        self.ip_address = None
        self.dynamic_allocation_enabled = None
        self.mac = None

        self.expose_attribute(local_name=u"ip_address", remote_name=u"IPAddress", attribute_type=str)
        self.expose_attribute(local_name=u"dynamic_allocation_enabled", remote_name=u"dynamicAllocationEnabled", attribute_type=bool)
        self.expose_attribute(local_name=u"mac", remote_name=u"MAC", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"ipreservation"

    # REST methods
