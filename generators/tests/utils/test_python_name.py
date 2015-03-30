# -*- coding: utf-8 -*-

from unittest import TestCase
from generators.lib import Utils


class GetPythonNameTest(TestCase):
    """ Test for get_python_name function

    """
    def assertPythonNameEquals(self, remote_name, python_name):
        """ Check that the remote name is well converted to
            the python name

        """
        self.assertEqual(Utils.get_python_name(remote_name), python_name)

    def test_get_python_name(self):
        """ Convert REST names to Python

        """
        self.assertPythonNameEquals('enterpriseID', 'enterprise_id')
        self.assertPythonNameEquals('permittedEntityType', 'permitted_entity_type')
        self.assertPythonNameEquals('L2Domain', 'l2_domain')
        self.assertPythonNameEquals('L2DomainTemplate', 'l2_domain_template')
        self.assertPythonNameEquals('UUID', 'uuid')
        self.assertPythonNameEquals('VM', 'vm')
        self.assertPythonNameEquals('VMs', 'vms')
        self.assertPythonNameEquals('VPort', 'vport')
        self.assertPythonNameEquals('VPortTag', 'vport_tag')
        self.assertPythonNameEquals('PATEnabled', 'pat_enabled')
        self.assertPythonNameEquals('DHCPServerAddress', 'dhcp_server_address')
        self.assertPythonNameEquals('VMsInterfaces', 'vms_interfaces')
        self.assertPythonNameEquals('zoneIds', 'zone_ids')
        self.assertPythonNameEquals('domainIDs', 'domain_ids')
        self.assertPythonNameEquals('VPortsTag', 'vports_tag')
        self.assertPythonNameEquals('VPortsTagOptionL2Domain', 'vports_tag_option_l2_domain')
        self.assertPythonNameEquals('IDsTORemove', 'ids_to_remove')
        self.assertPythonNameEquals('MultiNICVPortsFetcher', 'multi_nic_vports_fetcher')
        self.assertPythonNameEquals('FloatingIPID', 'floating_ip_id')