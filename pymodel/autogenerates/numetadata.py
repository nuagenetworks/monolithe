# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUMetadata(NURESTObject):
    """ Represents a Metadata object """

    def __init__(self):
        """ Initializing object """

        super(NUMetadata, self).__init__()

        # Read/Write Attributes

        self.metadata = None
        self.resource_type = None

        self.expose_attribute(local_name=u"metadata", remote_name=u"metadata", attribute_type=str)
        self.expose_attribute(local_name=u"resource_type", remote_name=u"resourceType", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"metadat"

    # REST methods
