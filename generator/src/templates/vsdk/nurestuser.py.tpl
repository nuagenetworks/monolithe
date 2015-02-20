# -*- coding: utf-8 -*-

# Copyright 2014 Alcatel-Lucent USA Inc.
# NU{{ model.name }}
# {{ model.description }}

{% for relation in model.relations %}
from ..fetchers import NU{{ relation.plural_name }}Fetcher{% endfor %}
from bambou import NURESTBasicUser{% if model.has_time_attribute %}
from time import time{% endif %}


class NU{{ model.name }}(NURESTBasicUser):
    """ Represents a user that can login to the VSD.

        Warning:
            This file has been autogenerated. You should never change it.
            Override vsdk.NU{{ model.name }} instead.
    """

    __rest_name__ = u"me"

    def __init__(self, **kwargs):
        """ Initializes a {{ model.name }} instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> {{ model.name.lower() }} = NU{{ model.name }}(id=u'xxxx-xxx-xxx-xxx', name=u'{{ model.name }}')
                >>> {{ model.name.lower() }} = NU{{ model.name }}(data=my_dict)
        """

        super(NU{{ model.name }}, self).__init__()

        # Read/Write Attributes
        {% for attribute in model.attributes %}
        self._{{ attribute.local_name|lower }} = None{% endfor %}
        {% for attribute in model.attributes %}
        self.expose_attribute(local_name=u"{{ attribute.local_name|lower }}", remote_name=u"{{ attribute.remote_name }}", attribute_type={{ attribute.local_type }}{% if attribute.is_required %}, is_required=True{% endif %}{% if attribute.is_unique %}, is_unique=True{% endif %}{% if attribute.choices %}, choices={{ attribute.choices|sort|trim }}{% endif %}){% endfor %}
        {% if model.relations|length > 0 %}
        # Fetchers
        {% for relation in model.relations %}
        self.{{ relation.instance_plural_name }} = []
        self.{{ relation.instance_plural_name }}_fetcher = NU{{ relation.plural_name }}Fetcher.fetcher_with_object(nurest_object=self, local_name=u"{{relation.instance_plural_name}}")
        {% endfor %}{% endif %}

        self._compute_args(**kwargs)

    # Properties
    {% for attribute in model.attributes %}
    def _get_{{ attribute.local_name }}(self):
        """ Get {{ attribute.local_name }} value.

            Notes:
                {{ attribute.description }}

                {% if attribute.local_name != attribute.remote_name %}
                This attribute is named `{{ attribute.remote_name }}` in VSD API.
                {% endif %}
        """
        return self._{{ attribute.local_name }}

    def _set_{{ attribute.local_name }}(self, value):
        """ Set {{ attribute.local_name }} value.

            Notes:
                {{ attribute.description }}

                {% if attribute.local_name != attribute.remote_name %}
                This attribute is named `{{ attribute.remote_name }}` in VSD API.
                {% endif %}
        """
        self._{{ attribute.local_name }} = value

    {{ attribute.local_name }} = property(_get_{{ attribute.local_name }}, _set_{{ attribute.local_name }})
    {% endfor %}
    # Methods

    @classmethod
    def is_resource_name_fixed(cls):
        """ Force resource name to True

            Returns:
                bool: always return True for NU{{ model.name }} objects

        """

        return True

    def get_resource_url(self):
        """ Get the resource url for the given object.

            Notes:
                This method overrides bambou.NURESTObject method.

            Returns:
                string: a url with NU{{ model.name }} specific resource name

            Example:
                >>> {{ model.name }}.get_resource_url()
                https://.../nuage/api/v3_1/me
        """

        name = self.__class__.rest_resource_name
        url = self.__class__.rest_base_url()
        return "%s/%s" % (url, name)

    def get_resource_url_for_child_type(self, nurest_object_type):
        """ Get the resource url for NU{{ model.name }}'s child objects.

            Notes:
                This method overrides bambou.NURESTObject method.

            Args:
                nurest_object_type (bambou.NURESTObject): type of child

            Returns:
                string: the url for the given object

            Example:
                >>> {{ model.name }}.get_resource_url_for_child_type(NUEnterprise)
                https://.../nuage/api/v3_1/enterprises
        """

        return "%s/%s" % (self.__class__.rest_base_url(), object_type.rest_resource_name)
