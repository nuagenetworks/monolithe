First example
=============

Connection
----------

Let's import vsdk, and configure logging so that we can visualize the rest calls.

>>> import vsdk, logging
>>> log = logging.getLogger('bambou')
>>> log.addHandler(logging.StreamHandler())
>>> log.setLevel(logging.DEBUG)

Now we can start a session as `csproot` :

>>> session = NUVSDSession(username=u'csproot', password=u'csproot', enterprise=u'csp', api_url=u'https://135.227.150.222:8443/nuage/api/v3_2')
>>> session.start()
Bambou Sending >>>>>>
GET https://135.227.150.222:8443/nuage/api/v3_2/me with following data:
null
Bambou has been sent with user:csproot within enterprise:csp (Key=None)
Bambou <<<<< Response for
GET https://135.227.150.222:8443/nuage/api/v3_2/me
[
    {
        "userName": "csproot", 
        "mobileNumber": null, 
        "APIKey": "92790b4b-85e0-4f40-9835-2aa242f24a57", 
        "firstName": "csproot", 
        "APIKeyExpiry": 1424195980554, 
        "lastName": "csproot", 
        "enterpriseID": "76046673-d0ea-4a67-b6af-2829952f0812", 
        "ID": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
        "avatarType": null, 
        "enterpriseName": "CSP", 
        "role": "CSPROOT", 
        "avatarData": null, 
        "externalId": null, 
        "password": null, 
        "email": "csproot@CSP.com", 
        "externalID": null
    }
]

The session instance now have its :attr:`vsdk.NUVSDSession.user` attribute populated. Every object has a `to_dict()` method that allows to easily visualize an object and it's API attributes :

>>> session.user.to_dict()
{'APIKey': u'92790b4b-85e0-4f40-9835-2aa242f24a57',
 u'ID': u'8a6f0e20-a4db-4878-ad84-9cc61756cd5e',
 u'avatarData': None,
 u'avatarType': None,
 u'creationDate': None,
 u'email': u'csproot@CSP.com',
 u'enterpriseID': u'76046673-d0ea-4a67-b6af-2829952f0812',
 u'enterpriseName': u'CSP',
 u'firstName': u'csproot',
 u'lastName': u'csproot',
 u'lastUpdatedBy': None,
 u'lastUpdatedDate': None,
 u'mobileNumber': None,
 u'owner': None,
 u'parentID': None,
 u'parentType': None,
 u'password': None,
 u'role': u'CSPROOT',
 u'userName': u'csproot'}

CRUD operations
---------------

The VSD follows a tree structure : a given object can have one or multiple
children. For instance, an enterprise contains domains and L2 domains, domains
contains zones, etc. For the reason we will often to the `current object`, its
`parent object`, and its `children`.

Every classes have generics methods to perform CRUD operations relatively to the current object :
  * `add_child_objet()` creates a child object on the VSD
  * `fetch()` read the current object on the VSD. 
  * `save()` updates the current object on the VSD
  * `delete()` deletes the current object on the VSD
Every method performing ReST calls return a tuple of objects : the object that
has been created/updated/deleted, and a connection object that contains
informations about the ReST call (status code, potential error message, etc.)

To illustrate, let's create, update an delete an enteprise. The VSDK consider
that the root of the VSD hierarchy is the current user. Thus, an enterprise is
a child object of the current user.

First we instantiate an NUEnterprise object (the name is the only mandatoyy option)

>>> my_enterprise = vsdk.NUEnterprise(name='FooBar')

Create it on the VSD. The method will return an enterprise object and a connection, but we won't need them here.

>>> session.user.add_child_object(my_enterprise)
Bambou Sending >>>>>>
POST https://135.227.150.222:8443/nuage/api/v3_2/enterprises with following data:
{
    "allowedForwardingClasses": null, 
    "allowGatewayManagement": null, 
    "description": null, 
    "name": "foobar", 
    "DHCPLeaseInterval": null, 
    "avatarData": null, 
    "floatingIPsQuota": null, 
    "owner": null, 
    "ID": null, 
    "avatarType": null, 
    "parentType": null, 
    "lastUpdatedBy": null, 
    "enterpriseProfileID": null, 
    "lastUpdatedDate": null, 
    "parentID": null, 
    "allowTrustedForwardingClass": null, 
    "creationDate": null, 
    "floatingIPsUsed": null, 
    "customerID": null, 
    "allowAdvancedQOSConfiguration": null
}
Bambou has been sent with user:csproot within enterprise:csp (Key=92790b4b-85e0-4f40-9835-2aa242f24a57)
Bambou <<<<< Response for
POST https://135.227.150.222:8443/nuage/api/v3_2/enterprises
[
    {
        "allowGatewayManagement": true, 
        "DHCPLeaseInterval": 24, 
        "floatingIPsQuota": 50, 
        "externalID": null, 
        "parentID": null, 
        "owner": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
        "children": null, 
        "customerID": 10005, 
        "description": null, 
        "avatarType": null, 
        "parentType": null, 
        "lastUpdatedBy": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
        "creationDate": 1424130453100, 
        "allowTrustedForwardingClass": true, 
        "ID": "17afb19a-9cbc-4cd5-a03c-33660dfec10b", 
        "name": "foobar", 
        "avatarData": null, 
        "lastUpdatedDate": 1424130453100, 
        "enterpriseProfileID": "f1e5eb19-c67a-4651-90c1-3f84e23e1d36", 
        "allowedForwardingClasses": [
            "A", 
            "B", 
            "C", 
            "D", 
            "E", 
            "F", 
            "G", 
            "H"
        ], 
        "floatingIPsUsed": 0, 
        "allowAdvancedQOSConfiguration": true
    }
]
(<vsdk.nuenterprise.NUEnterprise at 0x7f1e30b878d0>,
 <bambou.nurest_connection.NURESTConnection at 0x7f1e30b955d0>)

We can see that `my_enterprise` has been updated :

>>> my_enterprise.to_dict() 
{u'DHCPLeaseInterval': 24,
 u'ID': u'17afb19a-9cbc-4cd5-a03c-33660dfec10b',
 u'allowAdvancedQOSConfiguration': True,
 u'allowGatewayManagement': True,
 u'allowTrustedForwardingClass': True,
 u'allowedForwardingClasses': [u'A', u'B', u'C', u'D', u'E', u'F', u'G', u'H'],
 u'avatarData': None,
 u'avatarType': None,
 u'creationDate': 1424130453100,
 u'customerID': 10005,
 u'description': None,
 u'enterpriseProfileID': u'f1e5eb19-c67a-4651-90c1-3f84e23e1d36',
 u'floatingIPsQuota': 50,
 u'floatingIPsUsed': 0,
 u'lastUpdatedBy': u'8a6f0e20-a4db-4878-ad84-9cc61756cd5e',
 u'lastUpdatedDate': 1424130453100,
 u'name': u'foobar',
 u'owner': u'8a6f0e20-a4db-4878-ad84-9cc61756cd5e',
 u'parentID': None,
 u'parentType': None}


Let's update it by changing the `name` attribute :

>>> my_enterprise.name = 'Barfoo'
>>> my_enterprise.save()
Bambou Sending >>>>>>
PUT https://135.227.150.222:8443/nuage/api/v3_2/enterprises/17afb19a-9cbc-4cd5-a03c-33660dfec10b with following data:
{
    "allowedForwardingClasses": [
        "A", 
        "B", 
        "C", 
        "D", 
        "E", 
        "F", 
        "G", 
        "H"
    ], 
    "allowGatewayManagement": true, 
    "description": null, 
    "name": "Barfoo", 
    "DHCPLeaseInterval": 24, 
    "avatarData": null, 
    "floatingIPsQuota": 50, 
    "owner": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
    "ID": "17afb19a-9cbc-4cd5-a03c-33660dfec10b", 
    "avatarType": null, 
    "parentType": null, 
    "lastUpdatedBy": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
    "enterpriseProfileID": "f1e5eb19-c67a-4651-90c1-3f84e23e1d36", 
    "lastUpdatedDate": 1424130453100, 
    "parentID": null, 
    "allowTrustedForwardingClass": true, 
    "creationDate": 1424130453100, 
    "floatingIPsUsed": 0, 
    "customerID": 10005, 
    "allowAdvancedQOSConfiguration": true
}
Bambou has been sent with user:csproot within enterprise:csp (Key=92790b4b-85e0-4f40-9835-2aa242f24a57)
Bambou <<<<< Response for
PUT https://135.227.150.222:8443/nuage/api/v3_2/enterprises/17afb19a-9cbc-4cd5-a03c-33660dfec10b
null
Out[29]: 
(<vsdk.nuenterprise.NUEnterprise at 0x7f1e30b878d0>,
 <bambou.nurest_connection.NURESTConnection at 0x7f1e30c004d0>)

If someone else made changes on this object, we can read it again :

>>> my_enterprise.fetch()
Bambou Sending >>>>>>
GET https://135.227.150.222:8443/nuage/api/v3_2/enterprises/17afb19a-9cbc-4cd5-a03c-33660dfec10b with following data:
null
Bambou has been sent with user:csproot within enterprise:csp (Key=92790b4b-85e0-4f40-9835-2aa242f24a57)
Bambou <<<<< Response for
GET https://135.227.150.222:8443/nuage/api/v3_2/enterprises/17afb19a-9cbc-4cd5-a03c-33660dfec10b
[
    {
        "allowGatewayManagement": true, 
        "DHCPLeaseInterval": 24, 
        "floatingIPsQuota": 50, 
        "externalID": null, 
        "parentID": null, 
        "owner": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
        "children": null, 
        "customerID": 10005, 
        "description": null, 
        "avatarType": null, 
        "parentType": null, 
        "lastUpdatedBy": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
        "creationDate": 1424130453000, 
        "allowTrustedForwardingClass": true, 
        "ID": "17afb19a-9cbc-4cd5-a03c-33660dfec10b", 
        "name": "BarBaz", 
        "avatarData": null, 
        "lastUpdatedDate": 1424131572000, 
        "enterpriseProfileID": "f1e5eb19-c67a-4651-90c1-3f84e23e1d36", 
        "allowedForwardingClasses": [
            "A", 
            "B", 
            "C", 
            "D", 
            "E", 
            "F", 
            "G", 
            "H"
        ], 
        "floatingIPsUsed": 0, 
        "allowAdvancedQOSConfiguration": true
    }
]
Out[31]: 
(<vsdk.nuenterprise.NUEnterprise at 0x7f1e30b878d0>,
 <bambou.nurest_connection.NURESTConnection at 0x7f1e30c00ed0>)

Finally let's delete it :

>>> my_enterprise.delete()
Bambou Sending >>>>>>
DELETE https://135.227.150.222:8443/nuage/api/v3_2/enterprises/17afb19a-9cbc-4cd5-a03c-33660dfec10b with following data:
{
    "allowedForwardingClasses": [
        "A", 
        "B", 
        "C", 
        "D", 
        "E", 
        "F", 
        "G", 
        "H"
    ], 
    "allowGatewayManagement": true, 
    "description": null, 
    "name": "BarBaz", 
    "DHCPLeaseInterval": 24, 
    "avatarData": null, 
    "floatingIPsQuota": 50, 
    "owner": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
    "ID": "17afb19a-9cbc-4cd5-a03c-33660dfec10b", 
    "avatarType": null, 
    "parentType": null, 
    "lastUpdatedBy": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
    "enterpriseProfileID": "f1e5eb19-c67a-4651-90c1-3f84e23e1d36", 
    "lastUpdatedDate": 1424131785000, 
    "parentID": null, 
    "allowTrustedForwardingClass": true, 
    "creationDate": 1424130453000, 
    "floatingIPsUsed": 0, 
    "customerID": 10005, 
    "allowAdvancedQOSConfiguration": true
}
Bambou has been sent with user:csproot within enterprise:csp (Key=92790b4b-85e0-4f40-9835-2aa242f24a57)
Bambou <<<<< Response for
DELETE https://135.227.150.222:8443/nuage/api/v3_2/enterprises/17afb19a-9cbc-4cd5-a03c-33660dfec10b
{
    "errors": [
        {
            "property": "", 
            "descriptions": [
                {
                    "description": "Once an enterprise is deleted, it cannot be recovered. Are you sure you want to delete enterprise 'Barfoo'?",
                    "title": "Delete enterprise"
                }
            ]
        }
    ], 
    "choices": [
        {
            "id": 1, 
            "label": "OK"
        }, 
        {
            "id": 0, 
            "label": "Cancel"
        }
    ]
}
Out[49]: 
(<vsdk.nuenterprise.NUEnterprise at 0x7f1e30b878d0>,
 <bambou.nurest_connection.NURESTConnection at 0x7f1e30c1cfd0>)

The logs show that deletion failed because VSD asks for a confirmation. The `delete()` method has a `response_choice` optionnal argument to handle such cases :

>>> my_enterprise.delete(response_choice=1) 
Bambou Sending >>>>>>
DELETE https://135.227.150.222:8443/nuage/api/v3_2/enterprises/17afb19a-9cbc-4cd5-a03c-33660dfec10b?responseChoice=1 with following data:
{
    "allowedForwardingClasses": [
        "A", 
        "B", 
        "C", 
        "D", 
        "E", 
        "F", 
        "G", 
        "H"
    ], 
    "allowGatewayManagement": true, 
    "description": null, 
    "name": "BarBaz", 
    "DHCPLeaseInterval": 24, 
    "avatarData": null, 
    "floatingIPsQuota": 50, 
    "owner": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
    "ID": "17afb19a-9cbc-4cd5-a03c-33660dfec10b", 
    "avatarType": null, 
    "parentType": null, 
    "lastUpdatedBy": "8a6f0e20-a4db-4878-ad84-9cc61756cd5e", 
    "enterpriseProfileID": "f1e5eb19-c67a-4651-90c1-3f84e23e1d36", 
    "lastUpdatedDate": 1424131785000, 
    "parentID": null, 
    "allowTrustedForwardingClass": true, 
    "creationDate": 1424130453000, 
    "floatingIPsUsed": 0, 
    "customerID": 10005, 
    "allowAdvancedQOSConfiguration": true
}
Bambou has been sent with user:csproot within enterprise:csp (Key=92790b4b-85e0-4f40-9835-2aa242f24a57)
Bambou <<<<< Response for
DELETE https://135.227.150.222:8443/nuage/api/v3_2/enterprises/17afb19a-9cbc-4cd5-a03c-33660dfec10b?responseChoice=1
null
Out[56]: 
(<vsdk.nuenterprise.NUEnterprise at 0x7f1e30b878d0>,
 <bambou.nurest_connection.NURESTConnection at 0x7f1e30c1cd90>)
