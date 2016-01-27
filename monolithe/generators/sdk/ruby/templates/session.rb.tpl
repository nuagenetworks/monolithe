# TODO: Complete this class to create the SDK Session.
# Take a look at the python version if necessary
{{ header }}

require "bambou.NURESTSession"
require "bambou.exceptions.InternalConsitencyError"
require ".{{ sdk_class_prefix|lower }}{{ sdk_root_api|lower }}.{{ sdk_class_prefix }}{{ sdk_root_api|capitalize }}"


class {{ sdk_class_prefix }}{{ product_accronym }}Session < NURESTSession:
    """ {{ product_accronym }} User Session

        Session can be started and stopped whenever its needed
    """

    def initialize(self, username, enterprise, api_url, password=None, certificate=None):
        """ Initializes a new sesssion

            Args:
                username (string): the username
                password (string): the password
                enterprise (string): the enterprise
                api_url (string): the url to the api

            Example:
                >>> session =  {{ sdk_class_prefix }}{{ product_accronym|lower }}Session(username="csproot", password="csproot", enterprise="csp", api_url="https://{{ product_accronym }}:8443")
                >>> session.start()

        """

        if certificate is None and password is None:
            raise InternalConsitencyError('{{ sdk_class_prefix }}{{ product_accronym|lower }}Session needs either a password or a certificate')

        super({{ sdk_class_prefix }}{{ product_accronym }}Session, self).__init__(username=username, password=password, enterprise=enterprise, api_url=api_url, api_prefix="{{ sdk_api_prefix }}", version=str(self.version), certificate=certificate)

    def version(self):
        """ Returns the current {{ product_accronym }} version

        """
        return @{{ version }}

    def {{sdk_root_api}}(self):
        """ Returns the root object

        """
        return @root_object

    def self.create_root_object(self):
        """ Returns a new instance

        """
        return {{ sdk_class_prefix }}{{ sdk_root_api|capitalize }}()

    {% if override_content %}
    ## Custom methods
    {{ override_content.replace('\n', '\n    ') }}
    {% endif %}