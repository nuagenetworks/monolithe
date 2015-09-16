# Monolithe

Monolithe is the generator of all documentation and SDK for Nuage Network VSP.

Supported version:

    * Python 2.6
    * Python 2.7



## Installation

### Install  from package

You can get Monolithe from PyPi:

    $ pip install monolithe

### Install  from sources

If not already done, get the source code:

    $ git clone https://github.com/nuagenetworks/monolithe.git

Then install the dependencies:

    $ cd monolithe
    $ pip install -r requirements.txt

### Generate a package

You can get generate a package Monolithe:

    $ python setup.py sdist

The package will be created in `dist`


## Usage

Monolithe can :

- generate the `vspk`
- generate the documentation for `vspk`
- generate the VSD api documentation
- generate api specification files
- validate a vsd server against the api specification


### Generate vspk package

Once all the `vsdk` versions you want to include in `vspk` have been generated, run the following command:

    $ generate-vspk -u VSD_SERVER_API_URL -v [VERSIONS]

For instance:

    $ generate-vspk -u https://myvsd.com:8443 -v 3.0 3.1 3.2

The source code for the generated `vsdp` package will be available in `codegen/vspk`.


### Generate vspk documentation

To generate the `vspk` API Documentation, run the following command (after having generated a `vspk`):

    $ generate-sdkdoc

The generated documentation will be available in `docgen/sdkdoc`


### Generate VSD Server ReST API documentation

You can generate a  VSD Server ReST API documentation for a particular API version against a running version of VSD by doing:

    $ generate-apidoc -u VSD_SERVER_API_URL -v VERSION

For instance:

    $ generate-apidoc -u https://api.nuagenetworks.net:8443 -v 3.0
    $ generate-apidoc -u https://api.nuagenetworks.net:8443 -v 3.1
    $ generate-apidoc -u https://api.nuagenetworks.net:8443 -v 3.2

The generated documentation will be available in `docgen/apidoc/{{version}}`


## Note

All commands that require to pass VSD informations such as vsd url, version, username, organization, etc can use environment variables

    VSD_USERNAME
    VSD_PASSWORD
    VSD_API_URL
    VSD_API_VERSION
    VSD_ENTERPRISE