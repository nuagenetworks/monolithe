# -*- coding: utf-8 -*-
from .autogenerates import NUUser as AutoGenerate


class NUUser(AutoGenerate):
    """ Represents a User object """

    def __init__(self):
        """ Initializing object """

        super(NUUser, self).__init__()

        # TODO: Check if user_name is a required field and set min/max length according to issues:
        # http://mvjira.mv.usa.alcatel.com/browse/VSD-2866
        # http://mvjira.mv.usa.alcatel.com/browse/VSD-2865
        self.expose_attribute(local_name=u"avatar_type", remote_name=u"avatarType", attribute_type=str, choices=['BASE64', 'URL'])
        self.expose_attribute(local_name=u"email", remote_name=u"email", attribute_type=str, is_required=True, is_email=True)
        self.expose_attribute(local_name=u"first_name", remote_name=u"firstName", attribute_type=str, is_required=True, min_length=1, max_length=255)
        self.expose_attribute(local_name=u"last_name", remote_name=u"lastName", attribute_type=str, is_required=True, min_length=1, max_length=255)
        self.expose_attribute(local_name=u"password", remote_name=u"password", attribute_type=str, is_required=True, is_password=True)
        self.expose_attribute(local_name=u"user_name", remote_name=u"userName", attribute_type=str, display_name=u'user name', is_required=True, is_editable=False, is_login=True, is_unique=True, can_order=True, can_search=True)

    def to_NURESTUser(self):
        """ convert NUUser to NURESTUser """

        from . import NURESTUser
        user = NURESTUser()

        for attribute in self.get_attributes():

            if hasattr(user, attribute.local_name):
                value = getattr(self, attribute.local_name)
                setattr(user, attribute.local_name, value)

        return user
