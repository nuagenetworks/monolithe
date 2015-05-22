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
            'id': '1549ea69-c826-46a4-bbfc-d8913744ca09'
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


from monolithe.command import Command
Command.run_tests(vsdurl='https://135.227.222.112:8443', username='csproot', password='csproot', enterprise='csp', version=3.2, data=data)
