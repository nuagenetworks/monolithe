# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUVPortMirror(NURESTObject):
    """ Represents a VPortMirror object """

    def __init__(self):
        """ Initializing object """

        super(NUVPortMirror, self).__init__()

        # Read/Write Attributes

        self.attached_network_type = None
        self.domain_name = None
        self.enterpise_name = None
        self.mirror_destination_id = None
        self.mirror_destination_name = None
        self.mirror_direction = None
        self.network_name = None
        self.vport_id = None
        self.v_port_name = None

        self.expose_attribute(local_name=u"attached_network_type", remote_name=u"attachedNetworkType", attribute_type=str)
        self.expose_attribute(local_name=u"domain_name", remote_name=u"domainName", attribute_type=str)
        self.expose_attribute(local_name=u"enterpise_name", remote_name=u"enterpiseName", attribute_type=str)
        self.expose_attribute(local_name=u"mirror_destination_id", remote_name=u"mirrorDestinationID", attribute_type=str)
        self.expose_attribute(local_name=u"mirror_destination_name", remote_name=u"mirrorDestinationName", attribute_type=str)
        self.expose_attribute(local_name=u"mirror_direction", remote_name=u"mirrorDirection", attribute_type=str)
        self.expose_attribute(local_name=u"network_name", remote_name=u"networkName", attribute_type=str)
        self.expose_attribute(local_name=u"vport_id", remote_name=u"vportId", attribute_type=str)
        self.expose_attribute(local_name=u"v_port_name", remote_name=u"VPortName", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vportmirror"

    # REST methods
