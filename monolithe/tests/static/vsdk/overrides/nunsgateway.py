# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.
# NUNSGateway
# Represents Network Service Gateway object.

from .autogenerates import NUNSGateway as AutoGenerate


class NUNSGateway(AutoGenerate):
    """ Represents a NUNSGateway object in the VSD

        See:
            vsdk.autogenerates.NUNSGateway
    """

    def __init__(self, **kwargs):
        """ Initializes a NUNSGateway instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsgateway = NUNSGateway(id=u'xxxx-xxx-xxx-xxx', name=u'NSGateway')
                >>> nsgateway = NUNSGateway(data=my_dict)
        """

        super(NUNSGateway, self).__init__(**kwargs)

    def is_template(self):
        """ Verify that the object is a template

            Returns:
                (bool): True if the object is a template
        """
        return False

    def is_from_template(self):
        """ Verify if the object has been instantiated from a template

            Note:
                The object has to be fetched. Otherwise, it does not
                have information from its parent

            Returns:
                (bool): True if the object is a template
        """
        return self.template_id
