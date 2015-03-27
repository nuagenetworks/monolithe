# vsdk vanilla

SDK Generator for Nuage Network API

Supported version:

    * Python 2.6
    * Python 2.7


## dependencies

Install the dependencies

    $ pip install -r requirements.txt


# installation

Create a and activate a virtualenv (if you want)

    $ virtualenv vsdk-vanilla-env
    $ cd vsdk-vanilla-env
    $ source bin/activate


## generate and install a new vsdk

This will take default sources and will create a new SDK in `codegen/{{version}}`

You can generate the `vsdk` for a particular API version against a running version of VSD by doing:

    $ vsdkgenerator -u https://url_of_vsd:8443 -v 3.1

You can also generate it from an API definition file if you have one (but you certainly don't):

    $ vsdkgenerator -f /path/to/V3_1

The source code for the generated `vsdk` will be available in `codegen/{version}`.

You can then install it by simply doing:

    $ cd /codegen/3.2
    $ pip install -r requirements.txt && python setup.py install


## generate and install a new vspk

`vspk` is a package that allows to embed multiple `vsdk` version in a same package. This way, it is possible to use multiple VSD API version in the same script.

> Note: you must already have some generated version of `vsdk`

    $ vspkgenerator --version 3.0,3.1,3.2

The generated `vspk` will be in the `codegen/vspk` directory. To install it:

    $ cd codegen/vspk
    $ pip install -r requirements.txt && python setup.py install


# Usage

The official way to use `vsdk` is through `vspk`. You can do something like this in a script:

    from vspk.vsdk import v3_2 as vsdk

    session = vsdk.NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://vsp:8443', version='3.2')
    session.start()

    license = NULicense()
    license.license = LICENSE_BLOB
    session.user.create_child(license)


