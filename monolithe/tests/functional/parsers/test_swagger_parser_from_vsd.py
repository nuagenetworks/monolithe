# -*- coding: utf-8 -*-

from mock import patch

from monolithe.tests.functional import FunctionalTest
from monolithe.tests.functional.utils import MockUtils
from monolithe.lib.parsers import SwaggerParser
from monolithe.lib.utils.printer import Printer


class SwaggerURLParserTests(FunctionalTest):
    """ Tests for SwaggerParser using file option

    """
    def test_run_call_api_docs_entry_point(self):
        """ SwaggerParser call correct /schema/api-docs URI

        """
        parser = SwaggerParser(vsdurl='https://135.227.222.112:8443', path=None, apiversion=3.1)

        mock = MockUtils.create_swagger_response(status_code=400, filepath=None)

        Printer.should_raise_exception(True)

        with patch('requests.get', mock):
            with self.assertRaises(Exception):
                parser.run()

        Printer.should_raise_exception(False)

        url = MockUtils.get_mock_parameter(mock, 'url')

        self.assertEqual(url, u'https://135.227.222.112:8443/web/docs/api/V3_1/schema/api-docs')

    def test_run(self):
        """ SwaggerParser retrieve all entities  """

        parser = SwaggerParser(vsdurl='https://135.227.222.112:8443', path=None, apiversion=3.1)
        resources = parser.run()

        # Verify principal entities
        self.assertIn('Enterprise', resources)
        self.assertIn('Subnet', resources)
        self.assertIn('Alarm', resources)
        self.assertIn('Domain', resources)

        # Verify Enterprise
        # self.assertEqual(resources['Enterprise'], {u'apiVersion': u'V3_1',
        #                                             u'apis': [{u'operations': [{u'method': u'GET',
        #                                                                         u'nickname': u'getEnterprises',
        #                                                                         u'parameters': [{u'name': u'id',
        #                                                                                          u'paramType': u'path',
        #                                                                                          u'required': True,
        #                                                                                          u'type': u'string'}],
        #                                                                         u'responseMessages': [],
        #                                                                         u'summary': u'Create or read all enterprises',
        #                                                                         u'type': u'Enterprise'},
        #                                                                        {u'method': u'POST',
        #                                                                         u'nickname': u'postEnterprises',
        #                                                                         u'parameters': [{u'name': u'id',
        #                                                                                          u'paramType': u'path',
        #                                                                                          u'required': True,
        #                                                                                          u'type': u'string'}],
        #                                                                         u'responseMessages': [],
        #                                                                         u'summary': u'Create or read all enterprises',
        #                                                                         u'type': u'Enterprise'}],
        #                                                        u'path': u'/enterprises'},
        #                                                       {u'operations': [{u'method': u'GET',
        #                                                                         u'nickname': u'getENTERPRISEPROFILESEnterprises',
        #                                                                         u'parameters': [{u'name': u'id',
        #                                                                                          u'paramType': u'path',
        #                                                                                          u'required': True,
        #                                                                                          u'type': u'string'}],
        #                                                                         u'responseMessages': [],
        #                                                                         u'summary': u'Read all Enterprises associated with an enterprise profile - this API can only be accessed by CSPROOT',
        #                                                                         u'type': u'Enterprise'}],
        #                                                        u'path': u'/enterpriseprofiles/{id}/enterprises'},
        #                                                       {u'operations': [{u'method': u'PUT',
        #                                                                         u'nickname': u'putEnterprises',
        #                                                                         u'parameters': [{u'name': u'id',
        #                                                                                          u'paramType': u'path',
        #                                                                                          u'required': True,
        #                                                                                          u'type': u'string'}],
        #                                                                         u'responseMessages': [],
        #                                                                         u'summary': u'Modify an enterprise',
        #                                                                         u'type': u'Enterprise'},
        #                                                                        {u'method': u'DELETE',
        #                                                                         u'nickname': u'deleteEnterprises',
        #                                                                         u'parameters': [{u'name': u'id',
        #                                                                                          u'paramType': u'path',
        #                                                                                          u'required': True,
        #                                                                                          u'type': u'string'}],
        #                                                                         u'responseMessages': [],
        #                                                                         u'summary': u'Delete an enterpris',
        #                                                                         u'type': u'Enterprise'},
        #                                                                        {u'method': u'GET',
        #                                                                         u'nickname': u'getEnterprises',
        #                                                                         u'parameters': [{u'name': u'id',
        #                                                                                          u'paramType': u'path',
        #                                                                                          u'required': True,
        #                                                                                          u'type': u'string'}],
        #                                                                         u'responseMessages': [],
        #                                                                         u'summary': u'Read an enterprise',
        #                                                                         u'type': u'Enterprise'}],
        #                                                        u'path': u'/enterprises/{id}'}],
        #                                             u'basePath': u'/',
        #                                             u'models': {u'Enterprise': {u'description': u'Definition of the enterprise object. This is the top level object that represents an enterprise or organization.',
        #                                                                         u'id': u'Enterprise',
        #                                                                         u'properties': {u'DHCPLeaseInterval': {u'description': u'DHCP Lease Interval (in hrs) to be used by an enterprise.',
        #                                                                                                                u'required': u'false',
        #                                                                                                                u'type': u'integer',
        #                                                                                                                u'uniqueItems': False},
        #                                                                                         u'ID': {u'description': u'This is a unique ID for the object (UUID) that is auto-populated by the VSD and it is used in both the http URI or other objects to refer to the particular object.',
        #                                                                                                 u'required': u'false',
        #                                                                                                 u'type': u'string',
        #                                                                                                 u'uniqueItems': False},
        #                                                                                         u'allowAdvancedQOSConfiguration': {u'description': u'Controls whether this enterprise has access to advanced QoS settings',
        #                                                                                                                            u'required': u'false',
        #                                                                                                                            u'type': u'boolean',
        #                                                                                                                            u'uniqueItems': False},
        #                                                                                         u'allowGatewayManagement': {u'description': u'This flag indicates if the enterprise/organization can manage gateways. If yes then it can create gateway templates, instantiate them etc.',
        #                                                                                                                     u'required': u'false',
        #                                                                                                                     u'type': u'boolean',
        #                                                                                                                     u'uniqueItems': False},
        #                                                                                         u'allowTrustedForwardingClass': {u'description': u'Controls whether QoS policies and templates created under this enterprise set the trusted flag to true',
        #                                                                                                                          u'required': u'false',
        #                                                                                                                          u'type': u'boolean',
        #                                                                                                                          u'uniqueItems': False},
        #                                                                                         u'allowedForwardingClasses': {u'description': u'Allowed Forwarding Classes for this enterprise. Possible values are NONE, A, B, C, D, E, F, G, H, .',
        #                                                                                                                       u'enum': [u'D',
        #                                                                                                                                 u'E',
        #                                                                                                                                 u'F',
        #                                                                                                                                 u'G',
        #                                                                                                                                 u'A',
        #                                                                                                                                 u'B',
        #                                                                                                                                 u'C',
        #                                                                                                                                 u'H',
        #                                                                                                                                 u'NONE'],
        #                                                                                                                       u'required': u'false',
        #                                                                                                                       u'type': u'enum',
        #                                                                                                                       u'uniqueItems': False},
        #                                                                                         u'associatedEnterpriseSecurityId': {u'description': u'Readonly Id of the associated group key encryption profile',
        #                                                                                                                             u'required': u'false',
        #                                                                                                                             u'type': u'string',
        #                                                                                                                             u'uniqueItems': False},
        #                                                                                         u'associatedGroupKeyEncryptionProfileId': {u'description': u'Readonly Id of the associated group key encryption profile',
        #                                                                                                                                    u'required': u'false',
        #                                                                                                                                    u'type': u'string',
        #                                                                                                                                    u'uniqueItems': False},
        #                                                                                         u'associatedKeyServerMonitorId': {u'description': u'Readonly Id of the associated keyserver monitor',
        #                                                                                                                           u'required': u'false',
        #                                                                                                                           u'type': u'string',
        #                                                                                                                           u'uniqueItems': False},
        #                                                                                         u'avatarData': {u'description': u'URL to the avatar data associated with the enterprise. If the avatarType is URL then value of avatarData should an URL of the image. If the avatarType BASE64 then avatarData should be BASE64 encoded value of the image',
        #                                                                                                         u'required': u'false',
        #                                                                                                         u'type': u'string',
        #                                                                                                         u'uniqueItems': False},
        #                                                                                         u'avatarType': {u'description': u'Avatar type - URL or BASE64 Possible values are URL, BASE64, COMPUTEDURL, .',
        #                                                                                                         u'enum': [u'COMPUTEDURL',
        #                                                                                                                   u'BASE64',
        #                                                                                                                   u'URL'],
        #                                                                                                         u'required': u'false',
        #                                                                                                         u'type': u'enum',
        #                                                                                                         u'uniqueItems': False},
        #                                                                                         u'creationDate': {u'description': u'Holds the time that this object was created.',
        #                                                                                                           u'required': u'false',
        #                                                                                                           u'type': u'date',
        #                                                                                                           u'uniqueItems': False},
        #                                                                                         u'customerID': {u'description': u'CustomerID that is used by VSC to identify this enterprise. This is a read only attribute.',
        #                                                                                                         u'required': u'false',
        #                                                                                                         u'type': u'long',
        #                                                                                                         u'uniqueItems': False},
        #                                                                                         u'description': {u'description': u'A description of the enterprise',
        #                                                                                                          u'required': u'false',
        #                                                                                                          u'type': u'string',
        #                                                                                                          u'uniqueItems': False},
        #                                                                                         u'encryptionManagementMode': {u'description': u'encryption management mode for this enterprise Possible values are DISABLED, MANAGED, .',
        #                                                                                                                       u'enum': [u'DISABLED',
        #                                                                                                                                 u'MANAGED'],
        #                                                                                                                       u'required': u'false',
        #                                                                                                                       u'type': u'enum',
        #                                                                                                                       u'uniqueItems': False},
        #                                                                                         u'enterpriseProfileID': {u'description': u'Enterprise profile id for this enterprise',
        #                                                                                                                  u'required': u'false',
        #                                                                                                                  u'type': u'string',
        #                                                                                                                  u'uniqueItems': False},
        #                                                                                         u'externalID': {u'description': u'This attribute is set when an external management system is managing this object. When set, the VSD will issue a warning if the user tries to modify this object directly through the UI or the API. For example, if VMware vCloud or Openstack create a network, then this network cannot be deleted directly by a user without requiring extra confirmation. This allows integrations to separate between managed objects by external entities and directly managed objects.',
        #                                                                                                         u'required': u'false',
        #                                                                                                         u'type': u'string',
        #                                                                                                         u'uniqueItems': False},
        #                                                                                         u'floatingIPsQuota': {u'description': u'Quota set for the number of floating IPs to be used by an enterprise.',
        #                                                                                                               u'required': u'false',
        #                                                                                                               u'type': u'int',
        #                                                                                                               u'uniqueItems': False},
        #                                                                                         u'floatingIPsUsed': {u'description': u'Number of floating IPs used by the enterprise from the assigned floatingIPsQuota',
        #                                                                                                              u'required': u'false',
        #                                                                                                              u'type': u'int',
        #                                                                                                              u'uniqueItems': False},
        #                                                                                         u'lastUpdatedBy': {u'description': u'Identifies the user that last modified this object.',
        #                                                                                                            u'required': u'false',
        #                                                                                                            u'type': u'string',
        #                                                                                                            u'uniqueItems': False},
        #                                                                                         u'lastUpdatedDate': {u'description': u'Determines the time that this object was last updated.',
        #                                                                                                              u'required': u'false',
        #                                                                                                              u'type': u'date',
        #                                                                                                              u'uniqueItems': False},
        #                                                                                         u'name': {u'description': u'The unique name of the enterprise. Valid characters are alphabets, numbers, space and hyphen( - ).',
        #                                                                                                   u'required': u'true',
        #                                                                                                   u'type': u'string',
        #                                                                                                   u'uniqueItems': False},
        #                                                                                         u'owner': {u'description': u'Identifies the user that has created this object.',
        #                                                                                                    u'required': u'false',
        #                                                                                                    u'type': u'string',
        #                                                                                                    u'uniqueItems': False},
        #                                                                                         u'parentID': {u'description': u'This is the ID of the parent object.',
        #                                                                                                       u'required': u'false',
        #                                                                                                       u'type': u'string',
        #                                                                                                       u'uniqueItems': False},
        #                                                                                         u'parentType': {u'description': u'This is the type of parent object for the particular object.',
        #                                                                                                         u'required': u'false',
        #                                                                                                         u'type': u'string',
        #                                                                                                         u'uniqueItems': False},
        #                                                                                         u'receiveMultiCastListId': {u'description': u'Readonly Id of the auto generated receive multicast list associated with this enterprise profile',
        #                                                                                                                     u'required': u'false',
        #                                                                                                                     u'type': u'string',
        #                                                                                                                     u'uniqueItems': False},
        #                                                                                         u'sendMultiCastListId': {u'description': u'Readonly Id of the auto generated send multicast list associated with this enterprise profile',
        #                                                                                                                  u'required': u'false',
        #                                                                                                                  u'type': u'string',
        #                                                                                                                  u'uniqueItems': False}}}},
        #                                             'package': u'/usermgmt',
        #                                             u'resourcePath': u'/Enterprise',
        #                                             u'swaggerVersion': u'1.2'})
