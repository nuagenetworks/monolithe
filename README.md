# Monolithe

Monolithe is a Python toolset that generates sdks with their documentation and ReST api documentation based some specifications and configuration.

It provides the following commands:

- `monogen-sdk`: generates a bambou-based sdk according to specifications and configuration.
- `monogen-apidoc`: generates ReST api documentation according to specifications and configuration.

The specifications are a set of files containing json data describing one object per file, its properties and their characteristics, and its position in the api hierarchy.

> For more info, please read the [Monolithe Specifications Reference](Specifications Reference.md).

In addition to the specifications, Monolithe uses a configuration that describes all the information relative to your sdk. For instance, you can set its name, the class prefix, some vanilla files, the license, and so on.

> For more info, please read the [Monolithe Configuration & Vanilla Reference](Configuration & Vanilla Reference.md).

Monolithe is before all a framework that you can integrate with other tools.

> For more info, please read the Monolithe API Documentation (TODO).


## Installation

> And remember, kids! You should always be using a virtualenv.

You can install Monolithe from PyPi:

    $ pip install monolithe

Or install it from the source:

    $ python setup.py install

Or install it in develop mode:

    $ python setup.py develop

Or directly run the command wrappers provided in the `commands` directory. Simply install the dependencies once:

    $ pip install -r requirements.txt


## ToDoList Tutorial

You can find an `examples` folder in the source code repository. This contains a working example for a todo list api.
More informations can be found in each files of the examples.

> Be sure to have Flask installed in addition to Monolithe's `requirements.txt`.

The example is composed of:

- Some specifications in `examples/specifications/`
- A Monolithe configuration in `examples/conf/conf.ini`
- Some vanilla data in `examples/vanilla`
- A `demo-server.py` command that starts a really stupid server that implements a ReST API for the ToDoList
- A `demo-client.py` command that interacts with the server using the generated sdk named `tdldk`.

### Step 1: install dependencies

    $ cd monolithe # be sure to go and stay there for the rest of the tutorial ;)
    $ pip install flask
    $ pip install -r `requirements.txt`


### Step 2: generate the tdldk

    $ ./commands/monogen-sdk --config examples/conf/conf.ini --folder examples/specifications

> Customizable using the configuration and the content of the `vanilla/sdk` folder.

> You can also generate the sdk documentation by adding the `--doc` argument. But it's slow.

You'll see a `codegen` directory created under `examples`.

It contains all the auto-generated sdk source code according to the specifications files.

You can install it by doing:

    $ cd examples/codegen
    $ python setup.py develop
    $ cd ../..

> This is mandatory for Step 6

> Don't forget to come back to the root folder

### Step 3: generate the ReST api documentation

    $ ./commands/monogen-apidoc --config examples/conf/conf.ini --folder examples/specifications

> Customizable using the configuration and the content of the `vanilla/apidoc` folder.

You'll see a `apidocgen` directory created under `examples`.

You can open the `index.html` to navigate the api documentation.


### Step 4: start the demo server

    $ ./examples/demo-server.py
    > * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    > * Restarting with stat

check that it's working by doing

    $ curl http://127.0.0.1:5000/api/v1_0/lists
    > [{"description": "Things to buy", "ID": "1", "title": "Shopping List"}, {"description": "You should not see this", "ID": "2", "title": "Secret List"}]


### Step 5: run the client

    $ ./examples/demo-client.py

And follow on screen instructions.

> For mor information, open the `demo-client.py` file and follow the comments.


### Step 6:  have fun with the cli

Each Monolithe SDK comes with a command line interface. According to the Monolithe Configuration file, this cli is named `tdl`.

You can simply run

    # hint: the exports can be put in a source file ;)
    $ export TDL_USERNAME=user
    $ export TDL_PASSWORD=password
    $ export TDL_API_URL=http://127.0.0.1:5000
    $ export TDL_API_VERSION=1.0
    $ export TDL_ENTERPRISE=root

    $ tdl create task --in lists 2 -p title='my task' description='from cli'
    > [Success] task has been created with ID=b3ae22d2-6c87-11e5-be61-080027ba8f35
    > +--------------+--------------------------------------+
    > | status       | TODO                                 |
    > | description  | from cli                             |
    > | title        | my task                              |
    > | parentType   |                                      |
    > | parentID     | 2                                    |
    > | owner        |                                      |
    > | creationDate |                                      |
    > | ID           | b3ae22d2-6c87-11e5-be61-080027ba8f35 |
    > +--------------+--------------------------------------+

    $ tdl list tasks --in lists 2
    > [Success] 3 tasks have been retrieved
    > +----------+---------------------------+---------------------+--------------+------------+---------+----------------+------+
    > | status   | description               | title               | parentType   |   parentID |   owner |   creationDate |   ID |
    > |----------+---------------------------+---------------------+--------------+------------+---------+----------------+------|
    > | TODO     | We are doing it right now | Explain Monolithe   | list         |          2 |         |                |   21 |
    > | TODO     | Almost done               | Make Garuda popular | list         |          2 |         |                |   22 |
    > | TODO     | That is the plan          | Dominate the world  | list         |          2 |         |                |   23 |
    > | TODO     | from cli                  | my task             |              |          2 |         |                |[snip]|
    > +----------+---------------------------+---------------------+--------------+------------+---------+----------------+------+

> `tdl --help` for the complete usage

## Command Line Interfaces Quick Reference

### monogen-sdk
This command will generate a sdk using specifications either from a local folder, or from a Github repository.

#### From Github

Using your username/password:

    $ monogen-sdk --config [conf.ini] --branches [branch1[,branch2,...branchX]]
    > Enter your Github API URL: [https://api.github.com/v3]
    > Enter your Github login: [username]
    > Enter your Github organization: [repo-organization]
    > Enter your Github repository: [repo-name]
    > Enter your Github password for amercada: [password]

Of course, you can give all those parameters right from the cli:

    $ monogen-sdk --config [conf.ini] -g [https://api.gitbhub.com/3] -l [username] -o [repo-organization] -r [repo-name] -b [branch1[,branch2,...branchX]]
    > Enter your Github Password:

You can also use a Github Application Token (https://github.com/settings/tokens):

    $ monogen-sdk --config [conf.ini] -g [https://gitbhub.com] -t [token] -o [repo-organization] -r [repo-name] -b [branch1[,branch2,...branchX]]

Then you won't have to enter your password.

You can also defaults certains arguments by using a environment variables, and eventually put them in a source file:

    $ cat ~/.monorc
    > export MONOLITHE_GITHUB_API_URL=[https://api.github.com/v3]
    > export MONOLITHE_GITHUB_TOKEN=[token]
    > export MONOLITHE_GITHUB_ORGANIZATION=[repo-organization]
    > export MONOLITHE_GITHUB_REPOSITORY=[repo-name]
    > export MONOLITHE_CONFIG_REPOSITORY_PATH=[/path/to/specsfolder]
    > export MONOLITHE_CONFIG_FULLPATH=[path/to/conf]
    $ source ~/.monorc

Then simply:

    $ monogen-sdk -b [branch1[,branch2,...branchX]]


##### From a folder

    $ monogen-sdk --config [conf.ini] --folder [/path/to/specifications/]



#### monogen-apidoc

This command will generate a ReST api documentation using specifications either from a local folder, or from a Github repository.

> This command is very similar to `monogen-sdk`.

##### From a folder

    $ monogen-apidoc --config [conf.ini] --folder [/path/to/specifications/]

##### From Github

The `monogen-apidoc` works exactly the same than `monogen-sdk`

