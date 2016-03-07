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

`monogen` command will generate a sdk using specifications either from a local folder, or from a Github repository.

```
usage: monogen [-h] [-g github_api_url] [-l login_login] [-t github_token]
               [-o github_organization] [-r github_repository]
               [-b [branches [branches ...]]] [-p path] [-f folder]
               [-c config_path] [-d] [--vanilla-prefix VANILLA_PREFIX]
               [--generation-version GENERATION_VERSION] [-L LANGUAGE]

Generates a SDK according from a specification set

optional arguments:

  -h, --help            show this help message and exit
  -g github_api_url, --github github_api_url
                        The GitHub API URL. Can be given by setting the
                        environment variable "MONOLITHE_GITHUB_API_URL"
  -l login_login, --login login_login
                        The GitHub Login (if set, you will be prompted for
                        your password). Can be given by setting the
                        environment variable "MONOLITHE_GITHUB_LOGIN"
  -t github_token, --token github_token
                        The GitHub Token (if set, --login will be ignored). To
                        generate a token, go here
                        https://github.com/settings/tokens. Can be given by
                        setting the environment variable
                        "$MONOLITHE_GITHUB_TOKEN"
  -o github_organization, --organization github_organization
                        The GitHub Organization. Can be given by setting the
                        environment variable "MONOLITHE_GITHUB_ORGANIZATION"
  -r github_repository, --repository github_repository
                        The GitHub Repository. Can be given by setting the
                        environment variable "MONOLITHE_GITHUB_REPOSITORY"
  -b [branches [branches ...]], --branches [branches [branches ...]]
                        The branches of the specifications to use to generate
                        the documentation (examples: "master 3.2")
  -p path, --path path  The relative repository path of the specification
                        folder. Can be given by setting the environment
                        variable "MONOLITHE_GITHUB_REPOSITORY_PATH"
  -f folder, --folder folder
                        Path of the specifications folder. If set, all other
                        attributes will be ignored
  -c config_path, --config config_path
                        Path the monolithe configuration file
  -d, --doc             generate documentation of the SDK
  --vanilla-prefix VANILLA_PREFIX
                        Prefix added to all vanilla path declared in the
                        monolithe configuration file
  --generation-version GENERATION_VERSION
                        Overwrite the sdk version given in monolithe.conf
  -L LANGUAGE, --language LANGUAGE
                        Choose the output language of the SDK. Default is
                        python
```
