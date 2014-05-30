# -*- coding:utf-8 -*-

from restnuage.nurest_object import NURESTObject


class Enterprise(NURESTObject):
    """ Creates a enterprise object for tests """

    def __init__(self, id=None, name='Alcatel-Lucent'):
        """ Creates a new enterprise """
        super(Enterprise, self).__init__(id=id)
        self.name = name
        self.invisible = True

        self.expose_attribute(local_name='name')

    @classmethod
    def get_remote_name(cls):
        """ Provides enterprise classname  """

        return u"enterprise"
