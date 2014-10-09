# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NULocation(NURESTObject):
    """ Represents a Location object """

    def __init__(self):
        """ Initializing object """

        super(NULocation, self).__init__()

        # Read/Write Attributes
        
        self.address = None
        self.country = None
        self.latitude = None
        self.locality = None
        self.longitude = None
        self.state = None
        
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"country", remote_name=u"country", attribute_type=str)
        self.expose_attribute(local_name=u"latitude", remote_name=u"latitude", attribute_type=float)
        self.expose_attribute(local_name=u"locality", remote_name=u"locality", attribute_type=str)
        self.expose_attribute(local_name=u"longitude", remote_name=u"longitude", attribute_type=float)
        self.expose_attribute(local_name=u"state", remote_name=u"state", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"location"

    # REST methods
    