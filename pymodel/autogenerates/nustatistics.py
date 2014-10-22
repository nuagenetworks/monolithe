# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUStatistics(NURESTObject):
    """ Represents a Statistics object """

    def __init__(self):
        """ Initializing object """

        super(NUStatistics, self).__init__()

        # Read/Write Attributes

        self.end_time = None
        self.number_of_data_points = None
        self.start_time = None
        self.stats_data = None
        self.version = None

        self.expose_attribute(local_name=u"end_time", remote_name=u"endTime", attribute_type=str)
        self.expose_attribute(local_name=u"number_of_data_points", remote_name=u"numberOfDataPoints", attribute_type=int)
        self.expose_attribute(local_name=u"start_time", remote_name=u"startTime", attribute_type=str)
        self.expose_attribute(local_name=u"stats_data", remote_name=u"statsData", attribute_type=str)
        self.expose_attribute(local_name=u"version", remote_name=u"version", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"statistic"

    # REST methods
