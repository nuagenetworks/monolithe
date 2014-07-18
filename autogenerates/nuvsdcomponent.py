# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUVSDComponent(NURESTObject):
    """ Represents a VSDComponent object """

    def __init__(self):
        """ Initializing object """

        super(NUVSDComponent, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.address = None
        self.location = None
        self.management_ip = None
        self.name = None
        self.product_version = None
        self.status = None
        self.type = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"address", remote_name=u"address", attribute_type=str)
        self.expose_attribute(local_name=u"location", remote_name=u"location", attribute_type=str)
        self.expose_attribute(local_name=u"management_ip", remote_name=u"managementIP", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"component"

    # REST methods
    