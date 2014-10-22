# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUAlarmsFetcher
from ..fetchers import NUAppsFetcher
from ..fetchers import NUServicesFetcher
from ..fetchers import NUGatewaysFetcher
from ..fetchers import NUGatewayTemplatesFetcher
from ..fetchers import NURedundantGWGrpsFetcher
from ..fetchers import NUInfrastructureGatewayProfilesFetcher
from ..fetchers import NUInfrastructurePortProfilesFetcher
from ..fetchers import NUInfrastructureVlanProfilesFetcher
from ..fetchers import NUJobsFetcher
from ..fetchers import NUDomainsFetcher
from ..fetchers import NUDomainTemplatesFetcher
from ..fetchers import NUEnterpriseNetworkMacrosFetcher
from ..fetchers import NUL2DomainsFetcher
from ..fetchers import NUL2DomainTemplatesFetcher
from ..fetchers import NUMultiCastChannelMapsFetcher
from ..fetchers import NUPublicNetworkMacrosFetcher
from ..fetchers import NUDSCPForwardingClassTablesFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NULDAPConfigurationsFetcher
from ..fetchers import NUUsersFetcher
from ..fetchers import NUVirtualMachinesFetcher

from bambou import NURESTObject


class NUEnterprise(NURESTObject):
    """ Represents a Enterprise object """

    def __init__(self):
        """ Initializing object """

        super(NUEnterprise, self).__init__()

        # Read/Write Attributes

        self.allow_advanced_qos_configuration = None
        self.allowed_forwarding_classes = None
        self.allow_gateway_management = None
        self.allow_trusted_forwarding_class = None
        self.avatar_data = None
        self.avatar_type = None
        self.customer_id = None
        self.description = None
        self.dhcp_lease_interval = None
        self.dhcp_mapping_retention_timer = None
        self.enterprise_profile_id = None
        self.floating_ips_quota = None
        self.floating_ips_used = None
        self.name = None

        self.expose_attribute(local_name=u"allow_advanced_qos_configuration", remote_name=u"allowAdvancedQOSConfiguration", attribute_type=bool)
        self.expose_attribute(local_name=u"allowed_forwarding_classes", remote_name=u"allowedForwardingClasses", attribute_type=str)
        self.expose_attribute(local_name=u"allow_gateway_management", remote_name=u"allowGatewayManagement", attribute_type=bool)
        self.expose_attribute(local_name=u"allow_trusted_forwarding_class", remote_name=u"allowTrustedForwardingClass", attribute_type=bool)
        self.expose_attribute(local_name=u"avatar_data", remote_name=u"avatarData", attribute_type=str)
        self.expose_attribute(local_name=u"avatar_type", remote_name=u"avatarType", attribute_type=str)
        self.expose_attribute(local_name=u"customer_id", remote_name=u"customerID", attribute_type=str)
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"dhcp_lease_interval", remote_name=u"DHCPLeaseInterval", attribute_type=int)
        self.expose_attribute(local_name=u"dhcp_mapping_retention_timer", remote_name=u"DHCPMappingRetentionTimer", attribute_type=int)
        self.expose_attribute(local_name=u"enterprise_profile_id", remote_name=u"enterpriseProfileID", attribute_type=str)
        self.expose_attribute(local_name=u"floating_ips_quota", remote_name=u"floatingIPsQuota", attribute_type=int)
        self.expose_attribute(local_name=u"floating_ips_used", remote_name=u"floatingIPsUsed", attribute_type=int)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers

        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")

        self.allalarms = []
        self._allalarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"allalarms")

        self.applications = []
        self._applications_fetcher = NUAppsFetcher.fetcher_with_entity(entity=self, local_name=u"applications")

        self.applicationservices = []
        self._applicationservices_fetcher = NUServicesFetcher.fetcher_with_entity(entity=self, local_name=u"applicationservices")

        self.gateways = []
        self._gateways_fetcher = NUGatewaysFetcher.fetcher_with_entity(entity=self, local_name=u"gateways")

        self.gatewaytemplates = []
        self._gatewaytemplates_fetcher = NUGatewayTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"gatewaytemplates")

        self.redundancygroups = []
        self._redundancygroups_fetcher = NURedundantGWGrpsFetcher.fetcher_with_entity(entity=self, local_name=u"redundancygroups")

        self.infrastructuregatewayprofiles = []
        self._infrastructuregatewayprofiles_fetcher = NUInfrastructureGatewayProfilesFetcher.fetcher_with_entity(entity=self, local_name=u"infrastructuregatewayprofiles")

        self.infrastructureportprofiles = []
        self._infrastructureportprofiles_fetcher = NUInfrastructurePortProfilesFetcher.fetcher_with_entity(entity=self, local_name=u"infrastructureportprofiles")

        self.infrastructurevlanprofiles = []
        self._infrastructurevlanprofiles_fetcher = NUInfrastructureVlanProfilesFetcher.fetcher_with_entity(entity=self, local_name=u"infrastructurevlanprofiles")

        self.jobs = []
        self._jobs_fetcher = NUJobsFetcher.fetcher_with_entity(entity=self, local_name=u"jobs")

        self.domains = []
        self._domains_fetcher = NUDomainsFetcher.fetcher_with_entity(entity=self, local_name=u"domains")

        self.domaintemplates = []
        self._domaintemplates_fetcher = NUDomainTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"domaintemplates")

        self.enterprisenetworks = []
        self._enterprisenetworks_fetcher = NUEnterpriseNetworkMacrosFetcher.fetcher_with_entity(entity=self, local_name=u"enterprisenetworks")

        self.l2domains = []
        self._l2domains_fetcher = NUL2DomainsFetcher.fetcher_with_entity(entity=self, local_name=u"l2domains")

        self.l2domaintemplates = []
        self._l2domaintemplates_fetcher = NUL2DomainTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"l2domaintemplates")

        self.multicastchannelmaps = []
        self._multicastchannelmaps_fetcher = NUMultiCastChannelMapsFetcher.fetcher_with_entity(entity=self, local_name=u"multicastchannelmaps")

        self.publicnetworks = []
        self._publicnetworks_fetcher = NUPublicNetworkMacrosFetcher.fetcher_with_entity(entity=self, local_name=u"publicnetworks")

        self.dscpforwardingclasstables = []
        self._dscpforwardingclasstables_fetcher = NUDSCPForwardingClassTablesFetcher.fetcher_with_entity(entity=self, local_name=u"dscpforwardingclasstables")

        self.groups = []
        self._groups_fetcher = NUGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"groups")

        self.ldapconfigurations = []
        self._ldapconfigurations_fetcher = NULDAPConfigurationsFetcher.fetcher_with_entity(entity=self, local_name=u"ldapconfigurations")

        self.users = []
        self._users_fetcher = NUUsersFetcher.fetcher_with_entity(entity=self, local_name=u"users")

        self.vms = []
        self._vms_fetcher = NUVirtualMachinesFetcher.fetcher_with_entity(entity=self, local_name=u"vms")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"enterprise"

    # REST methods

    def create_alarm(self, alarm, async=False, callback=None):
        """ Create a alarm
            :param alarm: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=alarm, async=async, callback=callback)

    def delete_alarm(self, alarm, async=False, callback=None):
        """ Removes a alarm
            :param alarm: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=alarm, async=async, callback=callback)

    def fetch_alarms(self, filter=None, page=None, order_by=None):
        """ Fetch Alarms """

        if order_by:
            self._alarms_fetcher.order_by = order_by

        return self._alarms_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_allalarm(self, allalarm, async=False, callback=None):
        """ Create a allalarm
            :param allalarm: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=allalarm, async=async, callback=callback)

    def delete_allalarm(self, allalarm, async=False, callback=None):
        """ Removes a allalarm
            :param allalarm: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=allalarm, async=async, callback=callback)

    def fetch_allalarms(self, filter=None, page=None, order_by=None):
        """ Fetch Alarms """

        if order_by:
            self._allalarms_fetcher.order_by = order_by

        return self._allalarms_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_application(self, application, async=False, callback=None):
        """ Create a application
            :param application: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=application, async=async, callback=callback)

    def delete_application(self, application, async=False, callback=None):
        """ Removes a application
            :param application: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=application, async=async, callback=callback)

    def fetch_applications(self, filter=None, page=None, order_by=None):
        """ Fetch Apps """

        if order_by:
            self._applications_fetcher.order_by = order_by

        return self._applications_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_applicationservice(self, applicationservice, async=False, callback=None):
        """ Create a applicationservice
            :param applicationservice: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=applicationservice, async=async, callback=callback)

    def delete_applicationservice(self, applicationservice, async=False, callback=None):
        """ Removes a applicationservice
            :param applicationservice: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=applicationservice, async=async, callback=callback)

    def fetch_applicationservices(self, filter=None, page=None, order_by=None):
        """ Fetch Services """

        if order_by:
            self._applicationservices_fetcher.order_by = order_by

        return self._applicationservices_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_gateway(self, gateway, async=False, callback=None):
        """ Create a gateway
            :param gateway: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=gateway, async=async, callback=callback)

    def delete_gateway(self, gateway, async=False, callback=None):
        """ Removes a gateway
            :param gateway: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=gateway, async=async, callback=callback)

    def fetch_gateways(self, filter=None, page=None, order_by=None):
        """ Fetch Gateways """

        if order_by:
            self._gateways_fetcher.order_by = order_by

        return self._gateways_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_gatewaytemplate(self, gatewaytemplate, async=False, callback=None):
        """ Create a gatewaytemplate
            :param gatewaytemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=gatewaytemplate, async=async, callback=callback)

    def delete_gatewaytemplate(self, gatewaytemplate, async=False, callback=None):
        """ Removes a gatewaytemplate
            :param gatewaytemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=gatewaytemplate, async=async, callback=callback)

    def fetch_gatewaytemplates(self, filter=None, page=None, order_by=None):
        """ Fetch GatewayTemplates """

        if order_by:
            self._gatewaytemplates_fetcher.order_by = order_by

        return self._gatewaytemplates_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_redundancygroup(self, redundancygroup, async=False, callback=None):
        """ Create a redundancygroup
            :param redundancygroup: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=redundancygroup, async=async, callback=callback)

    def delete_redundancygroup(self, redundancygroup, async=False, callback=None):
        """ Removes a redundancygroup
            :param redundancygroup: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=redundancygroup, async=async, callback=callback)

    def fetch_redundancygroups(self, filter=None, page=None, order_by=None):
        """ Fetch RedundantGWGrps """

        if order_by:
            self._redundancygroups_fetcher.order_by = order_by

        return self._redundancygroups_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_infrastructuregatewayprofile(self, infrastructuregatewayprofile, async=False, callback=None):
        """ Create a infrastructuregatewayprofile
            :param infrastructuregatewayprofile: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=infrastructuregatewayprofile, async=async, callback=callback)

    def delete_infrastructuregatewayprofile(self, infrastructuregatewayprofile, async=False, callback=None):
        """ Removes a infrastructuregatewayprofile
            :param infrastructuregatewayprofile: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=infrastructuregatewayprofile, async=async, callback=callback)

    def fetch_infrastructuregatewayprofiles(self, filter=None, page=None, order_by=None):
        """ Fetch InfrastructureGatewayProfiles """

        if order_by:
            self._infrastructuregatewayprofiles_fetcher.order_by = order_by

        return self._infrastructuregatewayprofiles_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_infrastructureportprofile(self, infrastructureportprofile, async=False, callback=None):
        """ Create a infrastructureportprofile
            :param infrastructureportprofile: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=infrastructureportprofile, async=async, callback=callback)

    def delete_infrastructureportprofile(self, infrastructureportprofile, async=False, callback=None):
        """ Removes a infrastructureportprofile
            :param infrastructureportprofile: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=infrastructureportprofile, async=async, callback=callback)

    def fetch_infrastructureportprofiles(self, filter=None, page=None, order_by=None):
        """ Fetch InfrastructurePortProfiles """

        if order_by:
            self._infrastructureportprofiles_fetcher.order_by = order_by

        return self._infrastructureportprofiles_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_infrastructurevlanprofile(self, infrastructurevlanprofile, async=False, callback=None):
        """ Create a infrastructurevlanprofile
            :param infrastructurevlanprofile: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=infrastructurevlanprofile, async=async, callback=callback)

    def delete_infrastructurevlanprofile(self, infrastructurevlanprofile, async=False, callback=None):
        """ Removes a infrastructurevlanprofile
            :param infrastructurevlanprofile: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=infrastructurevlanprofile, async=async, callback=callback)

    def fetch_infrastructurevlanprofiles(self, filter=None, page=None, order_by=None):
        """ Fetch InfrastructureVlanProfiles """

        if order_by:
            self._infrastructurevlanprofiles_fetcher.order_by = order_by

        return self._infrastructurevlanprofiles_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_job(self, job, async=False, callback=None):
        """ Create a job
            :param job: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=job, async=async, callback=callback)

    def delete_job(self, job, async=False, callback=None):
        """ Removes a job
            :param job: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=job, async=async, callback=callback)

    def fetch_jobs(self, filter=None, page=None, order_by=None):
        """ Fetch Jobs """

        if order_by:
            self._jobs_fetcher.order_by = order_by

        return self._jobs_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_domain(self, domain, async=False, callback=None):
        """ Create a domain
            :param domain: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=domain, async=async, callback=callback)

    def delete_domain(self, domain, async=False, callback=None):
        """ Removes a domain
            :param domain: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=domain, async=async, callback=callback)

    def fetch_domains(self, filter=None, page=None, order_by=None):
        """ Fetch Domains """

        if order_by:
            self._domains_fetcher.order_by = order_by

        return self._domains_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_domaintemplate(self, domaintemplate, async=False, callback=None):
        """ Create a domaintemplate
            :param domaintemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=domaintemplate, async=async, callback=callback)

    def delete_domaintemplate(self, domaintemplate, async=False, callback=None):
        """ Removes a domaintemplate
            :param domaintemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=domaintemplate, async=async, callback=callback)

    def fetch_domaintemplates(self, filter=None, page=None, order_by=None):
        """ Fetch DomainTemplates """

        if order_by:
            self._domaintemplates_fetcher.order_by = order_by

        return self._domaintemplates_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_enterprisenetwork(self, enterprisenetwork, async=False, callback=None):
        """ Create a enterprisenetwork
            :param enterprisenetwork: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=enterprisenetwork, async=async, callback=callback)

    def delete_enterprisenetwork(self, enterprisenetwork, async=False, callback=None):
        """ Removes a enterprisenetwork
            :param enterprisenetwork: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=enterprisenetwork, async=async, callback=callback)

    def fetch_enterprisenetworks(self, filter=None, page=None, order_by=None):
        """ Fetch EnterpriseNetworkMacros """

        if order_by:
            self._enterprisenetworks_fetcher.order_by = order_by

        return self._enterprisenetworks_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_l2domain(self, l2domain, async=False, callback=None):
        """ Create a l2domain
            :param l2domain: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=l2domain, async=async, callback=callback)

    def delete_l2domain(self, l2domain, async=False, callback=None):
        """ Removes a l2domain
            :param l2domain: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=l2domain, async=async, callback=callback)

    def fetch_l2domains(self, filter=None, page=None, order_by=None):
        """ Fetch L2Domains """

        if order_by:
            self._l2domains_fetcher.order_by = order_by

        return self._l2domains_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_l2domaintemplate(self, l2domaintemplate, async=False, callback=None):
        """ Create a l2domaintemplate
            :param l2domaintemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=l2domaintemplate, async=async, callback=callback)

    def delete_l2domaintemplate(self, l2domaintemplate, async=False, callback=None):
        """ Removes a l2domaintemplate
            :param l2domaintemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=l2domaintemplate, async=async, callback=callback)

    def fetch_l2domaintemplates(self, filter=None, page=None, order_by=None):
        """ Fetch L2DomainTemplates """

        if order_by:
            self._l2domaintemplates_fetcher.order_by = order_by

        return self._l2domaintemplates_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_multicastchannelmap(self, multicastchannelmap, async=False, callback=None):
        """ Create a multicastchannelmap
            :param multicastchannelmap: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=multicastchannelmap, async=async, callback=callback)

    def delete_multicastchannelmap(self, multicastchannelmap, async=False, callback=None):
        """ Removes a multicastchannelmap
            :param multicastchannelmap: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=multicastchannelmap, async=async, callback=callback)

    def fetch_multicastchannelmaps(self, filter=None, page=None, order_by=None):
        """ Fetch MultiCastChannelMaps """

        if order_by:
            self._multicastchannelmaps_fetcher.order_by = order_by

        return self._multicastchannelmaps_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_publicnetwork(self, publicnetwork, async=False, callback=None):
        """ Create a publicnetwork
            :param publicnetwork: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=publicnetwork, async=async, callback=callback)

    def delete_publicnetwork(self, publicnetwork, async=False, callback=None):
        """ Removes a publicnetwork
            :param publicnetwork: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=publicnetwork, async=async, callback=callback)

    def fetch_publicnetworks(self, filter=None, page=None, order_by=None):
        """ Fetch PublicNetworkMacros """

        if order_by:
            self._publicnetworks_fetcher.order_by = order_by

        return self._publicnetworks_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_dscpforwardingclasstable(self, dscpforwardingclasstable, async=False, callback=None):
        """ Create a dscpforwardingclasstable
            :param dscpforwardingclasstable: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=dscpforwardingclasstable, async=async, callback=callback)

    def delete_dscpforwardingclasstable(self, dscpforwardingclasstable, async=False, callback=None):
        """ Removes a dscpforwardingclasstable
            :param dscpforwardingclasstable: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=dscpforwardingclasstable, async=async, callback=callback)

    def fetch_dscpforwardingclasstables(self, filter=None, page=None, order_by=None):
        """ Fetch DSCPForwardingClassTables """

        if order_by:
            self._dscpforwardingclasstables_fetcher.order_by = order_by

        return self._dscpforwardingclasstables_fetcher.fetch_matching_entities(filter=filter, page=page)

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

    def fetch_groups(self, filter=None, page=None, order_by=None):
        """ Fetch Groups """

        if order_by:
            self._groups_fetcher.order_by = order_by

        return self._groups_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_ldapconfiguration(self, ldapconfiguration, async=False, callback=None):
        """ Create a ldapconfiguration
            :param ldapconfiguration: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ldapconfiguration, async=async, callback=callback)

    def delete_ldapconfiguration(self, ldapconfiguration, async=False, callback=None):
        """ Removes a ldapconfiguration
            :param ldapconfiguration: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ldapconfiguration, async=async, callback=callback)

    def fetch_ldapconfigurations(self, filter=None, page=None, order_by=None):
        """ Fetch LDAPConfigurations """

        if order_by:
            self._ldapconfigurations_fetcher.order_by = order_by

        return self._ldapconfigurations_fetcher.fetch_matching_entities(filter=filter, page=page)

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
        """ Fetch Users """

        if order_by:
            self._users_fetcher.order_by = order_by

        return self._users_fetcher.fetch_matching_entities(filter=filter, page=page)

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
