# -*- coding: utf-8 -*-

from ..fetchers import NUIngressAdvancedForwardingTemplateEntriesFetcher

from bambou import NURESTObject


class NUIngressAdvancedForwardingTemplate(NURESTObject):
    """ Represents a IngressAdvancedForwardingTemplate object """

    def __init__(self):
        """ Initializing object """

        super(NUIngressAdvancedForwardingTemplate, self).__init__()

        # Read/Write Attributes

        self.description = None
        self.name = None
        self.active = None

        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"active", remote_name=u"active", attribute_type=bool)

        # Fetchers

        self.ingressadvfwdentrytemplates = []
        self._ingressadvfwdentrytemplates_fetcher = NUIngressAdvancedForwardingTemplateEntriesFetcher.fetcher_with_entity(entity=self, local_name=u"ingressadvfwdentrytemplates")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"ingressadvfwdtemplate"

    # REST methods

    def create_ingressadvfwdentrytemplate(self, ingressadvfwdentrytemplate, async=False, callback=None):
        """ Create a ingressadvfwdentrytemplate
            :param ingressadvfwdentrytemplate: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=ingressadvfwdentrytemplate, async=async, callback=callback)

    def delete_ingressadvfwdentrytemplate(self, ingressadvfwdentrytemplate, async=False, callback=None):
        """ Removes a ingressadvfwdentrytemplate
            :param ingressadvfwdentrytemplate: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=ingressadvfwdentrytemplate, async=async, callback=callback)

    def fetch_ingressadvfwdentrytemplates(self, filter=None, page=None, order_by=None):
        """ Fetch IngressAdvancedForwardingTemplateEntries """

        if order_by:
            self._ingressadvfwdentrytemplates_fetcher.order_by = order_by

        return self._ingressadvfwdentrytemplates_fetcher.fetch_matching_entities(filter=filter, page=page)
