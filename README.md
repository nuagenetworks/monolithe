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
* bambou (http://github.mv.usa.alcatel.com/chserafi/bambou)

WARNING: You will need to install `bambou` library first.

Setup your Python Virtual Environment
-------------------------------------

Install your virtualenv

    $ virtualenv --no-site-packages vsdk-env

Activate your environment

    $ cd vsdk-env
    $ source bin/activate
    (vsdk-env) $

Installation from package
-------------------------

Note: Before install, make sure you have activated your python environment

Download the `tar.gz` file that is distributed in `dist` directory and install it using pip:

    (vsdk-env) $ pip install git+ssh://github.mv.usa.alcatel.com/chserafi/bambou#egg=bambou
    (vsdk-env) $ pip install git+ssh://github.mv.usa.alcatel.com/chserafi/vsdk.git#egg=vsdk

Installation from package in development
----------------------------------------

Note: Before install, make sure you have activated your python environment

This enables you to install both packages and see sources in your python environment

    (vsdk-env) $ pip install -e git+ssh://github.mv.usa.alcatel.com/chserafi/bambou#egg=bambou
    (vsdk-env) $ pip install -e git+ssh://github.mv.usa.alcatel.com/chserafi/vsdk.git#egg=vsdk


Installation from sources
-------------------------

Get the sources

    (vsdk-env) $ git clone http://github.mv.usa.alcatel.com/cserafin/vsdk.git
    (vsdk-env) $ cd vsdk

Install dependencies

    (vsdk-env) $ pip install -r requirements.txt


Example
-------

Here is a quick example !

     from restnuage import NURESTLoginController
     from vsdk import NUEnterprise, NUUser, NURESTUser, NUDomainTemplate, NUDomain,NUGatewayTemplate, NUGateway

     # Setting a log level to see what happens (Optionnal)

     # import logging
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
     enterprise.instantiate_domain(domain, domain_template)


Check a complete example in `examples/scripts.py`. You can launch the example using the following command line:

    $ python example/script.py

Packaging
---------

Creating a tar.gz package is possible using the following command line :

    $ python setup.py sdist

