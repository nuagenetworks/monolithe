# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUVlanTemplate(NURESTObject):
    """ Represents a VlanTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUVlanTemplate, self).__init__()

        # Read/Write Attributes
        
        self.value = None
        self.description = None
        self.infrastructure_profile_id = None
        
        self.expose_attribute(local_name=u"value", remote_name=u"value", attribute_type=int)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"infrastructure_profile_id", remote_name=u"infrastructureProfileID", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vlantemplate"

    # REST methods
    