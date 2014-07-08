pymodel
=======

Nuage Network Python Model according to RESTNuage library

Example
=======

     from restnuage import NURESTLoginController
     from courgette.models import NUEnterprise, NUUser, NURESTUser, NUDomainTemplate, NUDomain,NUGatewayTemplate, NUGateway
     
     # Setting a log level to see what happens (Optionnal)
     
     # restnuage_log = logging.getLogger('restnuage')
     # restnuage_log.setLevel(logging.DEBUG)
     # restnuage_log.addHandler(logging.StreamHandler())

     # Log in on the application with csproot user
     
     controller = NURESTLoginController()
     controller.user = u"csproot"
     controller.password = u"csproot"
     controller.enterprise = u"csp"
     controller.url = u"https://135.227.220.152:8443/nuage/api/v3_0"
     csproot = NURESTUser()
     csproot.fetch()
     controller.api_key = csproot.api_key

     # Create an enterprise with csproot user
     enterprise = NUEnterprise()
     enterprise.name = u'Enterprise example'
     csproot.create_enterprise(enterprise)

     # Create a domain template and an instance
     domain_template = NUDomainTemplate()
     domain_template.name = u'Domain Template example'
     enterprise.create_gateway_template(domain_template)
     domain = NUDomain()
     domain.name = u'Instance Domain example'
     enterprise.instanciate_domain(domain, domain_template)
