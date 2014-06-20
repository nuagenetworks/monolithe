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

        # TODO: Check if username is a required field and set min/max length according to issues:
        # http://mvjira.mv.usa.alcatel.com/browse/VSD-2866
        # http://mvjira.mv.usa.alcatel.com/browse/VSD-2865
        self.expose_attribute(local_name=u'username', remote_name=u'userName', display_name=u'user name', attribute_type=str, is_required=True, is_editable=False, is_login=True, is_unique=True)
        self.expose_attribute(local_name=u'firstname', remote_name=u'firstName', attribute_type=str, is_required=True, min_length=1, max_length=255)
        self.expose_attribute(local_name=u'lastname', remote_name=u'lastName', attribute_type=str, is_required=True, min_length=1, max_length=255)
        self.expose_attribute(local_name=u'email', attribute_type=str, is_required=True, is_email=True)
        self.expose_attribute(local_name=u'password', attribute_type=str, is_required=True, is_password=True)  # TODO: Put /users/id with password set to None returns 'No changes to modify the entity'
        self.expose_attribute(local_name=u'avatar_data', remote_name=u'avatarData', attribute_type=str)
        self.expose_attribute(local_name=u'avatar_type', remote_name=u'avatarType', attribute_type=str, choices=['BASE64', 'URL'])

        # Read-only attributes

        # Fetchers

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"user"

    def to_NURESTUser(self):
        """ convert NUUser to NURESTUser """

        from . import NURESTUser
        user = NURESTUser()

        for attribute in self.get_attributes():

            if hasattr(user, attribute.local_name):
                value = getattr(self, attribute.local_name)
                setattr(user, attribute.local_name, value)

        return user

        