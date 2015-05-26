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



## Usage

Monolithe can generate:

- various versions of `vsdk`
- a `vspk` including various version of `vsdks`
- the documentation for `vspk`
- various versions of VSD Server ReST API documentation.


### Generate vsdk packages

You can generate a `vsdk` for a particular API version against a running version of VSD by doing:

    $ vsdk-generator -u VSD_SERVER_API_URL -v VERSION

For instance:

    $ vsdk-generator -u https://api.nuagenetworks.net:8443 -v 3.0
    $ vsdk-generator -u https://api.nuagenetworks.net:8443 -v 3.1
    $ vsdk-generator -u https://api.nuagenetworks.net:8443 -v 3.2

The source code for the generated `vsdk` packages will be available in `codegen/{version}`.


### Generate vspk package

Once all the `vsdk` versions you want to include in `vspk` have been generated, run the following command:

    $ vspk-generator --version 3.0 3.1 3.2

The source code for the generated `vsdp` package will be available in `codegen/vspk`.


### Generate vspk documentation

To generate the `vspk` API Documentation, run the following command:

    $ vspkdoc-generator

The generated documentation will be available in `docgen/vspkdoc`


### Generate VSD Server ReST API documentation

You can generate a  VSD Server ReST API documentation for a particular API version against a running version of VSD by doing:

    $ apidoc-generator -u VSD_SERVER_API_URL -v VERSION

For instance:

    $ apidoc-generator -u https://api.nuagenetworks.net:8443 -v 3.0
    $ apidoc-generator -u https://api.nuagenetworks.net:8443 -v 3.1
    $ apidoc-generator -u https://api.nuagenetworks.net:8443 -v 3.2

The generated documentation will be available in `docgen/apidoc/{{version}}`
