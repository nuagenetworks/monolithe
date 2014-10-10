# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUPolicyGroupTemplate(NURESTObject):
    """ Represents a PolicyGroupTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUPolicyGroupTemplate, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.name = None
        self.type = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"policygrouptemplate"

    # REST methods
    