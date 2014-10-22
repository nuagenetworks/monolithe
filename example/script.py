# # -*- coding: utf-8 -*-

import sys
sys.path.append("./")

from bambou import NURESTLoginController
from pymodel import NUEnterprise, NUUser, NURESTUser, NUDomainTemplate, NUDomain, NUGatewayTemplate, NUGateway, NUZone, NUZoneTemplate, NUSubNetwork, NUSubNetworkTemplate, NUVPort, NURedirectionTargetTemplate, NURedirectionTarget

# 'Setting a log level to see what happens (Optionnal)'

import logging
bambou_log = logging.getLogger('bambou')
bambou_log.setLevel(logging.DEBUG)
bambou_log.addHandler(logging.StreamHandler())

# 'Log in on the application with csproot user'

controller = NURESTLoginController()
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
enterprise.create_gatewaytemplate(domain_template)
domain = NUDomain()
domain.name = u'Instance Domain example'
enterprise.instantiate_domain(domain, domain_template)

# Create a redirection target template
redirection_target_template = NURedirectionTargetTemplate()
redirection_target_template.name = "RT Template"
domain_template.create_redirectiontargettemplate(redirection_target_template)

# Create a redirection target
redirection_target = NURedirectionTarget()
redirection_target.name = "RT Instance"
domain.create_redirectiontarget(redirection_target)

# 'Create a zone'
zone = NUZone()
zone.name = u'zone example'
domain.create_zone(zone)

# 'Create a zone template'
zone_template = NUZoneTemplate()
zone_template.name = u'Zone Template'
domain_template.create_zonetemplate(zone_template)

# 'Create subnet'
subnet = NUSubNetwork()
subnet.name = u'subnet name'
subnet.address = u'10.0.0.0'
subnet.netmask = u'255.255.255.0'
zone.create_subnet(subnet)

# 'Create subnet template'
subnet_template = NUSubNetworkTemplate()
subnet_template.name = u'subnet template name'
subnet_template.address = u'20.0.0.0'
subnet_template.netmask = u'255.255.255.0'
zone_template.create_subnettemplate(subnet_template)

# 'Create a VPort'
vport = NUVPort()
vport.name = u'VPort example'

subnet.create_vport(vport)


# Comment this line to avoid removing everything that has been created within the script.
enterprise.delete()
