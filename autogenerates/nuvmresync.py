# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUVMResync(NURESTObject):
    """ Represents a VMResync object """

    def __init__(self):
        """ Initializing object """

        super(NUVMResync, self).__init__()

        # Read/Write Attributes
        
        self.last_request_timestamp = None
        self.last_time_resync_initiated = None
        self.status = None
        
        self.expose_attribute(local_name=u"last_request_timestamp", remote_name=u"lastRequestTimestamp", attribute_type=str)
        self.expose_attribute(local_name=u"last_time_resync_initiated", remote_name=u"lastTimeResyncInitiated", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"resyn"

    # REST methods
    