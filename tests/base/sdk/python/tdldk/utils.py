# -*- coding: utf-8 -*-
#
# __code_header example
# put your license header here
# it will be added to all the generated files
#

import logging
logger = logging.getLogger("tdldk")

def set_log_level(level, handler=None):
    """ Set both tdldk and Bambou2 log level to the given level

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

    from bambou2 import bambou_logger, pushcenter_logger

    if handler is None:
        handler = logging.StreamHandler()

    bambou_logger.setLevel(level)
    bambou_logger.addHandler(handler)

    pushcenter_logger.setLevel(level)
    pushcenter_logger.addHandler(handler)

    logger.setLevel(level)
    logger.addHandler(handler)
