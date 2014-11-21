YamlImporter
============

Create/Update VSD Model into Python Model that could be used with Courgette


Setting up your python environment
----------------------------------

Follow these 3 steps to use your python environment.

1) First, you should install your environment if you have not done already

    $ virtual-env --no-site-packages myenv-env
    $ Installing Setuptools..[]..done.

2) Activate your environment

    $ cd myenv-env
    $ source bin/activate
    (myenv-env) $ cd myenv-env

3) Clone repository

    git clone http://github.mv.usa.alcatel.com/chserafi/myenv.git

4) Install package dependencies listed in requirements.txt file

    (myenv-env) $ cd myenv
    (myenv-env) $ pip install -r requirements.txt


Usage
-----

To autogenerate files, you should use the update-model script:

    (myenv-env) $ cd yamlimporter
    (myenv-env) $ python update-model.py -h
    usage: update-model.py [-h] [-f [FILENAME]] [-d [DESTINATION]]

    VSD Python model - Update the python model from a YAML file.

    optional arguments:
      -h, --help            show this help message and exit
      -f [FILENAME], --filename [FILENAME]
                            YAML file path (default is 'objects.yaml')
      -d [DESTINATION], --destination [DESTINATION]
                            Path to the output models directory

Augenerated files
-----------------

It will generates in your destination path (default is yamlimporter/models):

* an `autogenerates` directory which contains all the python object models that are created from the YAML file
* a `fetchers` directory which contains all fetchers that will enable our models to fetch their children dependencies
* all `nu[object].py` which are the __objects you should actually use and override__. Those files will never be updated.

