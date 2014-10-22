# -*- coding: utf-8 -*-


from bambou import NURESTObject
from time import time

class NULicense(NURESTObject):
    """ Represents a License object """

    def __init__(self):
        """ Initializing object """

        super(NULicense, self).__init__()

        # Read/Write Attributes

        self.allowed_cpes_count = None
        self.allowed_nics_count = None
        self.allowed_vms_count = None
        self.allowed_vrsgs_count = None
        self.allowed_vrss_count = None
        self.city = None
        self.company = None
        self.country = None
        self.customer_key = None
        self.email = None
        self.expiration_date = None
        self.is_cluster_license = None
        self.license = None
        self.license_id = None
        self.license_type = None
        self.major_release = None
        self.minor_release = None
        self.phone = None
        self.product_version = None
        self.provider = None
        self.state = None
        self.street = None
        self.user_name = None
        self.zip = None

        self.expose_attribute(local_name=u"allowed_cpes_count", remote_name=u"allowedCPEsCount", attribute_type=str)
        self.expose_attribute(local_name=u"allowed_nics_count", remote_name=u"allowedNICsCount", attribute_type=str)
        self.expose_attribute(local_name=u"allowed_vms_count", remote_name=u"allowedVMsCount", attribute_type=str)
        self.expose_attribute(local_name=u"allowed_vrsgs_count", remote_name=u"allowedVRSGsCount", attribute_type=str)
        self.expose_attribute(local_name=u"allowed_vrss_count", remote_name=u"allowedVRSsCount", attribute_type=str)
        self.expose_attribute(local_name=u"city", remote_name=u"city", attribute_type=str)
        self.expose_attribute(local_name=u"company", remote_name=u"company", attribute_type=str)
        self.expose_attribute(local_name=u"country", remote_name=u"country", attribute_type=str)
        self.expose_attribute(local_name=u"customer_key", remote_name=u"customerKey", attribute_type=str)
        self.expose_attribute(local_name=u"email", remote_name=u"email", attribute_type=str)
        self.expose_attribute(local_name=u"expiration_date", remote_name=u"expirationDate", attribute_type=time)
        self.expose_attribute(local_name=u"is_cluster_license", remote_name=u"isClusterLicense", attribute_type=bool)
        self.expose_attribute(local_name=u"license", remote_name=u"license", attribute_type=str)
        self.expose_attribute(local_name=u"license_id", remote_name=u"licenseID", attribute_type=int)
        self.expose_attribute(local_name=u"license_type", remote_name=u"licenseType", attribute_type=str)
        self.expose_attribute(local_name=u"major_release", remote_name=u"majorRelease", attribute_type=int)
        self.expose_attribute(local_name=u"minor_release", remote_name=u"minorRelease", attribute_type=int)
        self.expose_attribute(local_name=u"phone", remote_name=u"phone", attribute_type=str)
        self.expose_attribute(local_name=u"product_version", remote_name=u"productVersion", attribute_type=str)
        self.expose_attribute(local_name=u"provider", remote_name=u"provider", attribute_type=str)
        self.expose_attribute(local_name=u"state", remote_name=u"state", attribute_type=str)
        self.expose_attribute(local_name=u"street", remote_name=u"street", attribute_type=str)
        self.expose_attribute(local_name=u"user_name", remote_name=u"userName", attribute_type=str)
        self.expose_attribute(local_name=u"zip", remote_name=u"zip", attribute_type=str)

        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u"license"

    # REST methods
