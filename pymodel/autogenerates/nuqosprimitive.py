# -*- coding: utf-8 -*-

from ..fetchers import NUVirtualMachinesFetcher

from bambou import NURESTObject


class NUQosPrimitive(NURESTObject):
    """ Represents a QosPrimitive object """

    def __init__(self):
        """ Initializing object """

        super(NUQosPrimitive, self).__init__()

        # Read/Write Attributes

        self.associated_dscp_forwarding_class_table_id = None
        self.associated_dscp_forwarding_class_table_name = None
        self.assoc_qos_id = None
        self.bum_committed_burst_size = None
        self.bum_committed_information_rate = None
        self.bum_peak_burst_size = None
        self.bum_peak_information_rate = None
        self.bum_rate_limiting_active = None
        self.burst = None
        self.committed_burst_size = None
        self.committed_information_rate = None
        self.description = None
        self.name = None
        self.peak = None
        self.rate_limiting_active = None
        self.rewrite_forwarding_class = None
        self.service_class = None
        self.trusted_forwarding_class = None
        self.active = None

        self.expose_attribute(local_name=u"associated_dscp_forwarding_class_table_id", remote_name=u"associatedDSCPForwardingClassTableID", attribute_type=str)
        self.expose_attribute(local_name=u"associated_dscp_forwarding_class_table_name", remote_name=u"associatedDSCPForwardingClassTableName", attribute_type=str)
        self.expose_attribute(local_name=u"assoc_qos_id", remote_name=u"assocQosId", attribute_type=str)
        self.expose_attribute(local_name=u"bum_committed_burst_size", remote_name=u"BUMCommittedBurstSize", attribute_type=str)
        self.expose_attribute(local_name=u"bum_committed_information_rate", remote_name=u"BUMCommittedInformationRate", attribute_type=str)
        self.expose_attribute(local_name=u"bum_peak_burst_size", remote_name=u"BUMPeakBurstSize", attribute_type=str)
        self.expose_attribute(local_name=u"bum_peak_information_rate", remote_name=u"BUMPeakInformationRate", attribute_type=str)
        self.expose_attribute(local_name=u"bum_rate_limiting_active", remote_name=u"BUMRateLimitingActive", attribute_type=bool)
        self.expose_attribute(local_name=u"burst", remote_name=u"burst", attribute_type=str)
        self.expose_attribute(local_name=u"committed_burst_size", remote_name=u"committedBurstSize", attribute_type=str)
        self.expose_attribute(local_name=u"committed_information_rate", remote_name=u"committedInformationRate", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"peak", remote_name=u"peak", attribute_type=str)
        self.expose_attribute(local_name=u"rate_limiting_active", remote_name=u"rateLimitingActive", attribute_type=bool)
        self.expose_attribute(local_name=u"rewrite_forwarding_class", remote_name=u"rewriteForwardingClass", attribute_type=bool)
        self.expose_attribute(local_name=u"service_class", remote_name=u"serviceClass", attribute_type=str)
        self.expose_attribute(local_name=u"trusted_forwarding_class", remote_name=u"trustedForwardingClass", attribute_type=bool)
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool)

        # Fetchers

        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"qo"

    # REST methods

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
