# -*- coding: utf-8 -*-
"""

NURESTUser

Author Christophe Serafin <christophe.serafin@alcatel-lucent.com>

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 3.0 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

"""
from .fetchers import NUEnterprisesFetcher
from .fetchers import NUSystemConfigsFetcher
from bambou import NURESTBasicUser


class NURESTUser(NURESTBasicUser):
    """ Defines a user """

    def __init__(self, **kwargs):
        """ Initialize a new object """

        super(NURESTUser, self).__init__()

        # Read/Write Attributes
        self.email = None
        self.first_name = None
        self.last_name = None
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
        self.expose_attribute(local_name='first_name', remote_name='firstName', attribute_type=str)
        self.expose_attribute(local_name='last_name', remote_name='lastName', attribute_type=str)
        self.expose_attribute(local_name='enterprise_id', remote_name='enterpriseID', attribute_type=str)
        self.expose_attribute(local_name='enterprise_name', remote_name='enterpriseName', attribute_type=str)
        self.expose_attribute(local_name='role', attribute_type=str)
        self.expose_attribute(local_name='avatar_type', remote_name='avatarType', attribute_type=str)
        self.expose_attribute(local_name='avatar_data', remote_name='avatarData', attribute_type=str)

        # Fetchers
        self.enterprises_fetcher = NUEnterprisesFetcher.fetcher_with_object(nurest_object=self, local_name=u'enterprises')
        self.system_configs_fetcher = NUSystemConfigsFetcher.fetcher_with_object(nurest_object=self, local_name=u'system_configs')

        for key, value in kwargs.iteritems():
            if hasattr(self, key):
                setattr(self, key, value)

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return "me"

    @classmethod
    def is_resource_name_fixed(cls):
        """ Fixed resource name """

        return True

    def get_resource_url(self):
        """ Get resource complete url

            Returns:
                Retrns a complete url containing /me
        """

        name = self.__class__.get_resource_name()
        url = self.__class__.base_url()
        return "%s/%s" % (url, name)

    def get_resource_url_for_child_type(self, object_type):
        """ Get the resource url for the object type """

        return "%s/%s" % (self.__class__.base_url(), object_type.get_resource_name())

    def to_NUUser(self):
        """ Convert to NUUser

            Returns:
                Returns a NUUser instance
        """

        from . import NUUser
        user = NUUser()

        for attribute in self.get_attributes():

            if hasattr(user, attribute.local_name):
                value = getattr(self, attribute.local_name)
                setattr(user, attribute.local_name, value)

        return user
