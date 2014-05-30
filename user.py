# -*- coding:utf-8 -*-

from restnuage import NURESTBasicUser


class User(NURESTBasicUser):

    def __init__(self, id=None,
                       email=None,
                       username=None,
                       password=None,
                       api_key=None,
                       creation_date=None,
                       external_id=None,
                       local_id=None,
                       owner=None,
                       parent_id=None,
                       parent_type=None,
                       firstname=None,
                       lastname=None,
                       enterprise_id=None,
                       enterprise_name=None,
                       role=None,
                       avatar_type=None,
                       avatar_data=None,
                       api_key_expiry=None):
        """ Creates a new user """

        super(User, self).__init__(creation_date=creation_date,
                                   external_id=external_id,
                                   id=id,
                                   local_id=local_id,
                                   owner=owner,
                                   parent_id=parent_id,
                                   parent_type=parent_type,
                                   username=username,
                                   password=password,
                                   api_key=api_key)
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.enterprise_id = enterprise_id
        self.enterprise_name = enterprise_name
        self.role = role
        self.avatar_type = avatar_type
        self.avatar_data = avatar_data
        self.api_key_expiry = api_key_expiry

        self.expose_attribute(local_name='email', remote_name='email')
        self.expose_attribute(local_name='firstname', remote_name='firstName')
        self.expose_attribute(local_name='lastname', remote_name='lastName')
        self.expose_attribute(local_name='enterprise_id', remote_name='enterpriseID')
        self.expose_attribute(local_name='enterprise_name', remote_name='enterpriseName')
        self.expose_attribute(local_name='role', remote_name='role')
        self.expose_attribute(local_name='avatar_type', remote_name='avatarType')
        self.expose_attribute(local_name='avatar_data', remote_name='avatarData')
        self.expose_attribute(local_name='api_key_expiry', remote_name='APIKeyExpiry')

        # Overides from parents because rest name changed
        self.expose_attribute(local_name='username', remote_name='userName')  # TODO : Declare bug here
        self.expose_attribute(local_name='external_id', remote_name='externalId')  # TODO : Declare bug here

    @classmethod
    def get_remote_name(cls):
        """ Provides user classname  """

        return "me"

    @classmethod
    def is_resource_name_fixed(cls):
        """ Boolean to say if the resource name should be fixed. Default is False """

        return True
