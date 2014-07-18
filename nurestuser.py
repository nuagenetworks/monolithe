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
