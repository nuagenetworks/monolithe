# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NULDAPConfiguration(NURESTObject):
    """ Represents a LDAPConfiguration object """

    def __init__(self):
        """ Initializing object """

        super(NULDAPConfiguration, self).__init__()

        # Read/Write Attributes

        self.accept_all_certificates = None
        self.certificate = None
        self.enabled = None
        self.port = None
        self.server = None
        self.ssl_enabled = None
        self.user_dn_template = None

        self.expose_attribute(local_name=u"accept_all_certificates", remote_name=u"acceptAllCertificates", attribute_type=bool)
        self.expose_attribute(local_name=u"certificate", remote_name=u"certificate", attribute_type=str)
        self.expose_attribute(local_name=u"enabled", remote_name=u"enabled", attribute_type=bool)
        self.expose_attribute(local_name=u"port", remote_name=u"port", attribute_type=str)
        self.expose_attribute(local_name=u"server", remote_name=u"server", attribute_type=str)
        self.expose_attribute(local_name=u"ssl_enabled", remote_name=u"SSLEnabled", attribute_type=bool)
        self.expose_attribute(local_name=u"user_dn_template", remote_name=u"userDNTemplate", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"ldapconfiguration"

    # REST methods
