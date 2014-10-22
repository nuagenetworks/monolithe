# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUBootstrapActivation(NURESTObject):
    """ Represents a BootstrapActivation object """

    def __init__(self):
        """ Initializing object """

        super(NUBootstrapActivation, self).__init__()

        # Read/Write Attributes

        self.action = None
        self.status = None
        self.cacert = None
        self.cert = None
        self.config_url = None
        self.csr = None
        self.hash = None
        self.seed = None

        self.expose_attribute(local_name=u"action", remote_name=u"action", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)
        self.expose_attribute(local_name=u"cacert", remote_name=u"cacert", attribute_type=str)
        self.expose_attribute(local_name=u"cert", remote_name=u"cert", attribute_type=str)
        self.expose_attribute(local_name=u"config_url", remote_name=u"configURL", attribute_type=str)
        self.expose_attribute(local_name=u"csr", remote_name=u"csr", attribute_type=str)
        self.expose_attribute(local_name=u"hash", remote_name=u"hash", attribute_type=str)
        self.expose_attribute(local_name=u"seed", remote_name=u"seed", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"bootstrapactivation"

    # REST methods
