# Python SDK for VSD

Python SDK for Nuage VSD solution.

*Website: http://www.nuagenetworks.net/*

Supported version:


## Setup your Python Virtual Environment

_Note: If you do not have virtualenv installed, use `pip install virtualenv` to install it on your system_

Create your `virtualenv`

    $ virtualenv vsdk-env

Activate your environment

    $ cd vsdk-env
    $ source bin/activate
    (vsdk-env) $ # You are now inside your python virtual environment


## How it works ?

Here is a quick example !

    # # -*- coding: utf-8 -*-

    from vsdk import NUVSDSession
    from vsdk import NUEnterprise, NUUser, NUDomainTemplate, NUDomain, NUGatewayTemplate, NUGateway, NUZone, NUZoneTemplate, NUSubnet, NUSubnetTemplate, NUVPort, NURedirectionTargetTemplate, NURedirectionTarget, NUVM, NUVMInterface

    # 'Create a session for CSPRoot'
    session = NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://vsd:8443')

    # 'Start using the CSPRoot session
    session.start()
    csproot = session.user

    # Create an enterprise with csproot user
    enterprise = NUEnterprise()
    enterprise.name = u'vsdk Test'
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


## License

Copyright (c) 2015, Alcatel-Lucent Inc
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the copyright holder nor the names of its contributors
      may be used to endorse or promote products derived from this software without
      specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.