VSDK Vanilla
============

SDK Generator for Nuage Network API

Supported version:

    * Python 2.6
    * Python 2.7
    * Python 3

Dependencies
------------

See requirements.txt


Setup via github
----------------

Create your virtualenv :

```
$ virtualenv vsdk-vanilla-env && source vsdk-vanilla-env/bin/activate
```

Then clone the repo :

```
$ git clone git@github.mv.usa.alcatel.com:amercada/vsdk-vanilla.git
```

You'll have to install the dependancies manually. `bambou`
(github.mv.usa.alcatel.com/chserafi/bambou) is not available at
https://pypi.python.org. You can install it directly via github, or configure
pip to use a private pypi repository that hosts bambou. For the latter option, refer to the next section.

Once bambou is installed, you can run :

```
$ pip install -r requirements.txt --allow-external Contextual --allow-unverified Contextual
```

Setup via pip
-------------

Create your virtualenv :

```
$ virtualenv vsdk-vanilla-env && source vsdk-vanilla-env/bin/activate
```

Configure pip to use my privat repo by creating ~/.pip/pip.conf with the following content :

```
[global]
index-url = http://135.227.220.221:8080/simple/
```

Then you can install the package like any other regular package :

```
$ pip install vsdgenerators --allow-external Contextual --allow-unverified Contextual
```

Usage
-----

If you installed the package via `pip` :

```
# generate the vsdk from the 3.2 API available at https://10.31.45.137:8443
$ vsdk-generator -u https://10.31.45.137:8443 -v 3.2

# generate the doc for the vsdk previously generated
$ vsdkdoc-generator -v 3.2

# install the vsdk 
$ cd codegen/3.2 ; python setup.py install ; popd

# we can also generate the API documentation 
$ apidoc-generator -u https://10.31.45.137:8443 -v 3.2
```

If you installed the package via the sources :

```
# generate the vsdk from the 3.2 API available at https://10.31.45.137:8443
$ ./vsdkgenerator -u https://10.31.45.137:8443 -v 3.2

# generate the doc for the vsdk previously generated
$ ./vsdkdocgenerator -v 3.2

# install the vsdk 
$ cd codegen/3.2 ; python setup.py install ; popd

# we can also generate the API documentation 
$ ./apidocgenerator -u https://10.31.45.137:8443 -v 3.2
```

The vsdk and its documentation are generated in `$(pwd)/codegen/<version>`.
The api documentation is generated in `$(pwd)/docgen/`

Work from an existing API version
---------------------------------
This will clone the branch of the given git repository and update the SDK sources according to the VSD API.
_Note: If the branch does not exists, it will automatically create one_

```
$ ./vsdkgenerator -u https://135.227.220.152:8443 -v 3.0 -g http://github.mv.usa.alcatel.com/chserafi/vsdk.git
```


Work from an existing API version and Push
------------------------------------------
This will clone the branch of the given git repository and will push generates sources to the repository
_Note: If the branch does not exists, it will automatically create one_

```
$ ./vsdkgenerator -u https://135.227.220.152:8443 -v 3.0 -g http://github.mv.usa.alcatel.com/chserafi/vsdk.git --push
```

Any Trouble ?
-------------

It can happen ! Do not hesitate to send a quick email to `christophe.serafin@alcatel-lucent.com`
You can also refer to the doc :

* http://135.227.220.221/api30/
* http://135.227.220.221/api32/
* http://135.227.220.221/vsdk30/
* http://135.227.220.221/vsdk32/
