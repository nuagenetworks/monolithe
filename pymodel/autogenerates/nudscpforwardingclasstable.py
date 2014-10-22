# -*- coding: utf-8 -*-

from ..fetchers import NUDSCPForwardingClassMappingsFetcher

from bambou import NURESTObject


class NUDSCPForwardingClassTable(NURESTObject):
    """ Represents a DSCPForwardingClassTable object """

    def __init__(self):
        """ Initializing object """

        super(NUDSCPForwardingClassTable, self).__init__()

        # Read/Write Attributes

        self.description = None
        self.name = None

        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers

        self.dscpforwardingclassmappings = []
        self._dscpforwardingclassmappings_fetcher = NUDSCPForwardingClassMappingsFetcher.fetcher_with_entity(entity=self, local_name=u"dscpforwardingclassmappings")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"dscpforwardingclasstable"

    # REST methods

    def create_dscpforwardingclassmapping(self, dscpforwardingclassmapping, async=False, callback=None):
        """ Create a dscpforwardingclassmapping
            :param dscpforwardingclassmapping: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=dscpforwardingclassmapping, async=async, callback=callback)

    def delete_dscpforwardingclassmapping(self, dscpforwardingclassmapping, async=False, callback=None):
        """ Removes a dscpforwardingclassmapping
            :param dscpforwardingclassmapping: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=dscpforwardingclassmapping, async=async, callback=callback)

    def fetch_dscpforwardingclassmappings(self, filter=None, page=None, order_by=None):
        """ Fetch DSCPForwardingClassMappings """

        if order_by:
            self._dscpforwardingclassmappings_fetcher.order_by = order_by

        return self._dscpforwardingclassmappings_fetcher.fetch_matching_entities(filter=filter, page=page)
