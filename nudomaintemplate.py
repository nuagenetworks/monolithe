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
