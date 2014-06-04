# -*- coding:utf-8 -*-

from restnuage.nurest_object import NURESTObject


class NUUser(NURESTObject):
    """ Defines a group """

    def __init__(self):
        """ Initialize a new object """

        super(NUUser, self).__init__()

        # Read/Write Attributes
        self.username = None
        self.firstname = None
        self.lastname = None
        self.email = None
        self.password = None
        self.password_confirm = None
        self.avatar_data = None
        self.avatar_type = None

        self.expose_attribute(local_name=u'username', remote_name=u'userName', attribute_type=str, is_required=True, max_length=255)
        self.expose_attribute(local_name=u'firstname', remote_name=u'firstName', attribute_type=str, is_required=True, max_length=255)
        self.expose_attribute(local_name=u'lastname', remote_name=u'lastName', attribute_type=str, is_required=True, max_length=255)
        self.expose_attribute(local_name=u'email', attribute_type=str, is_required=True, max_length=255)
        self.expose_attribute(local_name=u'password', attribute_type=str, is_required=True, max_length=255)
        self.expose_attribute(local_name=u'password_confirm', remote_name=u'passwordConfirm', attribute_type=str, is_required=True, max_length=255)
        self.expose_attribute(local_name=u'avatar_data', remote_name=u'avatarData', attribute_type=str)
        self.expose_attribute(local_name=u'avatar_type', remote_name=u'avatarType', attribute_type=str)

        # Read-only attributes

        # Fetchers

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"user"
