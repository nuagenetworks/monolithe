# -*- coding: utf-8 -*-

from monolithe.tests.functional import FunctionalTest
from monolithe.lib.parsers import SwaggerParser
from monolithe.lib.transformers import SwaggerTransformer, SpecificationTransformer


class SpecificationTransformerTests(FunctionalTest):
    """ Tests for SwaggerParser using file option

    """
    @classmethod
    def setUpClass(cls):
        """ Set up context

        """
        parser = SwaggerParser(path=cls.get_valid_path(), vsdurl=None, apiversion=None)
        swagger_resources = parser.run()

        cls.specifications = SwaggerTransformer.get_specifications(resources=swagger_resources)

    def test_transformer_returns_all_objects_rest_names(self):
        """ SpecificationTransformer returns all objects with correct rest names

        """
        objects = SpecificationTransformer.get_objects(self.specifications)

        self.assertEqual(len(objects), 99)
        self.assertEqual(objects.keys(), [u'addressrange',
                                          u'alarm',
                                          u'app',
                                          u'application',
                                          u'applicationservice',
                                          u'autodiscoveredgateway',
                                          u'bgppeer',
                                          u'bootstrap',
                                          u'bootstrapactivation',
                                          u'bridgeinterface',
                                          u'component',
                                          u'dhcpoption',
                                          u'domain',
                                          u'domaintemplate',
                                          u'dscpforwardingclassmapping',
                                          u'dscpforwardingclasstable',
                                          u'egressaclentrytemplate',
                                          u'egressacltemplate',
                                          u'egressqospolicy',
                                          u'enterprise',
                                          u'enterprisenetwork',
                                          u'enterprisepermission',
                                          u'enterpriseprofile',
                                          u'eventlog',
                                          u'floatingip',
                                          u'flow',
                                          u'flowforwardingpolicy',
                                          u'flowsecuritypolicy',
                                          u'gateway',
                                          u'gatewaytemplate',
                                          u'globalmetadata',
                                          u'group',
                                          u'hostinterface',
                                          u'hsc',
                                          u'infraconfig',
                                          u'infrastructuregatewayprofile',
                                          u'infrastructureportprofile',
                                          u'ingressaclentrytemplate',
                                          u'ingressacltemplate',
                                          u'ingressadvfwdentrytemplate',
                                          u'ingressadvfwdtemplate',
                                          u'ipreservation',
                                          u'job',
                                          u'l2domain',
                                          u'l2domaintemplate',
                                          u'ldapconfiguration',
                                          u'license',
                                          u'location',
                                          u'me',
                                          u'metadata',
                                          u'mirrordestination',
                                          u'monitoringport',
                                          u'multicastchannelmap',
                                          u'multicastrange',
                                          u'multinicvport',
                                          u'natmapentry',
                                          u'networklayout',
                                          u'nsgateway',
                                          u'nsgatewaytemplate',
                                          u'patnatpool',
                                          u'permission',
                                          u'policydecision',
                                          u'policygroup',
                                          u'policygrouptemplate',
                                          u'port',
                                          u'porttemplate',
                                          u'publicnetwork',
                                          u'qos',
                                          u'ratelimiter',
                                          u'redirectiontarget',
                                          u'redirectiontargettemplate',
                                          u'redundancygroup',
                                          u'resync',
                                          u'service',
                                          u'sharednetworkresource',
                                          u'staticroute',
                                          u'statistics',
                                          u'statisticscollector',
                                          u'statisticspolicy',
                                          u'subnet',
                                          u'subnettemplate',
                                          u'systemconfig',
                                          u'tca',
                                          u'tier',
                                          u'user',
                                          u'virtualip',
                                          u'vlan',
                                          u'vlantemplate',
                                          u'vm',
                                          u'vminterface',
                                          u'vpnconnection',
                                          u'vport',
                                          u'vportmirror',
                                          u'vrs',
                                          u'vsc',
                                          u'vsd',
                                          u'vsp',
                                          u'zone',
                                          u'zonetemplate'])

    def test_transformer_returns_valid_rest_user(self):
        """ SpecificationTransformer returns all objects with correct rest names

        """
        objects = SpecificationTransformer.get_objects(self.specifications)

        rest_user = objects['me']

        self.assertEqual(rest_user.name, 'RESTUser')
        self.assertEqual(rest_user.remote_name, 'me')
        self.assertEqual(rest_user.plural_name, u'RESTUsers')
