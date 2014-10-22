# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUBGPPeer(NURESTObject):
    """ Represents a BGPPeer object """

    def __init__(self):
        """ Initializing object """

        super(NUBGPPeer, self).__init__()

        # Read/Write Attributes

        self.address = None
        self.last_state_change = None
        self.status = None

        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"last_state_change", remote_name=u"lastStateChange", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"bgppeer"

    # REST methods
