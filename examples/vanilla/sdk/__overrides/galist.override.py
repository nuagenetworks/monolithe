def is_complete(self):
    """ Returns if all the tasks in the list are complete
    """
    for task in self.tasks:
        if not task.is_complete():
            return False

    return True

