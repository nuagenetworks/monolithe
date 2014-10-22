# -*- coding: utf-8 -*-


from bambou import NURESTObject


class NUDiskStats(NURESTObject):
    """ Represents a DiskStats object """

    def __init__(self):
        """ Initializing object """

        super(NUDiskStats, self).__init__()

        # Read/Write Attributes



        # Fetchers


    @classmethod
    def get_remote_name(cls):
        """ Remote name that will be used to generates URI """

        return u""

    # REST methods
