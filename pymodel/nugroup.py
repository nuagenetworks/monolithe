# -*- coding: utf-8 -*-
from .autogenerates import NUGroup as AutoGenerate
from constants import UserRole


class NUGroup(AutoGenerate):
    """ Represents a Group object """

    def __init__(self):
        """ Initializing object """

        super(NUGroup, self).__init__()
        self.can_delete_children = True

        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, can_order=True, can_search=True)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, min_length=1, max_length=255, is_unique=True, can_order=True, can_search=True)
        self.expose_attribute(local_name=u"private", remote_name=u"private", attribute_type=bool, can_order=True, can_search=True)
        self.expose_attribute(local_name=u"role", remote_name=u"role", attribute_type=str, choices=[UserRole.CSPROOT, UserRole.CSPOPERATOR, UserRole.ORGADMIN, UserRole.ORGNETWORKDESIGNER, UserRole.ORGUSER, UserRole.USER])

    def create_user(self, user, async=False, callback=None):
        """ DO NOT USE """

        pass  # NOTE: Should do nothing because we use set_users instead

    def delete_user(self, user, async=False, callback=None):
        """ DO NOT USE """

        pass  # NOTE: Should do nothing because we use set_users instead

    def set_users(self, users, async=False, callback=None):
        """ Assign a user to this group """

        from courgette.models import NUUser
        return self.set_entities(entities=users, entity_type=NUUser, async=async, callback=callback)
