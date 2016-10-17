# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#



from .fetchers import GAMetadatasFetcher

from bambou import NURESTObject


class GAUser(NURESTObject):
    """ Represents a User in the TDL

        Notes:
            Represent a user.
    """

    __rest_name__ = "user"
    __resource_name__ = "users"

    

    def __init__(self, **kwargs):
        """ Initializes a User instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> user = GAUser(id=u'xxxx-xxx-xxx-xxx', name=u'User')
                >>> user = GAUser(data=my_dict)
        """

        super(GAUser, self).__init__()

        # Read/Write Attributes
        
        self._last_name = None
        self._age = None
        self._first_name = None
        self._user_name = None
        
        self.expose_attribute(local_name="last_name", remote_name="lastName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="age", remote_name="age", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="first_name", remote_name="firstName", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="user_name", remote_name="userName", attribute_type=str, is_required=True, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = GAMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def last_name(self):
        """ Get last_name value.

            Notes:
                The last name

                
                This attribute is named `lastName` in TDL API.
                
        """
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        """ Set last_name value.

            Notes:
                The last name

                
                This attribute is named `lastName` in TDL API.
                
        """
        self._last_name = value

    
    @property
    def age(self):
        """ Get age value.

            Notes:
                The age of the user

                
        """
        return self._age

    @age.setter
    def age(self, value):
        """ Set age value.

            Notes:
                The age of the user

                
        """
        self._age = value

    
    @property
    def first_name(self):
        """ Get first_name value.

            Notes:
                The first name

                
                This attribute is named `firstName` in TDL API.
                
        """
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        """ Set first_name value.

            Notes:
                The first name

                
                This attribute is named `firstName` in TDL API.
                
        """
        self._first_name = value

    
    @property
    def user_name(self):
        """ Get user_name value.

            Notes:
                the login

                
                This attribute is named `userName` in TDL API.
                
        """
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """ Set user_name value.

            Notes:
                the login

                
                This attribute is named `userName` in TDL API.
                
        """
        self._user_name = value

    

    