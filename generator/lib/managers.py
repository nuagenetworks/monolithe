# -*- coding: utf-8 -*-

import shutil
import threading

from git import Repo
from printer import Printer

class TaskManager(object):

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


class GitManager(object):
    """ Manager of git repository

    """

    def __init__(self, url, branch, directory):
        """ Initializes a GitManager

            Args:
                url: url of the git repository to clone
                branch: name of the branch
                directory: the directory name

        """
        self.url = url
        self.directory = directory
        self.branch = branch
        self.repo = None
        self._nb_diffs = 0

    def clone(self):
        """ Clone the branch of the repository

        """
        # TODO-CS: If the branch does not exists, it will throw an exception!
        self.repo = Repo.clone_from(url=self.url, branch=self.branch, to_path=self.directory)

    def commit(self, message):
        """ Add all modification and add a commit message

            Args:
                message: the message for the commit

            Returns:
                Returns the number of diffs affected by the commit
                No commit are made if no diffs are found

        """
        diffs = self.repo.index.diff(None)
        self._nb_diffs = len(diffs)

        if self._nb_diffs:
            self.repo.index.add([diff.a_blob.path for diff in diffs])
            self.repo.index.commit(message)

        return self._nb_diffs

    def push(self):
        """ Push all modififcation to the repository

        """
        if self._nb_diffs > 0:
            remote = self.repo.remote()
            push_info = remote.push()

            if not push_info.flags & PushInfo.ERROR:
                self._nb_diffs = 0

    def remove_directory(self):
        """ Clean the clone repository

        """
        shutil.rmtree(self.directory)