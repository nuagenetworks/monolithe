# -*- coding: utf-8 -*-

from ..fetchers import NUJobsFetcher
from ..fetchers import NUDomainsFetcher
from ..fetchers import NUSubNetworkTemplatesFetcher
from ..fetchers import NUZoneTemplatesFetcher
from ..fetchers import NUEgressACLTemplatesFetcher
from ..fetchers import NUIngressACLTemplatesFetcher
from ..fetchers import NUIngressAdvancedForwardingTemplatesFetcher
from ..fetchers import NUQosPrimitivesFetcher
from ..fetchers import NUGroupsFetcher
from ..fetchers import NUPermittedActionsFetcher
from ..fetchers import NUPolicyGroupTemplatesFetcher
from ..fetchers import NURedirectionTargetTemplatesFetcher

from restnuage import NURESTObject


class NUDomainTemplate(NURESTObject):
    """ Represents a DomainTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUDomainTemplate, self).__init__()

        # Read/Write Attributes
        
        self.description = None
        self.multicast = None
        self.associated_multicast_channel_map_id = None
        self.name = None
        
        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"multicast", remote_name=u"multicast", attribute_type=str)
        self.expose_attribute(local_name=u"associated_multicast_channel_map_id", remote_name=u"associatedMulticastChannelMapID", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)

        # Fetchers
        
        self.jobs = []
        self._jobs_fetcher = NUJobsFetcher.fetcher_with_entity(entity=self, local_name=u"jobs")
        
        self.domains = []
        self._domains_fetcher = NUDomainsFetcher.fetcher_with_entity(entity=self, local_name=u"domains")
        
        self.subnettemplates = []
        self._subnettemplates_fetcher = NUSubNetworkTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"subnettemplates")
        
        self.zonetemplates = []
        self._zonetemplates_fetcher = NUZoneTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"zonetemplates")
        
        self.egressacltemplates = []
        self._egressacltemplates_fetcher = NUEgressACLTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"egressacltemplates")
        
        self.ingressacltemplates = []
        self._ingressacltemplates_fetcher = NUIngressACLTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"ingressacltemplates")
        
        self.ingressadvfwdtemplates = []
        self._ingressadvfwdtemplates_fetcher = NUIngressAdvancedForwardingTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"ingressadvfwdtemplates")
        
        self.qos = []
        self._qos_fetcher = NUQosPrimitivesFetcher.fetcher_with_entity(entity=self, local_name=u"qos")
        
        self.groups = []
        self._groups_fetcher = NUGroupsFetcher.fetcher_with_entity(entity=self, local_name=u"groups")
        
        self.permissions = []
        self._permissions_fetcher = NUPermittedActionsFetcher.fetcher_with_entity(entity=self, local_name=u"permissions")
        
        self.policygrouptemplates = []
        self._policygrouptemplates_fetcher = NUPolicyGroupTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"policygrouptemplates")
        
        self.redirectiontargettemplates = []
        self._redirectiontargettemplates_fetcher = NURedirectionTargetTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u"redirectiontargettemplates")
        

    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"domaintemplate"

    # REST methods
    
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
    
    def create_subnettemplate(self, subnettemplate, async=False, callback=None):
        """ Create a subnettemplate
            :param subnettemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=subnettemplate, async=async, callback=callback)

    def delete_subnettemplate(self, subnettemplate, async=False, callback=None):
        """ Removes a subnettemplate
            :param subnettemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=subnettemplate, async=async, callback=callback)

    def fetch_subnettemplates(self, filter=None, page=None, order_by=None):
        """ Fetch SubNetworkTemplates """

        if order_by:
            self._subnettemplates_fetcher.order_by = order_by

        return self._subnettemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_zonetemplate(self, zonetemplate, async=False, callback=None):
        """ Create a zonetemplate
            :param zonetemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=zonetemplate, async=async, callback=callback)

    def delete_zonetemplate(self, zonetemplate, async=False, callback=None):
        """ Removes a zonetemplate
            :param zonetemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=zonetemplate, async=async, callback=callback)

    def fetch_zonetemplates(self, filter=None, page=None, order_by=None):
        """ Fetch ZoneTemplates """

        if order_by:
            self._zonetemplates_fetcher.order_by = order_by

        return self._zonetemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_egressacltemplate(self, egressacltemplate, async=False, callback=None):
        """ Create a egressacltemplate
            :param egressacltemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=egressacltemplate, async=async, callback=callback)

    def delete_egressacltemplate(self, egressacltemplate, async=False, callback=None):
        """ Removes a egressacltemplate
            :param egressacltemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=egressacltemplate, async=async, callback=callback)

    def fetch_egressacltemplates(self, filter=None, page=None, order_by=None):
        """ Fetch EgressACLTemplates """

        if order_by:
            self._egressacltemplates_fetcher.order_by = order_by

        return self._egressacltemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_ingressacltemplate(self, ingressacltemplate, async=False, callback=None):
        """ Create a ingressacltemplate
            :param ingressacltemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ingressacltemplate, async=async, callback=callback)

    def delete_ingressacltemplate(self, ingressacltemplate, async=False, callback=None):
        """ Removes a ingressacltemplate
            :param ingressacltemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ingressacltemplate, async=async, callback=callback)

    def fetch_ingressacltemplates(self, filter=None, page=None, order_by=None):
        """ Fetch IngressACLTemplates """

        if order_by:
            self._ingressacltemplates_fetcher.order_by = order_by

        return self._ingressacltemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_ingressadvfwdtemplate(self, ingressadvfwdtemplate, async=False, callback=None):
        """ Create a ingressadvfwdtemplate
            :param ingressadvfwdtemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ingressadvfwdtemplate, async=async, callback=callback)

    def delete_ingressadvfwdtemplate(self, ingressadvfwdtemplate, async=False, callback=None):
        """ Removes a ingressadvfwdtemplate
            :param ingressadvfwdtemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ingressadvfwdtemplate, async=async, callback=callback)

    def fetch_ingressadvfwdtemplates(self, filter=None, page=None, order_by=None):
        """ Fetch IngressAdvancedForwardingTemplates """

        if order_by:
            self._ingressadvfwdtemplates_fetcher.order_by = order_by

        return self._ingressadvfwdtemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
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
    
    def create_permission(self, permission, async=False, callback=None):
        """ Create a permission
            :param permission: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=permission, async=async, callback=callback)

    def delete_permission(self, permission, async=False, callback=None):
        """ Removes a permission
            :param permission: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=permission, async=async, callback=callback)

    def fetch_permissions(self, filter=None, page=None, order_by=None):
        """ Fetch PermittedActions """

        if order_by:
            self._permissions_fetcher.order_by = order_by

        return self._permissions_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_policygrouptemplate(self, policygrouptemplate, async=False, callback=None):
        """ Create a policygrouptemplate
            :param policygrouptemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=policygrouptemplate, async=async, callback=callback)

    def delete_policygrouptemplate(self, policygrouptemplate, async=False, callback=None):
        """ Removes a policygrouptemplate
            :param policygrouptemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=policygrouptemplate, async=async, callback=callback)

    def fetch_policygrouptemplates(self, filter=None, page=None, order_by=None):
        """ Fetch PolicyGroupTemplates """

        if order_by:
            self._policygrouptemplates_fetcher.order_by = order_by

        return self._policygrouptemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    
    def create_redirectiontargettemplate(self, redirectiontargettemplate, async=False, callback=None):
        """ Create a redirectiontargettemplate
            :param redirectiontargettemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=redirectiontargettemplate, async=async, callback=callback)

    def delete_redirectiontargettemplate(self, redirectiontargettemplate, async=False, callback=None):
        """ Removes a redirectiontargettemplate
            :param redirectiontargettemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=redirectiontargettemplate, async=async, callback=callback)

    def fetch_redirectiontargettemplates(self, filter=None, page=None, order_by=None):
        """ Fetch RedirectionTargetTemplates """

        if order_by:
            self._redirectiontargettemplates_fetcher.order_by = order_by

        return self._redirectiontargettemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
    