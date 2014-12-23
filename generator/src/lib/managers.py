# -*- coding: utf-8 -*-

import os
import shutil
import threading

from git import Repo, GitCommandError
from printer import Printer


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
        self.branch = str(branch)
        self.repo = None
        self._nb_changes = 0

        self.remove_directory()
        self.repo = Repo.clone_from(url=self.url, to_path=self.directory)

        try:
            self.repo.git.checkout(self.branch)
            Printer.log('Switching to branch %s' % self.branch)

        except GitCommandError:
            Printer.log('Branch %s does not exist yet. Creating it...' % self.branch)
            branch = self.repo.create_head(self.branch)
            self.repo.head.reference = branch
            # remote = self.repo.remote()
            # remote.push(self.repo.head)

    def commit(self, message):
        """ Add all modification and add a commit message

            Args:
                message: the message for the commit

            Returns:
                Returns the number of diffs affected by the commit
                No commit are made if no diffs are found

        """
        diffs = self.repo.index.diff(None)
        nb_diffs = len(diffs)
        nb_untracked_files = len(self.repo.untracked_files)

        if nb_diffs:

            for diff in diffs:
                if diff.b_mode == 0 and diff.b_blob is None:
                    self.repo.index.remove(items=[diff.a_blob.path])
                else:
                    self.repo.index.add(items=[diff.a_blob.path])

        if nb_untracked_files > 0:
            self.repo.index.add(items=self.repo.untracked_files)

        self._nb_changes = nb_diffs + nb_untracked_files

        if self._nb_changes > 0:
            self.repo.index.commit(message)

        return self._nb_changes

    def push(self):
        """ Push all modififcation to the repository

        """
        if self._nb_changes > 0:
            remote = self.repo.remote()
            remote.push(self.repo.head)
            self._nb_changes = 0

    def remove_directory(self):
        """ Clean the clone repository

        """
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
