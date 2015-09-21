# -*- coding: utf-8 -*-

import logging
import requests

from monolithe.lib import Printer


class TestHelper(object):
    """ Helper to make tests easier

    """
    _sdk = None
    _debug = False
    _session_class_name = None

    @classmethod
    def set_debug_mode(cls, debug=True):
        """ Activate debug mode

        """
        cls._debug = debug

        if cls._debug:
            cls._sdk.utils.set_log_level(logging.DEBUG)
        else:
            cls._sdk.utils.set_log_level(logging.ERROR)

    @classmethod
    def trace(cls, connection):
        """ Trace connection information

        """
        if not connection:
            return

        request = connection.request
        response = connection.response

        Printer.warn("%s %s [Response %s]" % (request.method, request.url, response.status_code))
        Printer.log("Header")
        Printer.json(request.headers)
        Printer.log("Body")
        Printer.json(request.data)
        Printer.log("Response")
        Printer.json(response.data)
        if len(response.errors):
            Printer.log("Errors")
            Printer.json(response.errors)

    @classmethod
    def use_sdk(cls, sdk, session_class_name):
        """ Retain used sdk

        """
        cls._session_class_name = session_class_name
        cls._sdk = sdk

    @classmethod
    def current_push_center(cls, session_class_name):
        """ Get current push center

        """

        session = getattr(cls._sdk, cls._session_class_name).get_current_session()
        return session.push_center

    @classmethod
    def set_api_key(cls, api_key):
        """ Change api key

        """
        session = getattr(cls._sdk, cls._session_class_name).get_current_session()
        session.login_controller.api_key = api_key

    @classmethod
    def session_headers(cls):
        """ Get headers

        """
        session = getattr(cls._sdk, cls._session_class_name).get_current_session()
        controller = session.login_controller

        headers = dict()
        headers["Content-Type"] = "application/json"
        headers["X-Nuage-Organization"] = controller.enterprise
        headers["Authorization"] = controller.get_authentication_header()

        return headers

    @classmethod
    def send_request(cls, method, url, data=None, remove_header=None):
        """ Send request with removed header

        """
        headers = cls.session_headers()

        if remove_header:
            headers.pop(remove_header)

        return requests.request(method=method, url=url, data=data, verify=False, headers=headers)

    @classmethod
    def send_post(cls, url, data, remove_header=None):
        """ Send a POST request

        """
        return cls.send_request(method="post", url=url, data=data, remove_header=remove_header)

    @classmethod
    def send_put(cls, url, data, remove_header=None):
        """ Send a PUT request

        """
        return cls.send_request(method="put", url=url, data=data, remove_header=remove_header)

    @classmethod
    def send_delete(cls, url, data, remove_header=None):
        """ Send a DELETE request

        """
        return cls.send_request(method="delete", url=url, data=data, remove_header=remove_header)

    @classmethod
    def send_get(cls, url, remove_header=None):
        """ Send a GET request

        """
        return cls.send_request(method="get", url=url, remove_header=remove_header)
