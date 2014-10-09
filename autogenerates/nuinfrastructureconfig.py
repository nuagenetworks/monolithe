# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUInfrastructureConfig(NURESTObject):
    """ Represents a InfrastructureConfig object """

    def __init__(self):
        """ Initializing object """

        super(NUInfrastructureConfig, self).__init__()

        # Read/Write Attributes
        
        self.gateway = None
        
        self.expose_attribute(local_name=u"gateway", remote_name=u"gateway", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"infraconfi"

    # REST methods
    