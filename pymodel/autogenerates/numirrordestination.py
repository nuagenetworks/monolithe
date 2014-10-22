# -*- coding: utf-8 -*-

from ..fetchers import NUVPortMirrorsFetcher

from bambou import NURESTObject


class NUMirrorDestination(NURESTObject):
    """ Represents a MirrorDestination object """

    def __init__(self):
        """ Initializing object """

        super(NUMirrorDestination, self).__init__()

        # Read/Write Attributes

        self.destination_ip = None
        self.name = None
        self.service_id = None

        self.expose_attribute(local_name=u"destination_ip", remote_name=u"destinationIp", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"service_id", remote_name=u"serviceId", attribute_type=str)

        # Fetchers

        self.vportmirrors = []
        self._vportmirrors_fetcher = NUVPortMirrorsFetcher.fetcher_with_entity(entity=self, local_name=u"vportmirrors")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"mirrordestination"

    # REST methods

    def create_vportmirror(self, vportmirror, async=False, callback=None):
        """ Create a vportmirror
            :param vportmirror: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=vportmirror, async=async, callback=callback)

    def delete_vportmirror(self, vportmirror, async=False, callback=None):
        """ Removes a vportmirror
            :param vportmirror: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=vportmirror, async=async, callback=callback)

    def fetch_vportmirrors(self, filter=None, page=None, order_by=None):
        """ Fetch VPortMirrors """

        if order_by:
            self._vportmirrors_fetcher.order_by = order_by

        return self._vportmirrors_fetcher.fetch_matching_entities(filter=filter, page=page)
