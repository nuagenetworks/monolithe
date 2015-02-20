Code Snippets
=============

This section provides various code snippets and scripts you can use or get inspiration from to develop your own scripts or application using the VSDK.


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

    import vsdk
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
            domain.create_child_object(zone)
            domain.add_child(zone)

            #creates subnets
            for j in range(0, number_of_subnets_per_zone):

                # pull a subnet and get information about it
                subnetwork = subnets.next()
                ip = "%s" % subnetwork.network_address
                gw = "%s" % subnetwork.hosts().next()
                nm = "%s" % subnetwork.netmask

                subnet = subnet_class(name="Subnet %d %d" % (i, j), address=ip, netmask=nm, gateway=gw)
                zone.create_child_object(subnet)
                zone.add_child(subnet)

                # if the given domain is a template, we stop
                if is_template:
                    break

                # Otherwise we create the VPorts
                for k in range(0, number_of_vports_per_subnet):

                    vport = vsdk.NUVport(name="VPort %d-%d-%d", (i, j, k), type="VM", address_spoofing="INHERITED", multicast="INHERITED")
                    subnet.create_child_object(vport)
                    subnet.add_child(vport)


    if __name__ == "__main__":

        session = vsdk.NUVSDSession(username=LOGIN_USER, password=LOGIN_PASS, enterprise=LOGIN_ENTERPRISE, api_url=LOGIN_API_URL, version=LOGIN_API_VERSION).start()

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

    import vsdk

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

        vsdsession.user.create_child_object(gateway_template)

        # create a network port for each given network_port_names
        for network_port_name in network_port_names:

            network_port_template = vsdk.NUPortTemplate(name=network_port_name, physical_name=network_port_name, portType="NETWORK")
            gateway_template.create_child_object(network_port_template)


        # create an access port for each given access_port_names
        for access_port_name in access_port_names:

            access_port_template = vsdk.NUPortTemplate(name=access_port_name, physical_name=access_port_name, portType="ACCESS", vlan_range=vlan_range)
            gateway_template.create_child_object(access_port_template)

            # create a VLAN for each given vlans_values
            for vlan_value in vlans_values:

                vlan = vsdk.NUVLANTemplate(value=vlan_value)
                access_port_template.create_child_object(vlan)

        return gateway_template


    def create_datacenter_gateway(name, gateway_template, enterprise, vsdsession, permission="USE"):
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

        gateway = vsdk.NUGateway(name=name, personality=personality)
        vsdsession.user.instantiate_child_object(gateway, gateway_template)
        permission = vsdk.NUEnterprisePermission(permitted_action=permission, permitted_entity_id=enterprise.id)
        gateway.create_child_object(permission)

        return gateway

        if __name__ == "__main__":

            # start the session
            session = vsdk.NUVSDSession(username=LOGIN_USER, password=LOGIN_PASS, enterprise=LOGIN_ENTERPRISE, api_url=LOGIN_API_URL, version=LOGIN_API_VERSION)
            session.start()

            # get an enterprise
            enterprise = session.user.enterprises_fetcher.fetch(filter="name == 'Triple A'")

            # create a gateway template
            gw_tmpl = create_data_gateway_template("my template", "VSRG", ["port0"], ["port1", "port2"], "0-400", [100, 200], session)

            # instantiate a gateway from the template and give USE permission to enterprise
            gw = create_datacenter_gateway("gateway 1", gw_tmpl, enterprise, session)


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
    import vsdk

    def import_known_application_services(session):

        # pip install requests

        protocols = requests.get('http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv').content
        csvreader = csv.reader(protocols.split('\r\n'))

        for row in csvreader:

            try:
                name = row[0]
                port_number = row[1]
                protocol = row[2]
                description = row[3]

                if not name:
                    continue;

                appservice = vsdk.NUApplicationService()
                appservice.protocol = "6" if protocol is "tcp" else "17"
                appservice.name = "%s/%d - %s " % (appservice.protocol, port_number, name)
                appservice.destination_port = port_number
                appservice.description = description
                appservice.direction = "REFLEXIVE"
                appservice.ether_type = "0x0800"
                appservice.source_port = "*"
                appservice.dscp = "*"

                session.user.create_child_object(appservice)

            except Exception as ex:
                print ex;


    if __name__ == "__main__":

        session = vsdk.NUVSDSession(username=LOGIN_USER, password=LOGIN_PASS, enterprise=LOGIN_ENTERPRISE, api_url=LOGIN_API_URL, version=LOGIN_API_VERSION).start()
        import_known_application_services(session)


Provisioning Default Security Policies
--------------------------------------

.. code-block:: python
    :linenos:

    # TODO :(


