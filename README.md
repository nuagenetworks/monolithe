pymodel
=======

Nuage Network Python Model according to RESTNuage library

Dependancies
------------

Python dependencies:
* logging
* restnuage

Installation from package
-------------------------

Download the `tar.gz` file that is distributed in `dist` directory and install it using pip:

    $ pip install packages/restnuage-xxx.tar.gz
    $ pip install pymodel-xxx.tar.gz

WARNING: You will need to install `restnuage` library first.

Installation from sources
-------------------------

Install your virtualenv

    $ virtualenv --no-site-packages pymodel-env

Activate your environment

    $ cd pymodel-env
    $ source bin/activate
    (pymodel-env) $

Get the sources

    (pymodel-env) $ git clone http://github.mv.usa.alcatel.com/cserafin/pymodel.git
    (pymodel-env) $ cd pymodel

Install dependencies

    (pymodel-env) $ pip install -r requirements.txt


Configuration
-------------

To configure your environment, just put a `settings.cfg` file including

* the user you want to connect with
* the password of your user
* the enterprise name
* the url to your VSD Server

Here is a basic configuration file example:

    [default]
    user = csproot
    password = csproot
    enterprise = csp
    url = https://135.227.220.152:8443/nuage/api/v3_0


Example
-------

Here is a quick example !

     from restnuage import NURESTLoginController
     from pymodel.models import NUEnterprise, NUUser, NURESTUser, NUDomainTemplate, NUDomain,NUGatewayTemplate, NUGateway

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

