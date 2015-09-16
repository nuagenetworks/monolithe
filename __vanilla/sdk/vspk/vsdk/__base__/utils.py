# -*- coding: utf-8 -*-

import logging
vsdk_logger = logging.getLogger('vsdk')


def set_log_level(level, handler=None):
    """ Set both vsdk and Bambou log level to the given level

        Args:
            level (logging.level): a logging level
            handler (logging.Handler): a logging handler

        Notes:
            if no handler is provided, it will automatically create a new StreamHandler.

        Examples:
            >>> set_log_level(logging.INFO)
            >>> set_log_level(logging.DEBUG, logging.Streamhandler())
            >>> set_log_level(logging.ERROR)

    """

    from bambou import bambou_logger, pushcenter_logger

    if handler is None:
        handler = logging.StreamHandler()

    bambou_logger.setLevel(level)
    bambou_logger.addHandler(handler)

    pushcenter_logger.setLevel(level)
    pushcenter_logger.addHandler(handler)

    vsdk_logger.setLevel(level)
    vsdk_logger.addHandler(handler)
