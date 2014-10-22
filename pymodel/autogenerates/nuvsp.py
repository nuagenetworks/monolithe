# -*- coding: utf-8 -*-

from ..fetchers import NUHSCsFetcher
from ..fetchers import NUVSCsFetcher
from ..fetchers import NUVSDsFetcher

from bambou import NURESTObject


class NUVSP(NURESTObject):
    """ Represents a VSP object """

    def __init__(self):
        """ Initializing object """

        super(NUVSP, self).__init__()

        # Read/Write Attributes

        self.description = None
        self.location = None
        self.name = None
        self.product_version = None

        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"location", remote_name=u"location", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=str)

        # Fetchers

        self.hscs = []
        self._hscs_fetcher = NUHSCsFetcher.fetcher_with_entity(entity=self, local_name=u"hscs")

        self.vscs = []
        self._vscs_fetcher = NUVSCsFetcher.fetcher_with_entity(entity=self, local_name=u"vscs")

        self.vsds = []
        self._vsds_fetcher = NUVSDsFetcher.fetcher_with_entity(entity=self, local_name=u"vsds")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"vsp"

    # REST methods

    def create_hsc(self, hsc, async=False, callback=None):
        """ Create a hsc
            :param hsc: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=hsc, async=async, callback=callback)

    def delete_hsc(self, hsc, async=False, callback=None):
        """ Removes a hsc
            :param hsc: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=hsc, async=async, callback=callback)

    def fetch_hscs(self, filter=None, page=None, order_by=None):
        """ Fetch HSCs """

        if order_by:
            self._hscs_fetcher.order_by = order_by

        return self._hscs_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_vsc(self, vsc, async=False, callback=None):
        """ Create a vsc
            :param vsc: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vsc, async=async, callback=callback)

    def delete_vsc(self, vsc, async=False, callback=None):
        """ Removes a vsc
            :param vsc: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vsc, async=async, callback=callback)

    def fetch_vscs(self, filter=None, page=None, order_by=None):
        """ Fetch VSCs """

        if order_by:
            self._vscs_fetcher.order_by = order_by

        return self._vscs_fetcher.fetch_matching_entities(filter=filter, page=page)

    def create_vsd(self, vsd, async=False, callback=None):
        """ Create a vsd
            :param vsd: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vsd, async=async, callback=callback)

    def delete_vsd(self, vsd, async=False, callback=None):
        """ Removes a vsd
            :param vsd: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vsd, async=async, callback=callback)

    def fetch_vsds(self, filter=None, page=None, order_by=None):
        """ Fetch VSDs """

        if order_by:
            self._vsds_fetcher.order_by = order_by

        return self._vsds_fetcher.fetch_matching_entities(filter=filter, page=page)
