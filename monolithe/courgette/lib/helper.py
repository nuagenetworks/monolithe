# -*- coding: utf-8 -*-

import logging
import requests

from monolithe.lib import Printer


class TestHelper(object):
    """ Helper to make tests easier

    """
    def __init__(self):
       self._sdk = None
       self._debug = False
       self._session_class_name = None

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

    def use_sdk(self, sdk, session_class_name):
        """ Retain used sdk

        """
        self._session_class_name = session_class_name
        self._sdk = sdk

    def current_push_center(self, session_class_name):
        """ Get current push center

        """

        session = getattr(self._sdk, self._session_class_name).get_current_session()
        return session.push_center

    def set_api_key(self, api_key, sdk_object=None):
        """ Change api key

        """
        session = getattr(self._sdk, self._session_class_name).get_current_session()
        session.login_controller.api_key = api_key

    def session_headers(self):
        """ Get headers

        """
        session = getattr(self._sdk, self._session_class_name).get_current_session()
        controller = session.login_controller

        headers = dict()
        headers["Content-Type"] = "application/json"
        headers["X-Nuage-Organization"] = controller.enterprise
        headers["Authorization"] = controller.get_authentication_header()

        return headers

    def send_request(self, method, url, data=None, remove_header=None):
        """ Send request with removed header

        """
        headers = self.session_headers()

        if remove_header:
            headers.pop(remove_header)

        return requests.request(method=method, url=url, data=data, verify=False, headers=headers)

    def send_post(self, url, data, remove_header=None):
        """ Send a POST request

        """
        return self.send_request(method="post", url=url, data=data, remove_header=remove_header)

    def send_put(self, url, data, remove_header=None):
        """ Send a PUT request

        """
        return self.send_request(method="put", url=url, data=data, remove_header=remove_header)

    def send_delete(self, url, data, remove_header=None):
        """ Send a DELETE request

        """
        return self.send_request(method="delete", url=url, data=data, remove_header=remove_header)

    def send_get(self, url, remove_header=None):
        """ Send a GET request

        """
        return self.send_request(method="get", url=url, remove_header=remove_header)
