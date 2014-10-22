# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUJob(NURESTObject):
    """ Represents a Job object """

    def __init__(self):
        """ Initializing object """

        super(NUJob, self).__init__()

        # Read/Write Attributes

        self.assoc_entity_type = None
        self.command = None
        self.parameter = None
        self.progress = None
        self.result = None
        self.status = None

        self.expose_attribute(local_name=u"assoc_entity_type", remote_name=u"assocEntityType", attribute_type=str)
        self.expose_attribute(local_name=u"command", remote_name=u"command", attribute_type=str)
        self.expose_attribute(local_name=u"parameter", remote_name=u"parameter", attribute_type=str)
        self.expose_attribute(local_name=u"progress", remote_name=u"progress", attribute_type=float)
        self.expose_attribute(local_name=u"result", remote_name=u"result", attribute_type=str)
        self.expose_attribute(local_name=u"status", remote_name=u"status", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"job"

    # REST methods
