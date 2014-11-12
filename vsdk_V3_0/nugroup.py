# -*- coding: utf-8 -*-
"""

NUGroup

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

from .autogenerates import NUGroup as AutoGenerate
from constants import UserRole


class NUGroup(AutoGenerate):
    """ Represents a Group object in the VSD
        This object should contain all specific methods
    """

    def __init__(self, **kwargs):
        """ Initializing object """

        super(NUGroup, self).__init__(**kwargs)
        self.can_delete_children = True

        self.expose_attribute(local_name=u"description", remote_name=u"description", attribute_type=str, can_order=True, can_search=True)
        self.expose_attribute(local_name=u"name", remote_name=u"name", attribute_type=str, is_required=True, min_length=1, max_length=255, is_unique=True, can_order=True, can_search=True)
        self.expose_attribute(local_name=u"private", remote_name=u"private", attribute_type=bool, can_order=True, can_search=True)
        self.expose_attribute(local_name=u"role", remote_name=u"role", attribute_type=str, choices=[UserRole.CSPROOT, UserRole.CSPOPERATOR, UserRole.ORGADMIN, UserRole.ORGNETWORKDESIGNER, UserRole.ORGUSER, UserRole.USER])

    def create_user(self, user, async=False, callback=None):
        """ Use assign_users method instead

            Raise:
                NotImplementedError
        """

        raise NotImplementedError("This method should not be used. Use assign_users method instead.")

    def delete_user(self, user, async=False, callback=None):
        """ Use assign_users method instead

            Raise:
                NotImplementedError
        """

        raise NotImplementedError("This method should not be used. Use assign_users method instead.")

    def assign_users(self, users, async=False, callback=None):
        """ Assign users to this group

            Args:
                users: (list) list of users to assign to the current group
                async: (bool) Make a sync or async HTTP request
                callback: (method) Callback method called when async is set to True

            Returns:
                Returns the current object and the connection (object, connection)
        """

        return self.assign_objects(objects=users, async=async, callback=callback)
