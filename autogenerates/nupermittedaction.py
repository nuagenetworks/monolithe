# -*- coding: utf-8 -*-

from ..fetchers import NUEventLogsFetcher

from restnuage import NURESTObject


class NUPermittedAction(NURESTObject):
    """ Represents a PermittedAction object """

    def __init__(self):
        """ Initializing object """

        super(NUPermittedAction, self).__init__()

        # Read/Write Attributes
        
        self.permitted_entity_id = None
        self.name = None
        self.permitted_action = None
        self.permitted_entity_description = None
        self.permitted_entity_name = None
        self.permitted_entity_type = None
        
        self.expose_attribute(local_name=u"permitted_entity_id", remote_name=u"permittedEntityID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_action", remote_name=u"permittedAction", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_entity_description", remote_name=u"permittedEntityDescription", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_entity_name", remote_name=u"permittedEntityName", attribute_type=str)
        self.expose_attribute(local_name=u"permitted_entity_type", remote_name=u"permittedEntityType", attribute_type=str)

        # Fetchers
        
        self.eventlogs = []
        self._eventlogs_fetcher = NUEventLogsFetcher.fetcher_with_entity(entity=self, local_name=u"eventlogs")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"permission"

    # REST methods
    
    def create_eventlog(self, eventlog, async=False, callback=None):
        """ Create a eventlog
            :param eventlog: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=eventlog, async=async, callback=callback)

    def delete_eventlog(self, eventlog, async=False, callback=None):
        """ Removes a eventlog
            :param eventlog: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=eventlog, async=async, callback=callback)

    def fetch_eventlogs(self, filter=None, page=None, order_by=None):
        """ Fetch EventLogs """

        if order_by:
            self._eventlogs_fetcher.order_by = order_by

        return self._eventlogs_fetcher.fetch_matching_entities(filter=filter, page=page)
    