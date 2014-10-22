# -*- coding: utf-8 -*-

from ..fetchers import NUSubNetworksFetcher
from ..fetchers import NUVirtualMachinesFetcher

from bambou import NURESTObject


class NUApplication(NURESTObject):
    """ Represents a Application object """

    def __init__(self):
        """ Initializing object """

        super(NUApplication, self).__init__()

        # Read/Write Attributes

        self.name = None

        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers

        self.subnets = []
        self._subnets_fetcher = NUSubNetworksFetcher.fetcher_with_entity(entity=self, local_name=u"subnets")

        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"app"

    # REST methods

    def create_subnet(self, subnet, async=False, callback=None):
        """ Create a subnet
            :param subnet: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=subnet, async=async, callback=callback)

    def delete_subnet(self, subnet, async=False, callback=None):
        """ Removes a subnet
            :param subnet: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=subnet, async=async, callback=callback)

    def fetch_subnets(self, filter=None, page=None, order_by=None):
        """ Fetch SubNetworks """

        if order_by:
            self._subnets_fetcher.order_by = order_by

        return self._subnets_fetcher.fetch_matching_entities(filter=filter, page=page)

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
