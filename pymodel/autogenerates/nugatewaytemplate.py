# -*- coding: utf-8 -*-

from ..fetchers import NUPortTemplatesFetcher

from restnuage import NURESTObject


class NUGatewayTemplate(NURESTObject):
    """ Represents a GatewayTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUGatewayTemplate, self).__init__()

        # Read/Write Attributes
        
        self.enterprise_id = None
        self.description = None
        self.infrastructure_profile_id = None
        self.name = None
        self.personality = None
        
        self.expose_attribute(local_name=u"enterprise_id", remote_name=u"enterpriseID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"infrastructure_profile_id", remote_name=u"infrastructureProfileID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"personality", remote_name=u"personality", attribute_type=str)

        # Fetchers
        
        self.porttemplates = []
        self._porttemplates_fetcher = NUPortTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"porttemplates")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"gatewaytemplate"

    # REST methods
    
    def create_porttemplate(self, porttemplate, async=False, callback=None):
        """ Create a porttemplate
            :param porttemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=porttemplate, async=async, callback=callback)

    def delete_porttemplate(self, porttemplate, async=False, callback=None):
        """ Removes a porttemplate
            :param porttemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=porttemplate, async=async, callback=callback)

    def fetch_porttemplates(self, filter=None, page=None, order_by=None):
        """ Fetch PortTemplates """

        if order_by:
            self._porttemplates_fetcher.order_by = order_by

        return self._porttemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    