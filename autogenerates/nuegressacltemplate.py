# -*- coding: utf-8 -*-

from ..fetchers import NUEgressACLTemplateEntriesFetcher
from ..fetchers import NUVirtualMachinesFetcher

from restnuage import NURESTObject


class NUEgressACLTemplate(NURESTObject):
    """ Represents a EgressACLTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUEgressACLTemplate, self).__init__()

        # Read/Write Attributes
        
        self.default_allow_ip = None
        self.default_allow_non_ip = None
        self.description = None
        self.name = None
        self.active = None
        
        self.expose_attribute(local_name=u"default_allow_ip", remote_name=u"defaultAllowIP", attribute_type=bool)
        self.expose_attribute(local_name=u"default_allow_non_ip", remote_name=u"defaultAllowNonIP", attribute_type=bool)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool)

        # Fetchers
        
        self.egressaclentrytemplates = []
        self._egressaclentrytemplates_fetcher = NUEgressACLTemplateEntriesFetcher.fetcher_with_entity(entity=self, local_name=u"egressaclentrytemplates")
        
        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"egressacltemplate"

    # REST methods
    
    def create_egressaclentrytemplate(self, egressaclentrytemplate, async=False, callback=None):
        """ Create a egressaclentrytemplate
            :param egressaclentrytemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=egressaclentrytemplate, async=async, callback=callback)

    def delete_egressaclentrytemplate(self, egressaclentrytemplate, async=False, callback=None):
        """ Removes a egressaclentrytemplate
            :param egressaclentrytemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=egressaclentrytemplate, async=async, callback=callback)

    def fetch_egressaclentrytemplates(self, filter=None, page=None, order_by=None):
        """ Fetch EgressACLTemplateEntries """

        if order_by:
            self._egressaclentrytemplates_fetcher.order_by = order_by

        return self._egressaclentrytemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    