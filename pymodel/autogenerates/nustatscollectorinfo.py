# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUStatsCollectorInfo(NURESTObject):
    """ Represents a StatsCollectorInfo object """

    def __init__(self):
        """ Initializing object """

        super(NUStatsCollectorInfo, self).__init__()

        # Read/Write Attributes

        self.ip_address = None
        self.port = None

        self.expose_attribute(local_name=u"ip_address", remote_name=u"ipAddress", attribute_type=str)
        self.expose_attribute(local_name=u"port", remote_name=u"port", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"statisticscollecto"

    # REST methods
