# -*- coding: utf-8 -*-

import os
import shutil
import threading

from git import Repo, GitCommandError
from monolithe.lib.utils.printer import Printer


class TaskManager(object):
    """ Multi threading manager """

    def __init__(self):
        """ Initializes a TaskManager

        """
        self.threads = list()

    def wait_until_exit(self):
        """ Wait until all the threads are finished.

        """
        [t.join() for t in self.threads]

        self.threads = list()

    def start_task(self, method, *args, **kwargs):
        """ Start a task in a separate thread

            Args:
                method: the method to start in a separate thread
                args: Accept args/kwargs arguments
        """
        thread = threading.Thread(target=method, args=args, kwargs=kwargs)
        thread.is_daemon = False
        thread.start()
        self.threads.append(thread)
