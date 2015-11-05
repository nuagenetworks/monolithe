# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#



from .fetchers import GAUsersFetcher

from bambou import NURESTObject


class GATask(NURESTObject):
    """ Represents a Task in the TDL

        Notes:
            Represent a task to do in a list
    """

    __rest_name__ = "task"
    __resource_name__ = "tasks"

    
    ## Constants
    
    CONST_STATUS_TODO = "TODO"
    
    CONST_STATUS_DONE = "DONE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a Task instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> task = GATask(id=u'xxxx-xxx-xxx-xxx', name=u'Task')
                >>> task = GATask(data=my_dict)
        """

        super(GATask, self).__init__()

        # Read/Write Attributes
        
        self._description = None
        self._status = None
        self._title = None
        
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="status", remote_name="status", attribute_type=str, is_required=False, is_unique=False, choices=[u'DONE', u'TODO'])
        self.expose_attribute(local_name="title", remote_name="title", attribute_type=str, is_required=True, is_unique=True)
        

        # Fetchers
        
        
        self.users = GAUsersFetcher.fetcher_with_object(parent_object=self, relationship="member")
        

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
    def status(self):
        """ Get status value.

            Notes:
                The status of the task

                
        """
        return self._status

    @status.setter
    def status(self, value):
        """ Set status value.

            Notes:
                The status of the task

                
        """
        self._status = value

    
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
        """ Returns if the task is complete
        """
        return self.status == "DONE"
    