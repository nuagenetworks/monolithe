# # -*- coding: utf-8 -*-

import sys
sys.path.append("../")

from restnuage import NURESTLoginController
from pymodel import NUEnterprise, NUUser, NURESTUser, NUDomainTemplate, NUDomain, NUGatewayTemplate, NUGateway, NUZone, NUZoneTemplate, NUSubnet, NUSubnetTemplate, NUVPort

# 'Setting a log level to see what happens (Optionnal)'

import logging
restnuage_log = logging.getLogger('restnuage')
restnuage_log.setLevel(logging.DEBUG)
restnuage_log.addHandler(logging.StreamHandler())

# 'Log in on the application with csproot user'

controller = NURESTLoginController.get_default_instance()
controller.user = u"csproot"
controller.password = u"csproot"
controller.enterprise = u"csp"
controller.url = u"https://135.227.220.152:8443/nuage/api/v3_0"
csproot = NURESTUser()
csproot.fetch()
controller.api_key = csproot.api_key

# 'Create an enterprise with csproot user'
enterprise = NUEnterprise()
enterprise.name = u'Enterprise example'
csproot.create_enterprise(enterprise)

# 'Create a domain template and an instance'
domain_template = NUDomainTemplate()
domain_template.name = u'Domain Template example'
enterprise.create_gateway_template(domain_template)
domain = NUDomain()
domain.name = u'Instance Domain example'
enterprise.instanciate_domain(domain, domain_template)

# 'Create a zone'
zone = NUZone()
zone.name = u'zone example'
domain.create_zone(zone)

# 'Create a zone template'
zone_template = NUZoneTemplate()
zone_template.name = u'Zone Template'
domain_template.create_zone_template(zone_template)

# 'Create subnet'
subnet = NUSubnet()
subnet.name = u'subnet name'
subnet.address = u'10.0.0.0'
subnet.netmask = u'255.255.255.0'
zone.create_subnet(subnet)

# 'Create subnet template'
subnet_template = NUSubnetTemplate()
subnet_template.name = u'subnet template name'
subnet_template.address = u'20.0.0.0'
subnet_template.netmask = u'255.255.255.0'
zone_template.create_subnet_template(subnet_template)

# 'Create a VPort'
vport = NUVPort()
vport.name = u'VPort example'

subnet.create_vport(vport)