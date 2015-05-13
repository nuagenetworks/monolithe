vsd_options = {
    'vsdurl': 'https://135.227.222.112:8443',
    'username': 'csproot',
    'password': 'csproot',
    'enterprise': 'csp',
    'version': 3.2
}

datas = [
        {'parentObject' : {
            'resourceName': 'enterprises',
            'id': '1d30671a-818d-45cf-8db3-9d49d7f555bc'
         },
         'resourceName': 'DomainTemplate', # Name to search for the specification (Temporary)
         'defaultValues' : {
             'name': 'A domain template',
             'description': 'Description of the DT',
             'multicast': 'ENABLED',
             'encryption': 'ENABLED',
             'policyChangeStatus': 'APPLIED',
             'associatedMulticastChannelMapID': '7417415f-7c2a-4288-8284-fd9e5594ae82' # Created in the VSD
             },
         'spec': {} # Should be the JSON spec. Empty for now
        }
    ]

from monolithe import Command
Command.run_tests(vsdurl='https://135.227.222.112:8443', username='csproot', password='csproot', enterprise='csp', version=3.2, datas=datas)
