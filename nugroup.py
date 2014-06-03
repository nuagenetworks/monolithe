# -*- coding:utf-8 -*-

from restnuage.nurest_object import NURESTObject


class NUGroup(NURESTObject):
    """ Defines a group """

    def __init__(self):
        """ Initialize a new object """

        super(NUGroup, self).__init__()

        # Read/Write Attributes
        self.name = None
        self.description = None
        self.is_private = bool()
        self.role = None

        self.users = []

        self.expose_attribute(local_name=u'name', attribute_type=str)
        self.expose_attribute(local_name=u'description', attribute_type=str)
        self.expose_attribute(local_name=u'is_private', remote_name=u'private', attribute_type=str)
        self.expose_attribute(local_name=u'role', attribute_type=str)

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"group"
