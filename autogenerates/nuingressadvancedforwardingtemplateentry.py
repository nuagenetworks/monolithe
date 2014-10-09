# -*- coding: utf-8 -*-


from restnuage import NURESTObject


class NUIngressAdvancedForwardingTemplateEntry(NURESTObject):
    """ Represents a IngressAdvancedForwardingTemplateEntry object """

    def __init__(self):
        """ Initializing object """

        super(NUIngressAdvancedForwardingTemplateEntry, self).__init__()

        # Read/Write Attributes
        
        self.fc_override = None
        self.redirect_v_port_tag_id = None
        self.action = None
        self.address_override = None
        self.associated_application_id = None
        self.associated_application_object_id = None
        self.associated_application_object_type = None
        self.description = None
        self.destination_port = None
        self.dscp = None
        self.ether_type = None
        self.location_id = None
        self.location_type = None
        self.network_id = None
        self.network_type = None
        self.priority = None
        self.protocol = None
        self.source_port = None
        
        self.expose_attribute(local_name=u"fc_override", remote_name=u"FCOverride", attribute_type=str)
        self.expose_attribute(local_name=u"redirect_v_port_tag_id", remote_name=u"redirectVPortTagID", attribute_type=str)
        self.expose_attribute(local_name=u"action", remote_name=u"action", attribute_type=str)
        self.expose_attribute(local_name=u"address_override", remote_name=u"addressOverride", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_id", remote_name=u"associatedApplicationID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_object_id", remote_name=u"associatedApplicationObjectID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_application_object_type", remote_name=u"associatedApplicationObjectType", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"destination_port", remote_name=u"destinationPort", attribute_type=str)
        self.expose_attribute(local_name=u"dscp", remote_name=u"DSCP", attribute_type=str)
        self.expose_attribute(local_name=u"ether_type", remote_name=u"etherType", attribute_type=str)
        self.expose_attribute(local_name=u"location_id", remote_name=u"locationID", attribute_type=str)
        self.expose_attribute(local_name=u"location_type", remote_name=u"locationType", attribute_type=str)
        self.expose_attribute(local_name=u"network_id", remote_name=u"networkID", attribute_type=str)
        self.expose_attribute(local_name=u"network_type", remote_name=u"networkType", attribute_type=str)
        self.expose_attribute(local_name=u"priority", remote_name=u"priority", attribute_type=int)
        self.expose_attribute(local_name=u"protocol", remote_name=u"protocol", attribute_type=str)
        self.expose_attribute(local_name=u"source_port", remote_name=u"sourcePort", attribute_type=str)

        # Fetchers
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"ingressadvfwdentrytemplate"

    # REST methods
    