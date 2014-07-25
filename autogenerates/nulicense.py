# -*- coding: utf-8 -*-


from restnuage import NURESTObject
from time import time

class NULicense(NURESTObject):
    """ Represents a License object """

    def __init__(self):
        """ Initializing object """

        super(NULicense, self).__init__()

        # Read/Write Attributes
        
        self.allowed_nics_count = None
        self.allowed_vms_count = None
        self.city = None
        self.company = None
        self.country = None
        self.email = None
        self.expiration_date = None
        self.license = None
        self.license_id = None
        self.major_release = None
        self.minor_release = None
        self.phone = None
        self.product_version = None
        self.provider = None
        self.state = None
        self.street = None
        self.user_name = None
        self.zip = None
        
        self.expose_attribute(local_name=u"allowed_nics_count", remote_name=u"allowedNICsCount", attribute_type=str)
        self.expose_attribute(local_name=u"allowed_vms_count", remote_name=u"allowedVMsCount", attribute_type=str)
        self.expose_attribute(local_name=u"city", remote_name=u"city", attribute_type=str)
        self.expose_attribute(local_name=u"company", remote_name=u"company", attribute_type=str)
        self.expose_attribute(local_name=u"country", remote_name=u"country", attribute_type=str)
        self.expose_attribute(local_name=u"email", remote_name=u"email", attribute_type=str)
        self.expose_attribute(local_name=u"expiration_date", remote_name=u"expirationDate", attribute_type=time)
        self.expose_attribute(local_name=u"license", remote_name=u"license", attribute_type=str)
        self.expose_attribute(local_name=u"license_id", remote_name=u"licenseID", attribute_type=int)
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
    