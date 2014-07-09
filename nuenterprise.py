# -*- coding:utf-8 -*-

from .fetchers import NUGroupsFetcher, NUUsersFetcher, NUDomainsFetcher, NUDomainTemplatesFetcher, NUGatewaysFetcher, NUGatewayTemplatesFetcher
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

        self.expose_attribute(local_name=u'name', display_name=u'enterprise name', attribute_type=str, is_required=True, max_length=255)
        self.expose_attribute(local_name=u'description', attribute_type=str)
        self.expose_attribute(local_name=u'allow_trusted_forwarding_class', remote_name=u'allowTrustedForwardingClass', attribute_type=str)
        self.expose_attribute(local_name=u'avatar_data', remote_name=u'avatarData', attribute_type=str)
        self.expose_attribute(local_name=u'avatar_type', remote_name=u'avatarType', attribute_type=str)
        self.expose_attribute(local_name=u'associated_enterprise_profile_id', remote_name=u'enterpriseProfileID', attribute_type=str)
        self.expose_attribute(local_name=u'floating_ips_used', remote_name=u'floatingIPsUsed', attribute_type=str)

        # Read-only attributes
        self.customer_id = None

        self.expose_attribute(local_name=u'customer_id', remote_name=u'customerID', attribute_type=str, is_readonly=True)

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

        self.expose_attribute(local_name=u'floating_ips_quota', remote_name=u'floatingIPsQuota', attribute_type=str)
        self.expose_attribute(local_name=u'allow_advanced_quos_configuration', remote_name=u'allowAdvancedQOSConfiguration', attribute_type=str)
        self.expose_attribute(local_name=u'allow_gateway_management', remote_name=u'allowGatewayManagement', attribute_type=str)
        self.expose_attribute(local_name=u'allow_forwarding_class_a', remote_name=u'allowForwardingClassA', attribute_type=str)
        self.expose_attribute(local_name=u'allow_forwarding_class_b', remote_name=u'allowForwardingClassB', attribute_type=str)
        self.expose_attribute(local_name=u'allow_forwarding_class_c', remote_name=u'allowForwardingClassC', attribute_type=str)
        self.expose_attribute(local_name=u'allow_forwarding_class_d', remote_name=u'allowForwardingClassD', attribute_type=str)
        self.expose_attribute(local_name=u'allow_forwarding_class_e', remote_name=u'allowForwardingClassE', attribute_type=str)
        self.expose_attribute(local_name=u'allow_forwarding_class_f', remote_name=u'allowForwardingClassF', attribute_type=str)
        self.expose_attribute(local_name=u'allow_forwarding_class_g', remote_name=u'allowForwardingClassG', attribute_type=str)
        self.expose_attribute(local_name=u'allow_forwarding_class_h', remote_name=u'allowForwardingClassH', attribute_type=str)

        # Fetchers
        self._groups_fetcher = NUGroupsFetcher.fetcher_with_entity(entity=self, local_name=u'groups')
        self._users_fetcher = NUUsersFetcher.fetcher_with_entity(entity=self, local_name=u'users')
        self._domains_fetcher = NUDomainsFetcher.fetcher_with_entity(entity=self, local_name=u'domains')
        self._domain_templates_fetcher = NUDomainTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u'domain_templates')
        self._gateways_fetcher = NUGatewaysFetcher.fetcher_with_entity(entity=self, local_name=u'gateways')
        self._gateway_templates_fetcher = NUGatewayTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u'gateway_templates')

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

        return self.add_child_entity(entity=group, async=async, callback=callback)

    def delete_group(self, group, async=False, callback=None):
        """ Removes a group
            :param group: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=group, async=async, callback=callback)

    def fetch_groups(self):
        """ Fetch groups """

        self._groups_fetcher.fetch_entities()

    def create_user(self, user, async=False, callback=None):
        """ Create a user
            :param user: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=user, async=async, callback=callback)

    def delete_user(self, user, async=False, callback=None):
        """ Removes a user
            :param user: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=user, async=async, callback=callback)

    def fetch_users(self, filter=None, page=None, order_by=None):
        """ Fetch users """

        if order_by:
            self._users_fetcher.order_by = order_by

        return self._users_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_domain_template(self, domain_template, async=False, callback=None):
        """ Create a domain template
            :param domain: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=domain_template, async=async, callback=callback)

    def delete_domain_template(self, domain_template, async=False, callback=None):
        """ Removes a domain template
            :param user: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=domain_template, async=async, callback=callback)

    def instanciate_domain(self, domain, domain_template, async=False, callback=None):
        """ Instanciate a domain
            :param domain: object to instanciate
            :param domain_template: template to intanciate from
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        domain.template_id = domain_template.id
        return self.add_child_entity(entity=domain, async=async, callback=callback)

    def create_gateway_template(self, gateway_template, async=False, callback=None):
        """ Create a gateway template
            :param gateway: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=gateway_template, async=async, callback=callback)

    def delete_gateway_template(self, gateway_template, async=False, callback=None):
        """ Removes a gateway template
            :param user: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=gateway_template, async=async, callback=callback)

    def instanciate_gateway(self, gateway, gateway_template, async=False, callback=None):
        """ Instanciate a gateway
            :param gateway: object to instanciate
            :param gateway_template: template to intanciate from
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        gateway.template_id = gateway_template.id
        return self.add_child_entity(entity=gateway, async=async, callback=callback)
