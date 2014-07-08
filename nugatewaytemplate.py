# -*- coding:utf-8 -*-

from .nudomainbase import NUDomainBase


class NUGatewayTemplate(NUDomainBase):
    """ Defines a domain template """

    def __init__(self):
        """ Initialize a new object """

        super(NUGatewayTemplate, self).__init__()

        # Read/Write Attributes
        self.template_of_selected_gateway = None

        self.port_templates = []

        self.expose_attribute(local_name=u'template_of_selected_gateway', remote_name=u'templateOfSelectedGateway', attribute_type=str)

        # Fetchers
        # TODO: Write fetcher here
        # self.port_templates_fetcher = NUPortTemplatesFetcher.fetcher_with_entity(entity=self, local_name=u'port_templates')

    @classmethod
    def get_remote_name(cls):
        """ Provides restname """

        return u"gatewaytemplate"

    # REST methods

    def create_port_template(self, port_template, async=False, callback=None):
        """ Create an port template
            :param port_template: object to add
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.add_child_entity(entity=port_template, async=async, callback=callback)

    def delete_permission(self, port_template, async=False, callback=None):
        """ Delete a port template
            :param port_template: object to remove
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        return self.remove_child_entity(entity=port_template, async=async, callback=callback)
