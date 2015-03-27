Python SDK for VSD
==================

Python SDK for Nuage VSD solution.

*Website: http://www.nuagenetworks.net/*

Supported version:

    * Python 2.6
    * Python 2.7

Dependencies
------------

Python dependencies (see `requirements.txt` file)

    * bambou
    * logging

Setup your Python Virtual Environment
-------------------------------------

_Note: If you do not have virtualenv installed, use `pip install virtualenv` to install it on your system_

Create your `virtualenv`

    $ virtualenv vsdk-env

Activate your environment

    $ cd vsdk-env
    $ source bin/activate
    (vsdk-env) $ # You are now inside your python virtual environment


How it works ?
--------------

Here is a quick example !

    # # -*- coding: utf-8 -*-

    from vsdk import NUVSDSession
    from vsdk import NUEnterprise, NUUser, NUDomainTemplate, NUDomain, NUGatewayTemplate, NUGateway, NUZone, NUZoneTemplate, NUSubnet, NUSubnetTemplate, NUVPort, NURedirectionTargetTemplate, NURedirectionTarget, NUVM, NUVMInterface

    # 'Create a session for CSPRoot'
    session = NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://vsd:8443', version=u'3.1')

    # 'Start using the CSPRoot session
    session.start()
    csproot = session.user

    # Create an enterprise with csproot user
    enterprise = NUEnterprise()
    enterprise.name = u'VSDK Test'
    csproot.create_child(enterprise)

    # Create a domain template and an instance
    domain_template = NUDomainTemplate()
    domain_template.name = u'Domain Template example'
    enterprise.create_child(domain_template)
    domain = NUDomain()
    domain.name = u'Instance Domain example'
    enterprise.instantiate_child(domain, domain_template)

    # Delete created objects
    domain_template.delete()
    enterprise.delete()