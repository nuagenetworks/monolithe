# -*- coding: utf-8 -*-

from ..fetchers import NUVlanTemplatesFetcher

from restnuage import NURESTObject


class NUPortTemplate(NURESTObject):
    """ Represents a PortTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUPortTemplate, self).__init__()

        # Read/Write Attributes
        
        self.name = None
        self.physical_name = None
        self.port_type = None
        self.description = None
        self.infrastructure_profile_id = None
        self.vlan_range = None
        
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"physical_name", remote_name=u"physicalName", attribute_type=str)
        self.expose_attribute(local_name=u"port_type", remote_name=u"portType", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"infrastructure_profile_id", remote_name=u"infrastructureProfileID", attribute_type=str)
        self.expose_attribute(local_name=u"vlan_range", remote_name=u"VLANRange", attribute_type=str)

        # Fetchers
        
        self.vlantemplates = []
        self._vlantemplates_fetcher = NUVlanTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"vlantemplates")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"porttemplate"

    # REST methods
    
    def create_vlantemplate(self, vlantemplate, async=False, callback=None):
        """ Create a vlantemplate
            :param vlantemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vlantemplate, async=async, callback=callback)

    def delete_vlantemplate(self, vlantemplate, async=False, callback=None):
        """ Removes a vlantemplate
            :param vlantemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vlantemplate, async=async, callback=callback)

    def fetch_vlantemplates(self, filter=None, page=None, order_by=None):
        """ Fetch VlanTemplates """

        if order_by:
            self._vlantemplates_fetcher.order_by = order_by

        return self._vlantemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    