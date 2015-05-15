vsd_options = {
    'vsdurl': 'https://135.227.222.112:8443',
    'username': 'csproot',
    'password': 'csproot',
    'enterprise': 'csp',
    'version': 3.2
}

data = {'parentObject' :
        {
            'resourceName': 'enterprises',
            'id': '4aae6a26-6427-4055-b514-ecd73524823b'
        },
        'RESTName': 'group', # Name to search for the specification (Temporary)
        'defaultValues' :
        {
            'name': 'A group',
            'description': 'a random group',
            'private': 'false',
            'accountRestrictions': 'true'
        },
        'spec': {} # Should be the JSON spec. Empty for now
       }


from monolithe import Command
Command.run_tests(vsdurl='https://135.227.222.112:8443', username='csproot', password='csproot', enterprise='csp', version=3.2, data=data)
