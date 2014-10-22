# -*- coding: utf-8 -*-


from bambou import NURESTObject
from time import time

class NUEventLog(NURESTObject):
    """ Represents a EventLog object """

    def __init__(self):
        """ Initializing object """

        super(NUEventLog, self).__init__()

        # Read/Write Attributes

        self.diff = None
        self.enterprise = None
        self.entities = None
        self.entity_id = None
        self.entity_parent_id = None
        self.entity_parent_type = None
        self.entity_type = None
        self.event_received_time = None
        self.type = None
        self.user = None

        self.expose_attribute(local_name=u"diff", remote_name=u"diff", attribute_type=str)
        self.expose_attribute(local_name=u"enterprise", remote_name=u"enterprise", attribute_type=str)
        self.expose_attribute(local_name=u"entities", remote_name=u"entities", attribute_type=str)
        self.expose_attribute(local_name=u"entity_id", remote_name=u"entityID", attribute_type=str)
        self.expose_attribute(local_name=u"entity_parent_id", remote_name=u"entityParentID", attribute_type=str)
        self.expose_attribute(local_name=u"entity_parent_type", remote_name=u"entityParentType", attribute_type=str)
        self.expose_attribute(local_name=u"entity_type", remote_name=u"entityType", attribute_type=str)
        self.expose_attribute(local_name=u"event_received_time", remote_name=u"eventReceivedTime", attribute_type=time)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)
        self.expose_attribute(local_name=u"user", remote_name=u"user", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"eventlog"

    # REST methods
