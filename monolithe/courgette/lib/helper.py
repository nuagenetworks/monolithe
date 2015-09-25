# -*- coding: utf-8 -*-

import logging
import requests

from monolithe.lib import Printer


class TestHelper(object):
    """ Helper to make tests easier

    """
    def __init__(self, sdk_module, sdk_session_class_name, api_url, api_username, api_password, api_enterprise):
        """
        """
        self._sdk_module = sdk_module
        self._sdk_session = getattr(self._sdk_module, sdk_session_class_name)(api_url=api_url, username=api_username, password=api_password, enterprise=api_enterprise)
        self._sdk_session.start()

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

    @property
    def session(self):
        return self._sdk_session

    @property
    def root_object(self):
        return self._sdk_session.root_object

    def current_push_center(self):
        """ Get current push center

        """
        return self._sdk_session.push_center

    def set_api_key(self, api_key, sdk_object=None):
        """ Change api key

        """
        self._sdk_session.login_controller.api_key = api_key

    def session_headers(self):
        """ Get headers

        """
        return {
            "Content-Type": "application/json",
            "X-Nuage-Organization": self._sdk_session.login_controller.enterprise,
            "Authorization": self._sdk_session.login_controller.get_authentication_header()
        }

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
