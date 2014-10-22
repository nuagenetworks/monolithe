# -*- coding: utf-8 -*-

from ..fetchers import NUIngressACLTemplateEntriesFetcher
from ..fetchers import NUVirtualMachinesFetcher

from bambou import NURESTObject


class NUIngressACLTemplate(NURESTObject):
    """ Represents a IngressACLTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUIngressACLTemplate, self).__init__()

        # Read/Write Attributes

        self.allow_l2_address_spoof = None
        self.assoc_acl_template_id = None
        self.default_allow_ip = None
        self.default_allow_non_ip = None
        self.description = None
        self.name = None
        self.active = None

        self.expose_attribute(local_name=u"allow_l2_address_spoof", remote_name=u"allowL2AddressSpoof", attribute_type=bool)
        self.expose_attribute(local_name=u"assoc_acl_template_id", remote_name=u"assocAclTemplateId", attribute_type=str)
        self.expose_attribute(local_name=u"default_allow_ip", remote_name=u"defaultAllowIP", attribute_type=bool)
        self.expose_attribute(local_name=u"default_allow_non_ip", remote_name=u"defaultAllowNonIP", attribute_type=bool)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool)

        # Fetchers

        self.ingressaclentrytemplates = []
        self._ingressaclentrytemplates_fetcher = NUIngressACLTemplateEntriesFetcher.fetcher_with_entity(entity=self, local_name=u"ingressaclentrytemplates")

        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"ingressacltemplate"

    # REST methods

    def create_ingressaclentrytemplate(self, ingressaclentrytemplate, async=False, callback=None):
        """ Create a ingressaclentrytemplate
            :param ingressaclentrytemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ingressaclentrytemplate, async=async, callback=callback)

    def delete_ingressaclentrytemplate(self, ingressaclentrytemplate, async=False, callback=None):
        """ Removes a ingressaclentrytemplate
            :param ingressaclentrytemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ingressaclentrytemplate, async=async, callback=callback)

    def fetch_ingressaclentrytemplates(self, filter=None, page=None, order_by=None):
        """ Fetch IngressACLTemplateEntries """

        if order_by:
            self._ingressaclentrytemplates_fetcher.order_by = order_by

        return self._ingressaclentrytemplates_fetcher.fetch_matching_entities(filter=filter, page=page)

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
