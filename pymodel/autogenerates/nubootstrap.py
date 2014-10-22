# -*- coding: utf-8 -*-


from bambou import NURESTObject
from time import time

class NUBootstrap(NURESTObject):
    """ Represents a Bootstrap object """

    def __init__(self):
        """ Initializing object """

        super(NUBootstrap, self).__init__()

        # Read/Write Attributes

        self.expiry = None
        self.hash = None
        self.installer_id = None
        self.seed = None
        self.status = None

        self.expose_attribute(local_name=u"expiry", remote_name=u"expiry", attribute_type=time)
        self.expose_attribute(local_name=u"hash", remote_name=u"hash", attribute_type=str)
        self.expose_attribute(local_name=u"installer_id", remote_name=u"installerID", attribute_type=str)
        self.expose_attribute(local_name=u"seed", remote_name=u"seed", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"bootstrap"

    # REST methods
