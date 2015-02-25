Installation
============

This section explains how to install vsdk from vdsk-vanilla.


Generation and Installation from  VSDK Vanilla
----------------------------------------------

VSDK Vanilla is a repository that contains everything needed to generate the following:

- The VSDK
- The API Documentation of VSD
- The VSDK API Documentation from VSDK
- Unit tests for the VSDK

.. note:: If you want to use a published version of the VSDK, you don't need to read this part.


Setting up the environment
+++++++++++++++++++++++++++

.. code-block:: bash
    :linenos:

    # create a virtual env
    cd /some/path/
    virtualenv vsdk-env
    cd vsdk-env
    source bin/activate

    # install dependency (this won't be necessary soon)
    pip install Contextual==0.7a1.dev-r2695 --allow-external Contextual --allow-unverified Contextual

    # install bambou
    git clone http://[your-login]@github.mv.usa.alcatel.com/chserafi/bambou.git
    cd bambou
    pip install -r requirements.txt
    python setup.py install

    # get the vsdk vanilla repository
    cd /some/path/
    git clone http://[your-login]@github.mv.usa.alcatel.com/amercada/vsdk-vanilla.git
    pip install -r requirements.txt



Generating VSDK
+++++++++++++++

From the same python virtualenv (be sure it's active)

.. code-block:: bash
    :linenos:

    cd vsdk-vanilla
    # ./vsdkgenerator.py -u [address of running VSD Server] -v [version of the API]
    ./vsdkgenerator.py -u https://api.nuagenetworks.net:8443 -v 3.2
    cd codegen/3.2
    python setup.py install


Generating VSD API Documentation
++++++++++++++++++++++++++++++++

From the same python virtualenv (be sure it's active)

.. code-block:: bash
    :linenos:

    cd vsdk-vanilla
    # ./docgenerator.py -u [address of running VSD Server] -v [version of the API]
    ./docgenerator.py  -u https://api.nuagenetworks.net:8443 -v 3.2

The doc will be available in ./docgen/[version]/apidoc


Generating VSDK Reference Documentation
+++++++++++++++++++++++++++++++++++++++

From the same python virtualenv (be sure it's active)

.. note:: the source of generated VSDK must be available in `codegen/[version]`

.. code-block:: bash
    :linenos:

    cd vsdk-vanilla
    # ./vsdkdocgenerator.py -v [version of the API]
    ./vsdkdocgenerator.py -v 3.2

The doc will be available in ./docgen/[API-VERSION]/vsdkdoc
