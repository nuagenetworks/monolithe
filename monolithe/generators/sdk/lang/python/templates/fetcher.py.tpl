# -*- coding: utf-8 -*-
{{ header }}

from bambou import NURESTFetcher


class {{ class_prefix }}{{ specification.entity_name_plural }}Fetcher(NURESTFetcher):
    """ Represents a {{ class_prefix }}{{ specification.entity_name_plural }} fetcher

        Notes:
            This fetcher enables to fetch {{ class_prefix }}{{ specification.entity_name }} objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return {{ class_prefix }}{{ specification.entity_name }} class that is managed.

            Returns:
                {{ name }}.{{ class_prefix }}{{ specification.entity_name }}: the managed class
        """

        from .. import {{ class_prefix }}{{ specification.entity_name }}
        return {{ class_prefix }}{{ specification.entity_name }}

    {% if override_content %}
    ## Custom methods
    {{ override_content.replace('\n', '\n    ') }}
    {% endif %}
