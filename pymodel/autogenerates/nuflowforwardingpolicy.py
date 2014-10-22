# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUFlowForwardingPolicy(NURESTObject):
    """ Represents a FlowForwardingPolicy object """

    def __init__(self):
        """ Initializing object """

        super(NUFlowForwardingPolicy, self).__init__()

        # Read/Write Attributes

        self.redirect_target_id = None
        self.type = None
        self.associated_network_object_id = None
        self.associated_network_object_type = None
        self.destination_address_overwrite = None
        self.flow_id = None
        self.associated_application_service_id = None
        self.source_address_overwrite = None

        self.expose_attribute(local_name=u"redirect_target_id", remote_name=u"redirectTargetID", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)
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

        return u"flowforwardingpolicy"

    # REST methods
