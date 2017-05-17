# Monolithe

[![Join the chat at https://gitter.im/nuagenetworks/monolithe](https://badges.gitter.im/nuagenetworks/monolithe.svg)](https://gitter.im/nuagenetworks/monolithe?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Monolithe is a Python toolset that can transform a set a specification to something else, like a sdk or a documentation.

It provides the `monogen` command that will transform the specification into the specified language.

The specifications are a set of files containing json data describing one object per file, its properties and their characteristics, and its position in the api hierarchy.

> For more info, please read the [Monolithe Specifications Reference](doc/Specifications Reference.md).

In addition to the specifications, Monolithe uses a configuration that describes all the information relative to your sdk. For instance, you can set its name, the class prefix, some vanilla files, the license, and so on.

> For more info, please read the [Monolithe Configuration & Vanilla Reference](doc/Configuration & Vanilla Reference.md).

Monolithe is not monolithic! While it provides three default transformers (Python, Go and HTML), you can create your own compatible language plugins. 

> For more info, please read the [Language Plugins Documentation](doc/Language Plugins.md).

This repository contains a full small example on how to use Monolithe, located in the `examples` folder.

> For more info, please read the [ToDoList Tutorial](doc/ToDoList Tutorial.md). 

## Installation

> And remember, kids! You should always be using a virtualenv.

Install Monolithe by running the following command:

    pip install git+https://github.com/nuagenetworks/monolithe.git


## Command Line Interfaces Quick Reference

`monogen` command will generate a sdk using specifications from a local folder. It also handles git repositories in case you want to generate an SDK from multiple branches of the same repository.

```
usage: monogen [-h] [-b [branches [branches ...]]] -f folder [-c config_path]
               [--vanilla-prefix VANILLA_PREFIX]
               [--generation-version GENERATION_VERSION] [-L LANGUAGE]

Generates a SDK according from a specification set

optional arguments:
  -h, --help            show this help message and exit
  -b [branches [branches ...]], --branches [branches [branches ...]]
                        The branches of the specifications to use to generate
                        the documentation (examples: "master 3.2")
  -f folder, --folder folder
                        Path of the specifications folder. If set, all other
                        attributes will be ignored
  -c config_path, --config config_path
                        Path the monolithe configuration file
  --vanilla-prefix VANILLA_PREFIX
                        Prefix added to all vanilla path declared in the
                        monolithe configuration file
  --generation-version GENERATION_VERSION
                        Overwrite the sdk version given in monolithe.conf
  -L LANGUAGE, --language LANGUAGE
                        Choose the output language of the SDK. Default is
                        python
```
