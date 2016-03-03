# ToDoList Tutorial

You can find an `examples` folder in the source code repository. This contains a working example for a todo list api.
More informations can be found in each files of the examples.

> Be sure to have Flask installed in addition to Monolithe's `requirements.txt`.

The example is composed of:

- Some specifications in `examples/specifications/`
- Some vanilla data in `examples/vanilla`
- A `demo-server.py` command that starts a really stupid server that implements a ReST API for the ToDoList
- A `demo-client.py` command that interacts with the server using the generated sdk named `tdldk`.

## Step 1: install dependencies

    cd monolithe # be sure to go and stay there for the rest of the tutorial ;)
    pip install flask
    pip install -r `requirements.txt`


## Step 2: generate the tdldk

    ./commands/monogen -f examples/specifications -L python

> Customizable using the configuration and the content of the `vanilla/python` folder.

> You can also generate the sdk documentation by adding the `--doc` argument. But it's slow.

You'll see a `codegen/python` directory created under `examples`.

It contains all the auto-generated sdk source code according to the specifications files.

You can install it by doing:

    cd examples/codegen
    python setup.py develop
    cd ../..

> This is mandatory for Step 6

> Don't forget to come back to the root folder

## Step 3: generate the ReST api documentation

    ./commands/monogen -f examples/specifications -L html

> Customizable using the configuration and the content of the `vanilla/html` folder.

You'll see a `codegen/html` directory created under `examples`.

You can open the `index.html` to navigate the api documentation.


## Step 4: start the demo server

    ./examples/demo-server.py
    > * Running on http://127.0.0.1:5555/ (Press CTRL+C to quit)
    > * Restarting with stat


## Step 5: run the client

    ./examples/demo-client.py

And follow on screen instructions.

> For mor information, open the `demo-client.py` file and follow the comments.


## Step 6:  have fun with the cli

Each Monolithe SDK comes with a command line interface. According to the Monolithe Configuration file, this cli is named `tdl`.

You can simply run

    # hint: the exports can be put in a source file ;)
    export TDL_USERNAME=user
    export TDL_PASSWORD=password
    export TDL_API_URL=http://127.0.0.1:5555
    export TDL_API_VERSION=1.0
    export TDL_ENTERPRISE=root

    $ tdl create task --in lists 2 -p title='my task' description='from cli'
    > [Success] task has been created with ID=b3ae22d2-6c87-11e5-be61-080027ba8f35
    > +--------------+--------------------------------------+
    > | status       | TODO                                 |
    > | description  | from cli                             |
    > | title        | my task                              |
    > | parentType   | <the demo server doesn't handle that>|
    > | parentID     | 2                                    |
    > | owner        | <the demo server doesn't handle that>|
    > | creationDate | <the demo server doesn't handle that>|
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

