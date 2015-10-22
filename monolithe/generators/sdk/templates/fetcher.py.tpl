# -*- coding: utf-8 -*-
{{ header }}

from bambou import NURESTFetcher


class {{ sdk_class_prefix }}{{ specification.plural_name }}Fetcher(NURESTFetcher):
    """ Represents a {{ sdk_class_prefix }}{{ specification.plural_name }} fetcher

        Notes:
            This fetcher enables to fetch {{ sdk_class_prefix }}{{ specification.entity_name }} objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return {{ sdk_class_prefix }}{{ specification.entity_name }} class that is managed.

            Returns:
                {{ sdk_name }}.{{ sdk_class_prefix }}{{ specification.entity_name }}: the managed class
        """

        from .. import {{ sdk_class_prefix }}{{ specification.entity_name }}
        return {{ sdk_class_prefix }}{{ specification.entity_name }}

    {% if override_content %}
    ## Custom methods
    {{ override_content.replace('\n', '\n    ') }}
    {% endif %}
