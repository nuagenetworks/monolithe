# -*- coding: utf-8 -*-
{{ header }}

from bambou import NURESTFetcher


class {{ sdk_class_prefix }}{{ specification.plural_name }}Fetcher(NURESTFetcher):
    """ Represents a {{ sdk_class_prefix }}{{ specification.plural_name }} fetcher

        Notes:
            This fetcher enables to fetch {{ sdk_class_prefix }}{{ specification.name }} objects.

        See:
            bambou.NURESTFetcher
    """

    @classmethod
    def managed_class(cls):
        """ Return {{ sdk_class_prefix }}{{ specification.name }} class that is managed.

            Returns:
                {{ sdk_name }}.{{ sdk_class_prefix }}{{ specification.name }}: the managed class
        """

        from .. import {{ sdk_class_prefix }}{{ specification.name }}
        return {{ sdk_class_prefix }}{{ specification.name }}

