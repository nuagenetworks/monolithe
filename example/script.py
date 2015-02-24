# # -*- coding: utf-8 -*-

import sys
import logging

sys.path.append("./")

from vsdk import NUVSDSession
from vsdk import NUEnterprise, NUUser, NUDomainTemplate, NUDomain, NUGatewayTemplate, NUGateway, NUZone, NUZoneTemplate, NUSubnet, NUSubnetTemplate, NUVPort, NURedirectionTargetTemplate, NURedirectionTarget, NUVM, NUVMInterface
from vsdk.utils import set_log_level

from bambou.exceptions import BambouHTTPError

# 'Setting a log level to see what happens (Optionnal)'
set_log_level(logging.INFO)

# 'Create a session for CSPRoot'
session = NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://135.227.220.152:8443', version=u'3.1')

# 'Start using the CSPRoot session
try:
    session.start()
except BambouHTTPError, e:
    print e.request.params
    print e.request.headers
    sys.exit(1)

csproot = session.user

# 'Create an enterprise with csproot user'
enterprise = NUEnterprise()
enterprise.name = u'VSDK Test'
csproot.create_child_object(enterprise)

# 'Create a domain template and an instance'
domain_template = NUDomainTemplate()
domain_template.name = u'Domain Template example'
enterprise.create_child_object(domain_template)
domain = NUDomain()
domain.name = u'Instance Domain example'
enterprise.instantiate_child_object(domain, domain_template)

# # Create a redirection target template
# redirection_target_template = NURedirectionTargetTemplate()
# redirection_target_template.name = "RT Template"
# domain_template.create_child_object(redirection_target_template)
#
# # Create a redirection target
# redirection_target = NURedirectionTarget()
# redirection_target.name = "RT Instance"
# domain.create_child_object(redirection_target)

# 'Create a zone'
zone = NUZone()
zone.name = u'zone example'
domain.create_child_object(zone)

# # 'Create a zone template'
# zone_template = NUZoneTemplate()
# zone_template.name = u'Zone Template'
# domain_template.create_child_object(zone_template)

# 'Create subnet'
subnet = NUSubnet()
subnet.name = u'subnet name'
subnet.address = u'10.0.0.0'
subnet.netmask = u'255.255.255.0'
zone.create_child_object(subnet)

# # 'Create subnet template'
# subnet_template = NUSubnetTemplate()
# subnet_template.name = u'subnet template name'
# subnet_template.address = u'20.0.0.0'
# subnet_template.netmask = u'255.255.255.0'
# zone_template.create_child_object(subnet_template)

# 'Create a VPort'
vport = NUVPort()
vport.name = u'VPort example'

subnet.create_child_object(vport)

# 'Create VM'
# interface = NUVMInterface()
# interface.mac = u"00:12:13:14:18:21"
# interface.ip_address = u"10.0.0.4"
# interface.attached_network_id = subnet.id
#
# vm = NUVM()
# vm.interfaces = [interface.to_dict()]
# vm.name = u'VM TEST'
# vm.uuid = u'2223818b-a56b-46e9-bed1-521761a3653e'

# try:
# csproot.create_child_object(vm)
# except:
#     # Comment this line to avoid removing everything that has been created within the script.
domain_template.delete()
enterprise.delete()
