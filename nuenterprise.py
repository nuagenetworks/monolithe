# -*- coding:utf-8 -*-

from .fetchers import NUGroupsFetcher
from restnuage import NURESTObject


class NUEnterprise(NURESTObject):
    """ Defines an enterprise """

    def __init__(self):
        """ Initialize a new object """

        super(NUEnterprise, self).__init__()

        # Read/Write Attributes
        self.name = None
        self.description = None
        self.allow_trusted_forwarding_class = bool()
        self.avatar_data = None
        self.avatar_type = None
        self.associated_enterprise_profile_id = None
        self.floating_ips_used = None

        self.alarms = []
        self.applications = []
        self.autodiscovered_gateways = []
        self.domains = []
        self.domain_templates = []
        self.dscp_forwarding_class_tables = []
        self.events = []
        self.gateways = []
        self.gateway_templates = []
        self.groups = []
        self.l2_domains = []
        self.l2_domain_templates = []
        self.ldap_configurations = []
        self.network_macros = []
        self.redundant_gateway_groups = []
        self.summaries = []
        self.users = []
        self.virtual_machines = []

        self.expose_attribute(local_name=u'name')
        self.expose_attribute(local_name=u'description')
        self.expose_attribute(local_name=u'allow_trusted_forwarding_class', remote_name=u'allowTrustedForwardingClass')
        self.expose_attribute(local_name=u'avatar_data', remote_name=u'avatarData')
        self.expose_attribute(local_name=u'avatar_type', remote_name=u'avatarType')
        self.expose_attribute(local_name=u'associated_enterprise_profile_id', remote_name=u'enterpriseProfileID')
        self.expose_attribute(local_name=u'floating_ips_used', remote_name=u'floatingIPsUsed')

        # Read-only attributes
        self.customer_id = None

        self.expose_attribute(local_name=u'customer_id', remote_name=u'customerID')

        # Read-only Attributes
        self.floating_ips_quota = None
        self.allow_advanced_quos_configuration = bool()
        self.allow_gateway_management = bool()
        self.allow_forwarding_class_a = bool()
        self.allow_forwarding_class_b = bool()
        self.allow_forwarding_class_c = bool()
        self.allow_forwarding_class_d = bool()
        self.allow_forwarding_class_e = bool()
        self.allow_forwarding_class_f = bool()
        self.allow_forwarding_class_g = bool()
        self.allow_forwarding_class_h = bool()

        self.expose_attribute(local_name=u'floating_ips_quota', remote_name=u'floatingIPsQuota')
        self.expose_attribute(local_name=u'allow_advanced_quos_configuration', remote_name=u'allowAdvancedQOSConfiguration')
        self.expose_attribute(local_name=u'allow_gateway_management', remote_name=u'allowGatewayManagement')
        self.expose_attribute(local_name=u'allow_forwarding_class_a', remote_name=u'allowForwardingClassA')
        self.expose_attribute(local_name=u'allow_forwarding_class_b', remote_name=u'allowForwardingClassB')
        self.expose_attribute(local_name=u'allow_forwarding_class_c', remote_name=u'allowForwardingClassC')
        self.expose_attribute(local_name=u'allow_forwarding_class_d', remote_name=u'allowForwardingClassD')
        self.expose_attribute(local_name=u'allow_forwarding_class_e', remote_name=u'allowForwardingClassE')
        self.expose_attribute(local_name=u'allow_forwarding_class_f', remote_name=u'allowForwardingClassF')
        self.expose_attribute(local_name=u'allow_forwarding_class_g', remote_name=u'allowForwardingClassG')
        self.expose_attribute(local_name=u'allow_forwarding_class_h', remote_name=u'allowForwardingClassH')

        # Fetchers
        self._groups_fetcher = NUGroupsFetcher.fetcher_with_entity(entity=self, local_name=u'groups')


    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"enterprise"

    # REST methods

    def create_group(self, group, async=False, callback=None):
        """ Create a group
            :param group: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        (group, connection) = self.add_child_entity(entity=group, async=async, callback=callback)

    def remove_group(self, group, async=False, callback=None, response_choice=1):
        """ Removes a group
            :param enterprise: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
            :param response_choice: additionnal information to set user choice when removing
        """

        self.remove_child_entity(entity=group, response_choice=response_choice)

    def fetch_groups(self):
        """ Fetch groups """

        self._groups_fetcher.fetch_entities()

    # def create_user(self, user, async=False, callback=None):
    #     """ Create a user
    #         :param user: object to add
    #         :param async: Make an sync or async HTTP request
    #         :param callback: Callback method called when async is set to true
    #     """
    #
    #     (user, connection) = self.add_child_entity(entity=user, async=async, callback=callback)
    #
    # def remove_user(self, user, async=False, callback=None, response_choice=1):
    #     """ Removes a user
    #         :param user: object to remove
    #         :param async: Make an sync or async HTTP request
    #         :param callback: Callback method called when async is set to true
    #         :param response_choice: additionnal information to set user choice when removing
    #     """
    #
    #     self.remove_child_entity(entity=user, response_choice=response_choice)
    #
    # def fetch_users(self):
    #     """ Fetch users """
    #
    #     self._users_fetcher.fetch_entities()
