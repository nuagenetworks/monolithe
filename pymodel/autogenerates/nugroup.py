# -*- coding: utf-8 -*-

from ..fetchers import NUUsersFetcher

from restnuage import NURESTObject


class NUGroup(NURESTObject):
    """ Represents a Group object """

    def __init__(self):
        """ Initializing object """

        super(NUGroup, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.name = None
        self.private = None
        self.role = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"private", remote_name=u"private", attribute_type=bool)
        self.expose_attribute(local_name=u"role", remote_name=u"role", attribute_type=str)

        # Fetchers
        
        self.users = []
        self._users_fetcher = NUUsersFetcher.fetcher_with_entity(entity=self, local_name=u"users")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"group"

    # REST methods
    
    def create_user(self, user, async=False, callback=None):
        """ Create a user
            :param user: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=user, async=async, callback=callback)

    def delete_user(self, user, async=False, callback=None):
        """ Removes a user
            :param user: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=user, async=async, callback=callback)

    def fetch_users(self, filter=None, page=None, order_by=None):
        """ Fetch Users """

        if order_by:
            self._users_fetcher.order_by = order_by

        return self._users_fetcher.fetch_matching_entities(filter=filter, page=page)
    