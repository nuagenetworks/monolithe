# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#



from .fetchers import GATasksFetcher


from .fetchers import GAMetadatasFetcher

from bambou import NURESTObject


class GAList(NURESTObject):
    """ Represents a List in the TDL

        Notes:
            Represent a a list of task to do.
    """

    __rest_name__ = "list"
    __resource_name__ = "lists"

    

    def __init__(self, **kwargs):
        """ Initializes a List instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> list = GAList(id=u'xxxx-xxx-xxx-xxx', name=u'List')
                >>> list = GAList(data=my_dict)
        """

        super(GAList, self).__init__()

        # Read/Write Attributes
        
        self._description = None
        self._title = None
        
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="title", remote_name="title", attribute_type=str, is_required=True, is_unique=False)
        

        # Fetchers
        
        
        self.tasks = GATasksFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.metadatas = GAMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def description(self):
        """ Get description value.

            Notes:
                The description

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                The description

                
        """
        self._description = value

    
    @property
    def title(self):
        """ Get title value.

            Notes:
                The title

                
        """
        return self._title

    @title.setter
    def title(self, value):
        """ Set title value.

            Notes:
                The title

                
        """
        self._title = value

    

    
    ## Custom methods
    def is_complete(self):
        """ Returns if all the tasks in the list are complete
        """
        for task in self.tasks:
            if not task.is_complete():
                return False
    
        return True
    