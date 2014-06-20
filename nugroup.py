# -*- coding:utf-8 -*-

from restnuage import NURESTObject

from .fetchers import NUUsersFetcher


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

        # Fetchers
        self._users_fetcher = NUUsersFetcher.fetcher_with_entity(entity=self, local_name=u'users')

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"group"

    # REST methods

    def assign_users(self, users, async=False, callback=None):
        """ Assign a user to this group """

        from courgette.models import NUUser
        return self.set_entities(entities=users, entity_type=NUUser, async=async, callback=callback)

    def fetch_users(self):
        """ Fetch users """

        return self._users_fetcher.fetch_entities()
