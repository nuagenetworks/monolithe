# -*- coding:utf-8 -*-

from .fetchers import NUEnterprisesFetcher
from restnuage import NURESTBasicUser


class NURESTUser(NURESTBasicUser):
    """ Defines a user """

    def __init__(self):
        """ Initialize a new object """

        super(NURESTUser, self).__init__()

        # Read/Write Attributes
        self.email = None
        self.firstname = None
        self.lastname = None
        self.enterprise_id = None
        self.enterprise_name = None
        self.avatar_data = None
        self.avatar_type = None
        self.role = None

        self.autodiscovered_gateways = []
        self.enterprise_profiles = []
        self.enterprises = []
        self.gateways = []
        self.gateway_templates = []
        self.licenses = []
        self.mirror_destinations = []
        self.redundant_gateway_groups = []
        self.shared_network_resources = []
        self.system_configs = []
        self.vsps = []

        self.expose_attribute(local_name='email', attribute_type=str)
        self.expose_attribute(local_name='firstname', remote_name='firstName', attribute_type=str)
        self.expose_attribute(local_name='lastname', remote_name='lastName', attribute_type=str)
        self.expose_attribute(local_name='enterprise_id', remote_name='enterpriseID', attribute_type=str)
        self.expose_attribute(local_name='enterprise_name', remote_name='enterpriseName', attribute_type=str)
        self.expose_attribute(local_name='role', attribute_type=str)
        self.expose_attribute(local_name='avatar_type', remote_name='avatarType', attribute_type=str)
        self.expose_attribute(local_name='avatar_data', remote_name='avatarData', attribute_type=str)

        # Fetchers
        self._enterprises_fetcher = NUEnterprisesFetcher.fetcher_with_entity(entity=self, local_name=u'enterprises')

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return "me"

    @classmethod
    def is_resource_name_fixed(cls):
        """ Fixed resource name """

        return True

    # REST methods

    def create_enterprise(self, enterprise, async=False, callback=None):
        """ Create an enterprise
            :param enterprise: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=enterprise, async=async, callback=callback)

    def delete_enterprise(self, enterprise, async=False, callback=None, response_choice=1):
        """ Removes an enteprise
            :param enterprise: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
            :param response_choice: additionnal information to set user choice when removing
        """

        return self.remove_child_entity(entity=enterprise, response_choice=response_choice)

    def fetch_enterprises(self):
        """ Fetch enterprises """

        return self._enterprises_fetcher.fetch_entities()
