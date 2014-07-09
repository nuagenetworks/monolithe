# -*- coding:utf-8 -*-

from .nudomainbase import NUDomainBase


class NUDomainTemplate(NUDomainBase):
    """ Defines a domain template """

    def __init__(self):
        """ Initialize a new object """

        super(NUDomainTemplate, self).__init__()

        # Read/Write Attributes

        self.policy_group_templates = []
        self.redirection_target_templates = []
        self.subnet_templates = []
        self.vport_templates = []
        self.zone_templates = []

        # Fetchers
        # TODO : Write fetchers here

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"domaintemplate"

    # REST methods

    def create_zone_template(self, zone_template, async=False, callback=None):
        """ Create a zone template
            :param zone_template: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=zone_template, async=async, callback=callback)

    def delete_zone_template(self, zone_template, async=False, callback=None):
        """ Removes a zone template
            :param zone_template: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=zone_template, async=async, callback=callback)
