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
            'id': '15de101d-1bfd-4365-b2e5-c4326eaafebd'
        },
        'RESTName': 'addressrange',  # Name to search for the specification (Temporary)
        'defaultValues' :
        {
            'DHCPPoolType' : 'HOST',
            'maxAddress' : '10.83.101.20',
            'minAddress' : '10.83.101.10'
        },
        'spec': {}  # Should be the JSON spec. Empty for now
       }


from monolithe.validators import APIValidator

validator = APIValidator(vsdurl='https://135.227.222.112:8443', swagger_path=None, username='csproot', password='csproot', enterprise='csp', apiversion=3.2, data=data)
validator.run()
