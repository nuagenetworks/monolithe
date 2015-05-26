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
            'id': '28dde1d1-a37d-4b1a-a0ae-96f1c20c7d02'
        },
        'RESTName': 'addressrange',  # Name to search for the specification (Temporary)
        'defaultValues' :
        {
            'DHCPPoolType' : 'HOST',
            'maxAddress' : '10.30.28.20',
            'minAddress' : '10.30.28.10'
        },
        'spec': {}  # Should be the JSON spec. Empty for now
       }


from monolithe.courgette import Courgette

validator = Courgette(vsdurl='https://135.227.222.112:8443', swagger_path=None, username='csproot', password='csproot', enterprise='csp', apiversion=3.2, data=data)
validator.run()
