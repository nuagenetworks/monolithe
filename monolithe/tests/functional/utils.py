# -*- coding: utf-8 -*-

import json

from requests.models import Response
from mock import MagicMock


class MockUtils(object):

    @classmethod
    def create_swagger_response(cls, status_code, filepath):
        """ Build a fake response

            Args:
                status_code (string): the status code
                filepath (string): the file path

        """

        response = Response()
        response.status_code = status_code

        if filepath:
            content = json.load(open(filepath))
        else:
            content = dict()

        response._content = content

        return MagicMock(return_value=response)

    @classmethod
    def get_mock_parameter(cls, mock, name):
        """ Get the argument of a mock call

            Args:
                mock: the mock that has been called
                name: the name of the argument

        """
        args = mock.call_args[1]

        if name in args:
            return args[name]

        return None
