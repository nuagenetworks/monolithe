# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUAlarm(NURESTObject):
    """ Represents a Alarm object """

    def __init__(self):
        """ Initializing object """

        super(NUAlarm, self).__init__()

        # Read/Write Attributes

        self.acknowledged = None
        self.target_object = None
        self.timestamp = None
        self.description = None
        self.enterprise_id = None
        self.error_condition = None
        self.name = None
        self.number_of_occurances = None
        self.reason = None
        self.severity = None

        self.expose_attribute(local_name=u"acknowledged", remote_name=u"acknowledged", attribute_type=bool)
        self.expose_attribute(local_name=u"target_object", remote_name=u"targetObject", attribute_type=str)
        self.expose_attribute(local_name=u"timestamp", remote_name=u"timestamp", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str)
        self.expose_attribute(local_name=u"error_condition", remote_name=u"errorCondition", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"number_of_occurances", remote_name=u"numberOfOccurances", attribute_type=int)
        self.expose_attribute(local_name=u"reason", remote_name=u"reason", attribute_type=str)
        self.expose_attribute(local_name=u"severity", remote_name=u"severity", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"alarm"

    # REST methods
