# Monolithe

Monolithe is the generator of everything.

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

Monolithe can:

- generate `vsdks`
- generate `vspk`
- generate documentation for `vspk`
- generate VSD Server ReST API documentation.
- generate VSD API Specification
- generate reports of specification conformity of a VSD server
- generate tests for VSD API using specifications


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

    $ vspk-generator -v 3.0 3.1 3.2

The source code for the generated `vspk` package will be available in `codegen/vspk`.


### Generate vspk documentation

To generate the `vspk` API Documentation, run the following command:

    $ vspkdoc-generator

The generated documentation will be available in `docgen/vspkdoc`


### Generate VSD Server ReST API documentation

You can generate a  VSD Server ReST API documentation for a particular API version against a running version of VSD by doing:

    $ vsdapidoc-generator -u VSD_SERVER_API_URL -v VERSION

For instance:

    $ vsdapidoc-generator -u https://api.nuagenetworks.net:8443 -v 3.2

The generated documentation will be available in `docgen/apidoc/{version}`


### Generate API Specification from a VSD Server

You can generate an API specification of any VSD Servers by doing:

    $ spec-generator -u VSD_SERVER_API_URL -v VERSION

For instance:

    $ -generator -u https://api.nuagenetworks.net:8443 -v 3.2

The generated specification will be available in `specgen/{version}`