# -*- coding: utf-8 -*-

from ..fetchers import NUAlarmsFetcher

from bambou import NURESTObject


class NUTCA(NURESTObject):
    """ Represents a TCA object """

    def __init__(self):
        """ Initializing object """

        super(NUTCA, self).__init__()

        # Read/Write Attributes

        self.description = None
        self.metric = None
        self.name = None
        self.period = None
        self.scope = None
        self.threshold = None
        self.type = None
        self.url_end_point = None

        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str)
        self.expose_attribute(local_name=u"metric", remote_name=u"metric", attribute_type=str)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str)
        self.expose_attribute(local_name=u"period", remote_name=u"period", attribute_type=str)
        self.expose_attribute(local_name=u"scope", remote_name=u"scope", attribute_type=str)
        self.expose_attribute(local_name=u"threshold", remote_name=u"threshold", attribute_type=str)
        self.expose_attribute(local_name=u"type", remote_name=u"type", attribute_type=str)
        self.expose_attribute(local_name=u"url_end_point", remote_name=u"URLEndPoint", attribute_type=str)

        # Fetchers

        self.alarms = []
        self._alarms_fetcher = NUAlarmsFetcher.fetcher_with_entity(entity=self, local_name=u"alarms")


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"tca"

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
