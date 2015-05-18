vsd_options = {
    'vsdurl': 'https://135.227.222.112:8443',
    'username': 'csproot',
    'password': 'csproot',
    'enterprise': 'csp',
    'version': 3.2
}

data = {'parentObject' :
        {
            'resourceName': 'subnets',
            'id': '41fb2560-8080-4d56-a1a8-c41bc6b00c4b'
        },
        'RESTName': 'addressrange', # Name to search for the specification (Temporary)
        'defaultValues' :
        {
            'DHCPPoolType' : 'HOST',
            'maxAddress' : '10.34.17.10',
            'minAddress' : '10.34.17.20'
        },
        'spec': {} # Should be the JSON spec. Empty for now
       }


from monolithe import Command
Command.run_tests(vsdurl='https://135.227.222.112:8443', username='csproot', password='csproot', enterprise='csp', version=3.2, data=data)
