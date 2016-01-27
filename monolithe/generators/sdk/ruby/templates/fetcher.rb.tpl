# TODO: This Ruby file defines a fetcher that inherits from NURESTFetcher
{{ header }}

require 'bambou.NURESTFetcher'


class {{ sdk_class_prefix }}{{ specification.entity_name_plural }}Fetcher < NURESTFetcher:
    """ Represents a {{ sdk_class_prefix }}{{ specification.entity_name_plural }} fetcher

        Notes:
            This fetcher enables to fetch {{ sdk_class_prefix }}{{ specification.entity_name }} objects.

        See:
            bambou.NURESTFetcher
    """

    def self.managed_class(cls):
        """ Return {{ sdk_class_prefix }}{{ specification.entity_name }} class that is managed.

            Returns:
                {{ sdk_name }}.{{ sdk_class_prefix }}{{ specification.entity_name }}: the managed class
        """

        require "{{ sdk_class_prefix }}{{ specification.entity_name }}"
        return {{ sdk_class_prefix }}{{ specification.entity_name }}

    {% if override_content %}
    ## Custom methods
    {{ override_content.replace('\n', '\n    ') }}
    {% endif %}
