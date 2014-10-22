# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUFlowSecurityPolicy(NURESTObject):
    """ Represents a FlowSecurityPolicy object """

    def __init__(self):
        """ Initializing object """

        super(NUFlowSecurityPolicy, self).__init__()

        # Read/Write Attributes

        self.action = None
        self.priority = None
        self.associated_network_object_id = None
        self.associated_network_object_type = None
        self.destination_address_overwrite = None
        self.flow_id = None
        self.associated_application_service_id = None
        self.source_address_overwrite = None

        self.expose_attribute(local_name=u"action", remote_name=u"action", attribute_type=str)
        self.expose_attribute(local_name=u"priority", remote_name=u"priority", attribute_type=int)
        self.expose_attribute(local_name=u"associated_network_object_id", remote_name=u"associatedNetworkObjectID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_network_object_type", remote_name=u"associatedNetworkObjectType", attribute_type=str)
        self.expose_attribute(local_name=u"destination_address_overwrite", remote_name=u"destinationAddressOverwrite", attribute_type=str)
        self.expose_attribute(local_name=u"flow_id", remote_name=u"flowID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_service_id", remote_name=u"associatedApplicationServiceID", attribute_type=str)
        self.expose_attribute(local_name=u"source_address_overwrite", remote_name=u"sourceAddressOverwrite", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"flowsecuritypolicy"

    # REST methods
