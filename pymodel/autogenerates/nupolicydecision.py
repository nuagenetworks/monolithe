# -*- coding: utf-8 -*-

from ..fetchers import NUQosPrimitivesFetcher

from bambou import NURESTObject


class NUPolicyDecision(NURESTObject):
    """ Represents a PolicyDecision object """

    def __init__(self):
        """ Initializing object """

        super(NUPolicyDecision, self).__init__()

        # Read/Write Attributes

        self.egress_ac_ls = None
        self.ingress_ac_ls = None
        self.ingress_adv_fwd = None
        self.qos = None
        self.stats = None

        self.expose_attribute(local_name=u"egress_ac_ls", remote_name=u"egressACLs", attribute_type=str)
        self.expose_attribute(local_name=u"ingress_ac_ls", remote_name=u"ingressACLs", attribute_type=str)
        self.expose_attribute(local_name=u"ingress_adv_fwd", remote_name=u"ingressAdvFwd", attribute_type=str)
        self.expose_attribute(local_name=u"qos", remote_name=u"qos", attribute_type=str)
        self.expose_attribute(local_name=u"stats", remote_name=u"stats", attribute_type=str)

        # Fetchers

        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"policydecision"

    # REST methods

    def create_qo(self, qo, async=False, callback=None):
        """ Create a qo
            :param qo: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=qo, async=async, callback=callback)

    def delete_qo(self, qo, async=False, callback=None):
        """ Removes a qo
            :param qo: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=qo, async=async, callback=callback)

    def fetch_qos(self, filter=None, page=None, order_by=None):
        """ Fetch QosPrimitives """

        if order_by:
            self._qos_fetcher.order_by = order_by

        return self._qos_fetcher.fetch_matching_entities(filter=filter, page=page)
