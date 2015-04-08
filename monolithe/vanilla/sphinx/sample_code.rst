Code Snippets
=============

This section provides various code snippets and scripts you can use or get inspiration from to develop your own scripts or application using the `vsdk`.


Enterprise Onboarding
---------------------

.. code-block:: python
    :linenos:

    # TODO :(


Generic Network Provisioning
----------------------------

This sample function will populate a given domain with a given number of zones, subnets and vports.

.. code-block:: python
    :linenos:

    from vspk.vsdk import v3_2 as vsdk
    import ipaddress

    def populate_test_domain(domain, number_of_zones, number_of_subnets_per_zone, number_of_vports_per_subnet):
        """ Populate a domain with test data

            Args:
                domain (vsdk.NUDomain | vsdk.NUDomainTemplate): base domain to populate
                number_of_zones (int): number of desired zones
                number_of_subnets_per_zone (int): number of desired subnets per zone
                number_of_vports_per_subnet (int): number of desired vports per subnet (only available if domain is not a template)
        """

        # check if the domain is a template
        # if so use children template classes instead of instances
        is_template = domain.is_template()
        zone_class = vsdk.NUZoneTemplate if is_template else vsdk.NUZone
        subnet_class = vsdk.NUSubnetTemplate if is_template else vsdk.NUSubnet

        # generate a network and subnets
        network = ipaddress.ip_network(u'10.0.0.0/8')
        subnets = network.subnets(new_prefix=24)

        # create zones
        for i in range(0, number_of_zones):

            zone = zone_class(name="Zone %d" % i)
            domain.create_child(zone)
            domain.add_child(zone)

            #creates subnets
            for j in range(0, number_of_subnets_per_zone):

                # pull a subnet and get information about it
                subnetwork = subnets.next()
                ip = "%s" % subnetwork.network_address
                gw = "%s" % subnetwork.hosts().next()
                nm = "%s" % subnetwork.netmask

                subnet = subnet_class(name="Subnet %d %d" % (i, j), address=ip, netmask=nm, gateway=gw)
                zone.create_child(subnet)
                zone.add_child(subnet)

                # if the given domain is a template, we stop
                if is_template:
                    break

                # Otherwise we create the VPorts
                for k in range(0, number_of_vports_per_subnet):

                    vport = vsdk.NUVPort(name="VPort %d-%d-%d" % (i, j, k), type="VM", address_spoofing="INHERITED", multicast="INHERITED")
                    subnet.create_child(vport)
                    subnet.add_child(vport)


    if __name__ == "__main__":

        session = vsdk.NUVSDSession(username=LOGIN_USER, password=LOGIN_PASS, enterprise=LOGIN_ENTERPRISE, api_url=LOGIN_API_URL, version=LOGIN_API_VERSION)
        session.start()

        # get a domain
        domain = vsdk.NUDomain(id="x")
        domain.fetch()

        # do the job
        populate_test_domain(domain, 3, 4, 5)


Gateway Provisioning
--------------------

This sample function will create a gateway with ports, vlan and give some permissions to an enterprise

.. code-block:: python
    :linenos:

    from vspk.vsdk import v3_2 as vsdk

    def create_datacenter_gateway_template(name, personality, network_port_names, access_port_names, vlan_range, vlans_values, vsdsession, description=None):
        """ Creates a DC Gateway template

            Args:
                name (string): the name of the gateway template
                personality (string): the personality of the gateway template
                description (string): the description of the gateway template
                network_port_names (list): list of string representing the physical names of the network ports to create
                access_port_names (list): list of string representing the physical names of the access ports to create
                vlan_range (string): the default VLAN range for the access ports
                vlans_values (list): list of int representing the value of the VLAN to create in each access port
                vsdsession (vsdk.NUVSDSession): the VSD session to use

            Returns:
                vsdk.NUGatewayTemplate: the newly created gateway template.
        """

        # create the gateway template
        gateway_template = vsdk.NUGatewayTemplate(name=name, personality=personality, description=description)

        vsdsession.user.create_child(gateway_template)

        # create a network port for each given network_port_names
        for network_port_name in network_port_names:

            network_port_template = vsdk.NUPortTemplate(name=network_port_name, physical_name=network_port_name, port_type="NETWORK")
            gateway_template.create_child(network_port_template)


        # create an access port for each given access_port_names
        for access_port_name in access_port_names:

            access_port_template = vsdk.NUPortTemplate(name=access_port_name, physical_name=access_port_name, port_type="ACCESS", vlan_range=vlan_range)
            gateway_template.create_child(access_port_template)

            # create a VLAN for each given vlans_values
            for vlan_value in vlans_values:

                vlan = vsdk.NUVLANTemplate(value=vlan_value)
                access_port_template.create_child(vlan)

        return gateway_template


    def create_datacenter_gateway(name, system_id, gateway_template, enterprise, vsdsession, permission="USE"):
        """ Creates a gateway instance from a gateway template, and gives given permission to given enterprise

            Args:
                name (string): the gateway name
                gateway_template (vsdk.NUGatewayTemplate): the gateway template to use
                enterprise (vsdk.NUEnterprise): the enterprise to give permission to
                permission (string): the permission to give (default: "USE")
                vsdsession (vsdk.NUVSDSession): the VSD session to use

            Returns:
                vsdk.NUGateway: the newly created gateway.
        """

        gateway = vsdk.NUGateway(name=name, system_id=system_id)
        vsdsession.user.instantiate_child(gateway, gateway_template)
        permission = vsdk.NUEnterprisePermission(permitted_action=permission, permitted_entity_id=enterprise.id)
        gateway.create_child(permission)

        return gateway

    if __name__ == "__main__":

        # start the session
        session = vsdk.NUVSDSession(username=LOGIN_USER, password=LOGIN_PASS, enterprise=LOGIN_ENTERPRISE, api_url=LOGIN_API_URL, version=LOGIN_API_VERSION)
        session.start()

        # get an enterprise
        enterprise = session.user.enterprises.get_first(filter="name == 'Triple A'")

        # create a gateway template
        gw_tmpl = create_datacenter_gateway_template("my template", "VRSG", ["port0"], ["port1", "port2"], "0-400", [100, 200], session)

        # instantiate a gateway from the template and give USE permission to enterprise
        gw = create_datacenter_gateway("gateway 1", "id1", gw_tmpl, enterprise, session)


Populating a test environment
-----------------------------

.. code-block:: python
    :linenos:

    # TODO :(



Automatic Virtual Machine Provisioning
--------------------------------------

.. code-block:: python
    :linenos:

    # TODO :(



Populating Well-Known IANA Application Services
-----------------------------------------------

This function will fetch the latest known application services from IANA and create them as application services

.. code-block:: python
    :linenos:

    import requests
    import csv
    from vspk.vsdk import v3_2 as vsdk

    def import_known_application_services(session):

        # pip install requests

        protocols = requests.get('http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv').content
        csvreader = csv.reader(protocols.split('\r\n'))

        for row in csvreader:

            try:
                port_number = row[1]
                proto = "6" if row[2] is "tcp" else "17"
                desc = row[3]
                name = "%s - %s - %s " % (proto, port_number, row[0])

                if not name:
                    continue;

                appservice = vsdk.NUApplicationService(name=name, protocol=proto, destination_port=port_number, description=desc, direction="REFLEXIVE",\
                                                       ether_type="0x0800", source_port="*", dscp="*")

                session.user.create_child(appservice)

            except Exception as ex:
                print ex;


    if __name__ == "__main__":

        session = vsdk.NUVSDSession(username=LOGIN_USER, password=LOGIN_PASS, enterprise=LOGIN_ENTERPRISE, api_url=LOGIN_API_URL, version=LOGIN_API_VERSION)
        session.start()
        import_known_application_services(session)


Provisioning Default Security Policies
--------------------------------------

.. code-block:: python
    :linenos:

    # TODO :(


Working with Push Center
------------------------

.. code-block:: python
    :linenos:

    from vspk.vsdk.v3_2 import *
    from time import sleep
    from pprint import pprint

    class EnterpriseGroupsController (object):

        def __init__(self, parent_enterprise, push_center):

            self.enterprise = parent_enterprise

            # let's fetch current groups
            self.enterprise.groups.fetch()

            # register our method as a push event delegate
            push_center.add_delegate(self.on_receive_user_push)

        def on_receive_user_push(self, data):

            push_processed = False

            # a single push can contains multiple events as they are clobbed together by the server if needed
            for event in data["events"]:

                # if the push is not about users, we don't care
                if event["entityType"] != NUGroup.rest_name:
                    continue

                # We get the data. Server sends an array of entities, but it can contain one object only
                group_info = event["entities"][0]

                # if the pushed user is not part of the parent enterprise, we also don't care
                if group_info["parentID"] != self.enterprise.id:
                    continue

                # create a transient NUUser from the data
                pushed_group = NUGroup(data=group_info)

                if event["type"] == "CREATE":
                    # locally insert the object in the correct children list
                    self.enterprise.add_child(pushed_group)

                elif event["type"] == "UPDATE":
                    # locally replace a user with the new version in the correct children list
                    self.enterprise.update_child(pushed_group)

                elif event["type"] == "DELETE":
                    # locally remove the user from the correct children list
                    self.enterprise.remove_child(pushed_group)

                push_processed = True

            # if we processed a push, we print the current group list
            if push_processed:
                print "Current groups:"
                for group in self.enterprise.groups:
                    print " - %s" % group.name



    if __name__ == "__main__":

        # we create a session
        session = NUVSDSession("csproot", "csproot", "csp", "https://api.nuagenetworks.net:8443", "3.2")
        session.start()

        # we start the push center
        session.push_center.start()

        # we get an enterprise
        enterprise = session.user.enterprises.get_first(filter="name == 'Triple A'")

        # we create a controller
        controller = EnterpriseGroupsController(enterprise, session.push_center)

        # from now on, the user list of enterprise will always be up to date from the server!

        while True:
            sleep(1000)
