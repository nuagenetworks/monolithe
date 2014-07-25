# -*- coding: utf-8 -*-

from ..fetchers import NUApplicationsFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUVirtualMachinesFetcher

from restnuage import NURESTObject


class NUUser(NURESTObject):
    """ Represents a User object """

    def __init__(self):
        """ Initializing object """

        super(NUUser, self).__init__()

        # Read/Write Attributes
        
        self.avatar_data = None
        self.avatar_type = None
        self.email = None
        self.first_name = None
        self.last_name = None
        self.password = None
        self.user_name = None
        
        self.expose_attribute(local_name=u"avatar_data", remote_name=u"avatarData", attribute_type=str)
        self.expose_attribute(local_name=u"avatar_type", remote_name=u"avatarType", attribute_type=str)
        self.expose_attribute(local_name=u"email", remote_name=u"email", attribute_type=str)
        self.expose_attribute(local_name=u"first_name", remote_name=u"firstName", attribute_type=str)
        self.expose_attribute(local_name=u"last_name", remote_name=u"lastName", attribute_type=str)
        self.expose_attribute(local_name=u"password", remote_name=u"password", attribute_type=str)
        self.expose_attribute(local_name=u"user_name", remote_name=u"userName", attribute_type=str)

        # Fetchers
        
        self.apps = []
        self._apps_fetcher = NUApplicationsFetcher.fetcher_with_entity(entity=self, local_name=u"apps")
        
        self.groups = []
        self._groups_fetcher = NUGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"groups")
        
        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"user"

    # REST methods
    
    def create_app(self, app, async=False, callback=None):
        """ Create a app
            :param app: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=app, async=async, callback=callback)

    def delete_app(self, app, async=False, callback=None):
        """ Removes a app
            :param app: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=app, async=async, callback=callback)

    def fetch_apps(self, filter=None, page=None, order_by=None):
        """ Fetch Applications """

        if order_by:
            self._apps_fetcher.order_by = order_by

        return self._apps_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_group(self, group, async=False, callback=None):
        """ Create a group
            :param group: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=group, async=async, callback=callback)

    def delete_group(self, group, async=False, callback=None):
        """ Removes a group
            :param group: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=group, async=async, callback=callback)

    def fetch_groups(self, filter=None, page=None, order_by=None):
        """ Fetch Groups """

        if order_by:
            self._groups_fetcher.order_by = order_by

        return self._groups_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_vm(self, vm, async=False, callback=None):
        """ Create a vm
            :param vm: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vm, async=async, callback=callback)

    def delete_vm(self, vm, async=False, callback=None):
        """ Removes a vm
            :param vm: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vm, async=async, callback=callback)

    def fetch_vms(self, filter=None, page=None, order_by=None):
        """ Fetch VirtualMachines """

        if order_by:
            self._vms_fetcher.order_by = order_by

        return self._vms_fetcher.fetch_matching_entities(filter=filter, page=page)
    