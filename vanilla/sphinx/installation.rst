Installation
============

This section explains how to install vspk.

Install the vspk from a public source:

.. code-block:: bash
    :linenos:

    pip install vspk


Monolithe
---------

`monolithe` is a repository that contains everything needed to generate:

- The `vsdk` from a running VSD server or a VSD generated swagger file
- The `vspk` from a list of generated `vsdk` (this document)
- The `vspk` api documentation
- The VSD ReST API api documentation


Set up a Virtual Environment
++++++++++++++++++++++++++++

First, create a virtual environment and make it active:

.. code-block:: bash
    :linenos:

    virtualenv vspk-env
    cd k-env
    source bin/activate


Install Bambou
++++++++++++++

Get the `Bambou` source code and install it in the virtual env:

.. code-block:: bash
    :linenos:

    # cd to the root folder to your virtual env
    pip install bambou


Get monolithe
++++++++++++++++

Get the `monolithe` repository and install the requirements:

.. code-block:: bash
    :linenos:

    # cd to the root folder to your virtual env
    git clone https://github.com/nuagenetworks/monolithe.git
    cd monolithe
    pip install -r requirements.txt


Generate the vspk
+++++++++++++++++

.. note:: you need to have a running VSD server, or a VSD swagger API description file.

You must generate the vsdk versions you want to include in the vspk, then generate the vspk.

From the same python virtualenv (be sure it's active)

.. code-block:: bash
    :linenos:

    ./vsdkgenerator -u $RUNNING_VSD_SERVER -v 3.0
    ./vsdkgenerator -u $RUNNING_VSD_SERVER -v 3.1
    ./vsdkgenerator -u $RUNNING_VSD_SERVER -v 3.2
    ./vspkgenerator --versions 3.0 3.1 3.2

The results will be available in the `codegen` directory.
