# -*- coding: utf-8 -*-

from bambou import NURESTObject


class NURedirectionTargetTemplate(NURESTObject):
    """ Represents a RedirectionTargetTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NURedirectionTargetTemplate, self).__init__()

        # Read/Write Attributes

        self.description = None
        self.end_point_type = None
        self.name = None
        self.redundancy_enabled = None
        self.trigger_type = None

        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"end_point_type", remote_name=u"endPointType", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"redundancy_enabled", remote_name=u"redundancyEnabled", attribute_type=bool)
        self.expose_attribute(local_name=u"trigger_type", remote_name=u"triggerType", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"redirectiontargettemplate"

    # REST methods
