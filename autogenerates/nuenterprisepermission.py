# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUEnterprisePermission(NURESTObject):
    """ Represents a EnterprisePermission object """

    def __init__(self):
        """ Initializing object """

        super(NUEnterprisePermission, self).__init__()

        # Read/Write Attributes
        
        self.permitted_entity_id = None
        self.name = None
        self.permitted_action = None
        self.permitted_entity_description = None
        self.permitted_entity_name = None
        self.permitted_entity_type = None
        
        self.expose_attribute(local_name=u"permitted_entity_id", remote_name=u"permittedEntityID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_entity_description", remote_name=u"permittedEntityDescription", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_entity_name", remote_name=u"permittedEntityName", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_entity_type", remote_name=u"permittedEntityType", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"enterprisepermission"

    # REST methods
    