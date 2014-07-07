# -*- coding:utf-8 -*-

# from .fetchers import NUEgressSecurityPoliciesFetcher, NUIngressSecurityPoliciesFetcher, NUForwardingPoliciesFetcher, NUPermissionsFetcher, NUQOSsFetcher
from restnuage import NURESTObject


class NUDomainBase(NURESTObject):
    """ Defines a domain base """

    def __init__(self):
        """ Initialize a new object """

        super(NUDomainBase, self).__init__()

        # Read/Write Attributes
        self.associated_multicast_channel_map_id = None
        self.description = None
        self.is_multicast = bool()
        self.name = None

        self.egress_security_policies = []
        self.forwarding_policies = []
        self.inress_security_policies = []
        self.permissions = []
        self.quoss = []

        self.expose_attribute(local_name=u'associated_multicast_channel_map_id', remote_name=u'associatedMulticastChannelMapID')
        self.expose_attribute(local_name=u'descritpion')
        self.expose_attribute(local_name=u'is_multicast', remote_name=u'multicast')
        self.expose_attribute(local_name=u'name')

        # Fetchers
        # TODO : Write fetchers
        # self.egress_security_policies_fetcher = NUEgressSecurityPoliciesFetcher.fetcher_with_entity(entity=self, local_name=u'egress_security_policies')
        # self.ingress_security_policies_fetcher = NUIngressSecurityPoliciesFetcher.fetcher_with_entity(entity=self, local_name=u'ingress_security_policies_fetcher')
        # self.forwarding_policies_fetcher = NUForwardingPoliciesFetcher.fetcher_with_entity(entity=self, local_name=u'forwarding_policies')
        # self.permissions_fetcher = NUPermissionsFetcher.fetcher_with_entity(entity=self, local_name=u'permissions')
        # self.quoss_fetcher = NUQOSsFetcher.fetcher_with_entity(entity=self, local_name=u'quoss')

    # REST methods

    def create_egress_security_policy(self, egress_security_policy, async=False, callback=None):
        """ Create an egress security policy
            :param egress_security_policy: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=egress_security_policy, async=async, callback=callback)

    def delete_egress_security_policy(self, egress_security_policy, async=False, callback=None):
        """ Delete an egress security policy
            :param egress_security_policy: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=egress_security_policy, async=async, callback=callback)

    def create_ingress_security_policy(self, ingress_security_policy, async=False, callback=None):
        """ Create an ingress security policy
            :param ingress_security_policy: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ingress_security_policy, async=async, callback=callback)

    def delete_ingress_security_policy(self, ingress_security_policy, async=False, callback=None):
        """ Delete an ingress security policy
            :param ingress_security_policy: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ingress_security_policy, async=async, callback=callback)

    def create_forwarding_policy(self, forwarding_policy, async=False, callback=None):
        """ Create an forwarding policy
            :param forwarding_policy: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=forwarding_policy, async=async, callback=callback)

    def delete_forwarding_policy(self, forwarding_policy, async=False, callback=None):
        """ Delete an forwarding policy
            :param forwarding_policy: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=forwarding_policy, async=async, callback=callback)

    def create_permission(self, permission, async=False, callback=None):
        """ Create an permission
            :param permission: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=permission, async=async, callback=callback)

    def delete_permission(self, permission, async=False, callback=None):
        """ Delete an permission
            :param permission: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=permission, async=async, callback=callback)
