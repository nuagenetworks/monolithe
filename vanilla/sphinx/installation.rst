Installation
============

Installation from PyPi
----------------------

Install vspk
++++++++++++

To install `vspk`, run the following command:

.. code-block:: bash
    :linenos:

    pip install vspk


Install vsdcli
++++++++++++++

We also provide a command line interface named `vsd` that allows to interact with a VSD Server. This command uses introspection on the `vspk` and will work with all API versions supported by your current `vspk` installation. By updating the `vspk`, the cli will be automagically up to date to.

To install `vsdcli`, run the following command:

.. code-block:: bash
    :linenos:

    pip install vsdcli



Installation from Monolithe
---------------------------

`Monolithe` is a package that contains everything needed to generate:

- The `vsdk` from a running VSD server or a VSD generated swagger file
- The `vspk` from a list of generated `vsdk` (this document)
- The `vspk` api documentation
- The VSD ReST API api documentation


Install Monolite
++++++++++++++++

Get `Monolithe` from PyPi

.. code-block:: bash
    :linenos:

    pip install monolithe


Generate the vspk
+++++++++++++++++

.. note:: You need to have a running VSD server.

.. note:: You must generate the all the `vsdk` versions you want to include in the `vspk` first.

.. note:: This generates a raw python source package. This package can be installed using any installation method provided by Python.

To generate the `vspk` package, run the following commands:

.. code-block:: bash
    :linenos:

    vsdk-generator -u $RUNNING_VSD_SERVER -v 3.0
    vsdk-generator -u $RUNNING_VSD_SERVER -v 3.1
    vsdk-generator -u $RUNNING_VSD_SERVER -v 3.2
    vspk-generator --versions 3.0 3.1 3.2

The results will be available in `codegen/vspk`. You can now install it the way you want


Generate the VSPK API Documentation
+++++++++++++++++++++++++++++++++++

.. note:: You need to have a generated `vspk` available in the `codegen` directory.

To generate the `vspk` documentation (what you are reading right now), run the following commands:

.. code-block:: bash
    :linenos:

    vspkdoc-generator

The results will be available in `docgen/vspkdoc`.


Generate the VSD Server ReST API Documentation
++++++++++++++++++++++++++++++++++++++++++++++

Todo
