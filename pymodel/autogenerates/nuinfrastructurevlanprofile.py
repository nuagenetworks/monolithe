# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUInfrastructureVlanProfile(NURESTObject):
    """ Represents a InfrastructureVlanProfile object """

    def __init__(self):
        """ Initializing object """

        super(NUInfrastructureVlanProfile, self).__init__()

        # Read/Write Attributes

        self.qos_profile = None
        self.vlan = None
        self.description = None
        self.enterprise_id = None
        self.name = None

        self.expose_attribute(local_name=u"qos_profile", remote_name=u"qosProfile", attribute_type=str)
        self.expose_attribute(local_name=u"vlan", remote_name=u"vlan", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"infrastructurevlanprofile"

    # REST methods
