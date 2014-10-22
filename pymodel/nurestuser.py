# -*- coding: utf-8 -*-
from .autogenerates import NURESTUser as AutoGenerate


class NURESTUser(AutoGenerate):
    """ Represents a User object """

    def get_resource_url(self):
        """ Get resource complete url """

        name = self.__class__.get_resource_name()
        url = self.__class__.base_url()
        return "%s/%s" % (url, name)

    def get_resource_url_for_child_type(self, entity_type):
        """ Get the resource url for the entity type """

        return "%s/%s" % (self.__class__.base_url(), entity_type.get_resource_name())

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
