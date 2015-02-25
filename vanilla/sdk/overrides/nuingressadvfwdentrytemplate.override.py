def is_template(self):
    """ Verify that the object is a template

        Returns:
            (bool): True if the object is a template
    """
    return True

def is_from_template(self):
    """ Verify if the object has been instantiated from a template

        Note:
            The object has to be fetched. Otherwise, it does not
            have information from its parent

        Returns:
            (bool): True if the object is a template
    """
    return self.parent and self.rest_name != self.parent_type