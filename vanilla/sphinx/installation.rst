Installation
============

This section explains how to install vsdk.

.. note:: this manual may not be up to date until the release 1.0 of `vsdk`.


VSDK Installation from zips
---------------------------

You can set up a virtual environment if you like:

.. code-block:: bash
  :linenos:

  virtualenv vsdk-env
  cd vsdk-env
  source bin/activate


Then download the zips archives for `Bambou` and `vsdk`. Then run the following commands:

.. code-block:: bash
  :linenos:

  pip install Contextual==0.7a1.dev-r2695 --allow-external Contextual --allow-unverified Contextual
  pip install bambou-*.zip
  pip install vsdk-*-api*.zip



VSDK Installation from PIP
--------------------------

.. note:: This is not possible to do this today. Please see `VSDK Installation from zips`_ or `VSDK Vanilla`_.

Install the VSDK from a public source:

.. code-block:: bash
    :linenos:

    pip install vsdk


Or install it from a local git repository:

.. code-block:: bash
    :linenos:

    pip install git+ssh://github.com/nuagenetworksgithub.com:vsdk/vsdk.git


VSDK Vanilla
------------

VSDK Vanilla is a repository that contains everything needed to generate:

- The VSDK from a running VSD server or a VSD generated swagger file
- The VSDK API Reference from VSDK (this document)

.. note:: If you want to use a published version of the VSDK, see `VSDK Installation from zips`_ or `VSDK Installation from PIP`_.


Set up a Virtual Environment
++++++++++++++++++++++++++++

First, create a virtual environment and make it active:

.. code-block:: bash
    :linenos:

    virtualenv vsdk-env
    cd vsdk-env
    source bin/activate

    # Manually install one missing dependency (this won't be necessary soon):
    pip install Contextual==0.7a1.dev-r2695 --allow-external Contextual --allow-unverified Contextual


Install Bambou
++++++++++++++

Get the `Bambou` source code and install it in the virtual env:

.. code-block:: bash
    :linenos:

    # cd to the root folder to your virtual env
    git clone http://$GIT_USERNAME@github.mv.usa.alcatel.com/vsdk/bambou.git
    cd bambou
    pip install -r requirements.txt
    python setup.py install

.. note:: Instead of `python setup.py install`, you can do `python setup.py develop`. This will allow you to update `Bambou` in your virtual env by simply doing `git pull origin master`.


Get vsdk-vanilla
++++++++++++++++

Get the `vsdk-vanilla` repository and install the requirements:

.. code-block:: bash
    :linenos:

    # cd to the root folder to your virtual env
    git clone http://$GIT_USERNAME@github.mv.usa.alcatel.com/vsdk/vsdk-vanilla.git
    pip install -r requirements.txt


Generate the VSDK
+++++++++++++++++

.. note:: you need to have a running VSD server, or a VSD swagger API description file.

From the same python virtualenv (be sure it's active)

.. code-block:: bash
    :linenos:

    # cd to the vsdk-vanilla folder to your virtual env
    ./vsdkgenerator -u $RUNNING_VSD_SERVER -v $API_VERSION
    cd codegen/3.2
    python setup.py install

.. note:: Instead of `python setup.py install`, you can do `python setup.py develop`. This will allow you to update `VSDK` in your virtual env by simply regenerating it with the `vssdkgenerator`.


Generate the VSDK Reference
+++++++++++++++++++++++++++

.. note:: the source of generated VSDK must be available in `codegen/$API_VERSION`.

From the same python virtualenv (be sure it's active)

.. code-block:: bash
    :linenos:

    # cd to the vsdk-vanilla folder to your virtual env
    ./vsdkdocgenerator -v $API_VERSION

The doc will be available in `docgen/$API-VERSION/vsdkdoc`


VSDK Vanilla Lazy Install Script
--------------------------------

You can use this dirty little script to prepare your `vsdk-vanilla` environment :

.. code-block:: bash
    :linenos:

    #!/bin/bash

    VENV_NAME=$1
    GIT_USERNAME=$2
    RUNNING_VSD_SERVER=$3
    API_VERSION=$4

    if [[ -z $VENV_NAME || -z $GIT_USERNAME || -z $RUNNING_VSD_SERVER || -z $API_VERSION ]]; then
        echo "Invalid arguments"
        echo "USAGE: $0 virtual_env_name git_username vsd_server_api_url api_version"
        echo
        echo "    sExample: $0 vsdk-env amercada https://api.nuagenetworks.net:8443 3.2"
        echo
        exit 1
    fi

    virtualenv $VENV_NAME && \
    cd $VENV_NAME && \
    source bin/activate && \
    pip install Contextual==0.7a1.dev-r2695 --allow-external Contextual --allow-unverified Contextual && \
    git clone http://$GIT_USERNAME@github.mv.usa.alcatel.com/vsdk/bambou.git && \
    cd bambou && \
    pip install -r requirements.txt && \
    python setup.py develop && \
    cd .. && \
    git clone http://$GIT_USERNAME@github.mv.usa.alcatel.com/vsdk/vsdk-vanilla.git && \
    cd vsdk-vanilla && \
    pip install -r requirements.txt && \
    ./vsdkgenerator -u $RUNNING_VSD_SERVER -v $API_VERSION && \
    cd codegen/3.2 && \
    python setup.py install && \
    echo "" && \
    echo "[DONE] now run:" && \
    echo "    cd $VENV_NAME && source bin/activate"
