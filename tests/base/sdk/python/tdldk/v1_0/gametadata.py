# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#


from bambou import NURESTObject


class GAMetadata(NURESTObject):
    """ Represents a Metadata in the TDL

        Notes:
            None
    """

    __rest_name__ = "metadata"
    __resource_name__ = "metadatas"

    

    def __init__(self, **kwargs):
        """ Initializes a Metadata instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> metadata = GAMetadata(id=u'xxxx-xxx-xxx-xxx', name=u'Metadata')
                >>> metadata = GAMetadata(data=my_dict)
        """

        super(GAMetadata, self).__init__()

        # Read/Write Attributes
        
        self._blob = None
        
        self.expose_attribute(local_name="blob", remote_name="blob", attribute_type=str, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def blob(self):
        """ Get blob value.

            Notes:
                the blob

                
        """
        return self._blob

    @blob.setter
    def blob(self, value):
        """ Set blob value.

            Notes:
                the blob

                
        """
        self._blob = value

    

    