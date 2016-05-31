# README goes here

Please follow these steps to test the client and server

    $ cd monolithe
    $ monogen -f examples/specifications
    [log] retrieving specifications from folder "examples/specifications/"
    [log] 5 specifications retrieved from folder "examples/specifications/" (api version: 1.0)
    [log] transforming specifications into python for version 1.0...
    [log] assembling...
    [success] tdldk generation complete and available in "examples/codegen/python"

    $ cd examples/codegen/python
    $ python setup.py develop
    $ cd ../..

    # Serve the server
    $ python demo-server.py
    # Serve the client
    $ python demo-client.py
