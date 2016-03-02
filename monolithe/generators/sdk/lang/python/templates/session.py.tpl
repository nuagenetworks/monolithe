# -*- coding: utf-8 -*-
{{ header }}

from bambou import NURESTSession
from bambou.exceptions import InternalConsitencyError
from .{{ class_prefix|lower }}{{ root_api|lower }} import {{ class_prefix }}{{ root_api|capitalize }}


class {{ class_prefix }}{{ product_accronym }}Session(NURESTSession):
    """ {{ product_accronym }} User Session

        Session can be started and stopped whenever its needed
    """

    def __init__(self, username, enterprise, api_url, password=None, certificate=None):
        """ Initializes a new sesssion

            Args:
                username (string): the username
                password (string): the password
                enterprise (string): the enterprise
                api_url (string): the url to the api

            Example:
                >>> session =  {{ class_prefix }}{{ product_accronym|lower }}Session(username="csproot", password="csproot", enterprise="csp", api_url="https://{{ product_accronym }}:8443")
                >>> session.start()

        """

        if certificate is None and password is None:
            raise InternalConsitencyError('{{ class_prefix }}{{ product_accronym|lower }}Session needs either a password or a certificate')

        super({{ class_prefix }}{{ product_accronym }}Session, self).__init__(username=username, password=password, enterprise=enterprise, api_url=api_url, api_prefix="{{ api_prefix }}", version=str(self.version), certificate=certificate)

    @property
    def version(self):
        """ Returns the current {{ product_accronym }} version

        """
        return {{ version }}

    @property
    def {{root_api}}(self):
        """ Returns the root object

        """
        return self.root_object

    @classmethod
    def create_root_object(self):
        """ Returns a new instance

        """
        return {{ class_prefix }}{{ root_api|capitalize }}()

    {% if override_content %}
    ## Custom methods
    {{ override_content.replace('\n', '\n    ') }}
    {% endif %}
