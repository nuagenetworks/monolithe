VSD SDK for API v3.0
====================

Python SDK for Nuage VSD solution.

Supported version:

    * Python 2.6
    * Python 2.7
    * Python 3

Dependancies
------------

Python dependencies:

    * bambou
    * logging

Setup your Python Virtual Environment
-------------------------------------

Create your virtualenv
::

    $ virtualenv vsdk-env

Activate your environment
::

    $ cd vsdk-env
    $ source bin/activate
    (vsdk-env) $


How it works
------------

Here is a quick example !
::

    from vsdk_V3_0 import NUVSDSession
    from vsdk_V3_0 import NUEnterprise, NUUser, NUDomainTemplate, NUDomain, NUGatewayTemplate, NUGateway, NUZone, NUZoneTemplate, NUSubNetwork, NUSubNetworkTemplate, NUVPort, NURedirectionTargetTemplate, NURedirectionTarget
    from vsdk_V3_0.utils import set_log_level

    # Setting a log level to see what happens (Optionnal)
    set_log_level(logging.INFO)

    # Create a session for user
    session = NUVSDSession(username=u'<YOUR_USERNAME>', password=u'<YOUR_PASSWORD>', enterprise=u'<YOUR_ENTERPRISE>', api_url=u'<YOUR_API_URL/V3_0>')

    # Start using the user session
    session.start()
    user = session.user

    # Create an enterprise with user user
    enterprise = NUEnterprise()
    enterprise.name = u'Enterprise example'
    user.add_child_object(enterprise)

    # Create a domain template and an instance
    domain_template = NUDomainTemplate()
    domain_template.name = u'Domain Template example'
    enterprise.add_child_object(domain_template)
    domain = NUDomain()
    domain.name = u'Instance Domain example'
    enterprise.instantiate_child_object(domain, domain_template)

    # Create a redirection target template
    redirection_target_template = NURedirectionTargetTemplate()
    redirection_target_template.name = "RT Template"
    domain_template.add_child_object(redirection_target_template)
