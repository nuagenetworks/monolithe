# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#



from .fetchers import GAListsFetcher


from .fetchers import GAUsersFetcher

from bambou import NURESTRootObject


class GARoot(NURESTRootObject):
    """ Represents a Root in the TDL

        Notes:
            Root object of the APIh
    """

    __rest_name__ = "root"
    __resource_name__ = "root"

    

    def __init__(self, **kwargs):
        """ Initializes a Root instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> root = GARoot(id=u'xxxx-xxx-xxx-xxx', name=u'Root')
                >>> root = GARoot(data=my_dict)
        """

        super(GARoot, self).__init__()

        # Read/Write Attributes
        
        
        

        # Fetchers
        
        
        self.lists = GAListsFetcher.fetcher_with_object(parent_object=self, relationship="root")
        
        
        self.users = GAUsersFetcher.fetcher_with_object(parent_object=self, relationship="root")
        

        self._compute_args(**kwargs)

    # Properties
    

    