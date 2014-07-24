# -*- coding: utf-8 -*-
from .autogenerates import NURESTUser as AutoGenerate


class NURESTUser(AutoGenerate):
    """ Represents a User object """

    def to_NUUser(self):
        """ Convert to NUUser """

        from . import NUUser
        user = NUUser()

        for attribute in self.get_attributes():

            if hasattr(user, attribute.local_name):
                value = getattr(self, attribute.local_name)
                setattr(user, attribute.local_name, value)

        return user

    def delete_enterprise(self, enterprise, async=False, callback=None, response_choice=1):
        """ Removes an enteprise
            :param enterprise: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
            :param response_choice: additionnal information to set user choice when removing
        """

        return self.remove_child_entity(entity=enterprise, response_choice=response_choice)
