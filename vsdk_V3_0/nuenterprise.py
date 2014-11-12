# -*- coding: utf-8 -*-
"""

NUEnterprise

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

from .autogenerates import NUEnterprise as AutoGenerate

class NUEnterprise(AutoGenerate):
    """ Represents a NUEnterprise in the VSD
        This object should contain all specific methods
    """

    def delete(self, callback=None, async=False, response_choice=1):
        """ Override to automatically accept deletion """

        super(AutoGenerate, self).delete(callback=callback, async=async, response_choice=response_choice)

    def instantiate_domain(self, domain, domain_template, async=False, callback=None):
        """ instantiate a domain
            :param domain: object to instantiate
            :param domain_template: template to intanciate from
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        domain.template_id = domain_template.id
        return self.add_child_object(nurest_object=domain, async=async, callback=callback)

    def instantiate_gateway(self, gateway, gateway_template, async=False, callback=None):
        """ instantiate a gateway
            :param gateway: object to instantiate
            :param gateway_template: template to intanciate from
            :param async: Make an sync or async HTTP request
            :param callback: Callback method called when async is set to true
        """

        gateway.template_id = gateway_template.id
        return self.add_child_object(nurest_object=gateway, async=async, callback=callback)


